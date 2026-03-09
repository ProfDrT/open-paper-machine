---
description: Generate a statistical plot from CSV/JSON data using PaperBanana. Provide a data file and describe the visualization intent.
---

# Generate Plot: **$ARGUMENTS**

Read the figure-engine skill first.

## Steps
1. Parse `$ARGUMENTS` — extract the data file path and visualization intent
2. Read and validate the data file (CSV or JSON)
3. **PRIMARY**: Use the direct Python API via `paperbanana_direct.py` script:
   ```bash
   PB_SCRIPT="$(find ~/.claude/plugins -name paperbanana_direct.py -path '*/open-academic-paper-machine/*' 2>/dev/null | head -1)" && \
   python3 "$PB_SCRIPT" plot \
     --data '{"col1": [...], "col2": [...]}' \
     --caption "Description of the plot" \
     --output-dir figures/ \
     --filename "fig_results_name.png" \
     --iterations 3
   ```
4. If the script is not found, **FALLBACK**: call PaperBanana MCP `paperbanana_generate_plot`
5. If MCP also fails, **LAST RESORT**: generate using Python (matplotlib/seaborn) with academic styling
6. Save output PNG to `figures/` in the workspace (300 DPI, tight layout)
7. Provide the LaTeX `\begin{figure}` snippet ready for inclusion
8. Show the user the generated figure using the Read tool on the PNG path
