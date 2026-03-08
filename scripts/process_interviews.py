"""Process qualitative interview transcripts for analysis.

Reads interview Markdown files, generates an index with metadata,
and provides utilities for chunking and searching across transcripts.

Usage:
    from process_interviews import (
        load_interviews,
        build_index,
        chunk_interview,
        search_interviews,
        save_index,
    )

    interviews = load_interviews("interviews/")
    index = build_index(interviews)
    save_index(index, "interviews/INDEX.md")

CLI:
    python process_interviews.py <interviews_dir> [--rebuild-index]
"""

import re
import sys
from pathlib import Path


def load_interviews(directory: str) -> list[dict]:
    """Load all interview Markdown files from a directory.

    Skips INDEX.md, summary files, and the summaries/ subdirectory.

    Returns list of dicts with keys:
        path, filename, title, date, content, word_count
    """
    interviews_dir = Path(directory)
    if not interviews_dir.exists():
        print(f"Error: Directory not found: {directory}")
        return []

    interviews = []
    for md_file in sorted(interviews_dir.glob("*.md")):
        if md_file.name in ("INDEX.md", "README.md"):
            continue
        if "summary" in md_file.name.lower():
            continue

        content = md_file.read_text(encoding="utf-8")
        word_count = len(content.split())

        # Extract date and title from filename pattern: YYYY-MM-DD_Title.md
        match = re.match(r"(\d{4}-\d{2}-\d{2})_(.+)\.md", md_file.name)
        if match:
            date = match.group(1)
            title = match.group(2).replace("_", " ")
        else:
            date = ""
            title = md_file.stem.replace("_", " ")

        interviews.append({
            "path": str(md_file),
            "filename": md_file.name,
            "title": title,
            "date": date,
            "content": content,
            "word_count": word_count,
        })

    return interviews


def build_index(interviews: list[dict]) -> str:
    """Build a Markdown index of all interviews.

    The index contains metadata (date, title, word count) and
    the first ~200 words of each interview as a preview.
    """
    lines = [
        "# Interview Index",
        "",
        f"**Total interviews:** {len(interviews)}",
        f"**Total words:** {sum(i['word_count'] for i in interviews):,}",
        "",
        "---",
        "",
        "| # | Date | Interviewee / Title | Words |",
        "|---|------|---------------------|-------|",
    ]

    for idx, iv in enumerate(interviews, 1):
        lines.append(
            f"| {idx} | {iv['date']} | {iv['title']} | {iv['word_count']:,} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    for idx, iv in enumerate(interviews, 1):
        preview = " ".join(iv["content"].split()[:200])
        if iv["word_count"] > 200:
            preview += " [...]"
        lines.append(f"## {idx}. {iv['title']}")
        lines.append(f"**Date:** {iv['date']}  |  **Words:** {iv['word_count']:,}  |  **File:** `{iv['filename']}`")
        lines.append("")
        lines.append(f"> {preview}")
        lines.append("")

    return "\n".join(lines)


def chunk_interview(content: str, chunk_size: int = 800, overlap: int = 100) -> list[dict]:
    """Split an interview transcript into overlapping word-based chunks.

    Args:
        content: Full transcript text.
        chunk_size: Target words per chunk.
        overlap: Overlapping words between chunks.

    Returns:
        List of dicts with keys: chunk_id, start_word, end_word, text
    """
    words = content.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_text = " ".join(words[start:end])
        chunks.append({
            "chunk_id": len(chunks),
            "start_word": start,
            "end_word": end,
            "text": chunk_text,
        })
        if end >= len(words):
            break
        start = end - overlap

    return chunks


def search_interviews(
    interviews: list[dict],
    keywords: list[str],
    context_words: int = 80,
) -> list[dict]:
    """Search across all interviews for keyword matches.

    Returns list of matches with surrounding context.
    """
    results = []
    patterns = [re.compile(re.escape(kw), re.IGNORECASE) for kw in keywords]

    for iv in interviews:
        content = iv["content"]
        for pattern in patterns:
            for match in pattern.finditer(content):
                # Extract context around match
                start = max(0, match.start() - context_words * 6)  # ~6 chars/word
                end = min(len(content), match.end() + context_words * 6)

                # Expand to word boundaries
                while start > 0 and content[start] != " ":
                    start -= 1
                while end < len(content) and content[end] != " ":
                    end += 1

                results.append({
                    "interview": iv["title"],
                    "date": iv["date"],
                    "filename": iv["filename"],
                    "keyword": pattern.pattern,
                    "context": content[start:end].strip(),
                    "position": match.start(),
                })

    return results


def save_index(index_content: str, output_path: str) -> None:
    """Save the index to a Markdown file."""
    Path(output_path).write_text(index_content, encoding="utf-8")
    print(f"Index saved to {output_path}")


def save_summary(summary: str, output_path: str) -> None:
    """Save a structured summary to a Markdown file."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(summary, encoding="utf-8")


# --- CLI ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_interviews.py <interviews_dir> [--rebuild-index]")
        sys.exit(1)

    interviews_dir = sys.argv[1]
    interviews = load_interviews(interviews_dir)

    if not interviews:
        print("No interview files found.")
        sys.exit(1)

    print(f"Found {len(interviews)} interviews ({sum(i['word_count'] for i in interviews):,} total words)")

    index = build_index(interviews)
    index_path = str(Path(interviews_dir) / "INDEX.md")
    save_index(index, index_path)

    # Print keyword search example
    if "--search" in sys.argv:
        search_idx = sys.argv.index("--search")
        if search_idx + 1 < len(sys.argv):
            keyword = sys.argv[search_idx + 1]
            results = search_interviews(interviews, [keyword])
            print(f"\n{len(results)} matches for '{keyword}':")
            for r in results[:10]:
                print(f"  [{r['interview']}] ...{r['context'][:120]}...")
