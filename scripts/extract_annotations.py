"""Extract annotations from PDF files for review processing.

Uses PyMuPDF (fitz) to extract highlights, sticky notes, and text comments
from annotated PDFs (e.g., co-author review feedback).

Derived from 4 actual revision rounds on Blask & Funk (2026).

Usage:
    from extract_annotations import extract_annotations, annotations_to_markdown
    annotations = extract_annotations("path/to/annotated.pdf")
    print(annotations_to_markdown(annotations))

CLI:
    python extract_annotations.py path/to/annotated.pdf
"""

import json
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)


def extract_annotations(pdf_path: str) -> list[dict]:
    """Extract all annotations from a PDF file.

    Handles: Highlight, Underline, Squiggly, StrikeOut, Text (sticky note),
    FreeText, and Caret annotations.

    Returns list of dicts with keys:
        id, page, type, content, highlighted_text, author, rect
    """
    doc = fitz.open(pdf_path)
    annotations = []

    # Annotation type codes that use quadpoints for text marking
    TEXT_MARKUP_TYPES = {8, 9, 10, 11}  # Highlight, Underline, Squiggly, StrikeOut

    for page_num, page in enumerate(doc, 1):
        for annot in page.annots() or []:
            entry = {
                "id": len(annotations) + 1,
                "page": page_num,
                "type": annot.type[1],  # Human-readable type name
                "content": annot.info.get("content", "").strip(),
                "author": annot.info.get("title", ""),
                "rect": [round(x, 1) for x in annot.rect],
                "highlighted_text": "",
            }

            # Extract marked text via quadpoints (for highlights, underlines, etc.)
            if annot.type[0] in TEXT_MARKUP_TYPES and annot.vertices:
                quad_count = len(annot.vertices) // 4
                text_parts = []
                for i in range(quad_count):
                    quad = annot.vertices[i * 4 : (i + 1) * 4]
                    rect = fitz.Rect(
                        min(p[0] for p in quad),
                        min(p[1] for p in quad),
                        max(p[0] for p in quad),
                        max(p[1] for p in quad),
                    )
                    text = page.get_text("text", clip=rect).strip()
                    if text:
                        text_parts.append(text)
                entry["highlighted_text"] = " ".join(text_parts)

            # For FreeText annotations, the content IS the text
            if annot.type[0] == 2:  # FreeText
                if not entry["content"]:
                    entry["content"] = annot.get_text().strip()

            # Skip completely empty annotations
            if entry["content"] or entry["highlighted_text"]:
                annotations.append(entry)

    doc.close()
    return annotations


def annotations_to_markdown(annotations: list[dict]) -> str:
    """Format annotations as a readable markdown table."""
    if not annotations:
        return "No annotations found in this PDF."

    lines = [
        f"**{len(annotations)} annotations extracted**\n",
        "| # | Page | Type | Comment | Highlighted Text |",
        "|---|------|------|---------|------------------|",
    ]
    for a in annotations:
        comment = a["content"].replace("\n", " ").replace("|", "\\|")
        if len(comment) > 80:
            comment = comment[:77] + "..."
        highlighted = a["highlighted_text"].replace("\n", " ").replace("|", "\\|")
        if len(highlighted) > 60:
            highlighted = highlighted[:57] + "..."
        author = f" ({a['author']})" if a["author"] else ""
        lines.append(
            f"| {a['id']} | {a['page']} | {a['type']}{author} | {comment} | {highlighted} |"
        )
    return "\n".join(lines)


def annotations_to_json(annotations: list[dict], indent: int = 2) -> str:
    """Serialize annotations to JSON string."""
    return json.dumps(annotations, indent=indent, ensure_ascii=False)


# --- CLI ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_annotations.py <pdf_path> [--json]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_json = "--json" in sys.argv

    if not Path(pdf_path).exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    annotations = extract_annotations(pdf_path)

    if output_json:
        print(annotations_to_json(annotations))
    else:
        print(annotations_to_markdown(annotations))
