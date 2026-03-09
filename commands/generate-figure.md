---
description: Generate an academic diagram from a text description using PaperBanana. Provide a section of your paper or a methodology description and get a publication-quality figure.
---

# Generate Figure: **$ARGUMENTS**

Read the figure-engine skill first.

## Steps
1. Parse `$ARGUMENTS` — extract the source text or file reference and optional caption
2. If a file path is given, read it. If inline text, use it directly.
3. Write the source context to `/tmp/pb_source_context.txt` if it's long
4. **PRIMARY**: Use the direct Python API via `paperbanana_direct.py` script:
   ```bash
   PB_SCRIPT="$(find ~/.claude/plugins -name paperbanana_direct.py -path '*/open-academic-paper-machine/*' 2>/dev/null | head -1)" && \
   python3 "$PB_SCRIPT" diagram \
     --source-context "$(cat /tmp/pb_source_context.txt)" \
     --caption "Figure N: Caption" \
     --output-dir figures/ \
     --filename "fig_section_name.png" \
     --iterations 3
   ```
5. If the script is not found, **FALLBACK**: call PaperBanana MCP `paperbanana_generate_diagram`
6. If MCP also fails, **LAST RESORT**: generate using Python (matplotlib + graphviz/networkx)
7. Save output PNG to `figures/` in the workspace
8. Provide the LaTeX `\begin{figure}` snippet ready for inclusion
9. Show the user the generated figure using the Read tool on the PNG path
