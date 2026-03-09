#!/usr/bin/env python3
"""Direct PaperBanana API wrapper — bypasses MCP transport layer.

This script calls PaperBanana's Python API directly via asyncio,
avoiding the unreliable MCP stdio transport. It accepts CLI arguments
and outputs JSON to stdout.

Supports all features from the latest PaperBanana (llmsresearch/paperbanana),
including aspect ratio, input optimization, auto-refine, exemplar retrieval,
and multiple VLM/image providers (Gemini, OpenAI, Anthropic, Bedrock).

Usage (diagram):
    python3 paperbanana_direct.py diagram \
        --source-context "methodology text..." \
        --caption "Figure 1: ..." \
        --output-dir figures/ \
        --iterations 3

Usage (plot):
    python3 paperbanana_direct.py plot \
        --data '{"x":[1,2,3],"y":[4,5,6]}' \
        --caption "Bar chart of ..." \
        --output-dir figures/ \
        --iterations 3

Usage (evaluate):
    python3 paperbanana_direct.py evaluate \
        --generated path/to/generated.png \
        --reference path/to/reference.png \
        --context "methodology text..." \
        --caption "Figure caption"

Usage (download-references):
    python3 paperbanana_direct.py download-references

All commands print JSON to stdout on success:
    {"status":"ok","image_path":"...","iterations":3,"metadata":{...}}

On failure:
    {"status":"error","message":"..."}

Environment:
    GOOGLE_API_KEY     — Required for Gemini provider (default)
    OPENAI_API_KEY     — For OpenAI provider
    ANTHROPIC_API_KEY  — For Anthropic Claude VLM provider
    OPENROUTER_API_KEY — For OpenRouter provider
    AWS_PROFILE        — For AWS Bedrock provider
    Loads .env from ~/.paperbanana.env or CWD/.env automatically.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import sys
from pathlib import Path


def _load_env():
    """Load environment from .env files if GOOGLE_API_KEY not already set.

    Priority: env var > ~/.paperbanana.env > CWD/.env
    The global ~/.paperbanana.env takes precedence over project .env to avoid
    stale project keys overriding a working global key.
    """
    if os.environ.get("GOOGLE_API_KEY"):
        return
    for env_path in [
        Path.home() / ".paperbanana.env",
        Path.cwd() / ".env",
    ]:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("'\"")
                    if key and value:
                        os.environ.setdefault(key, value)
            break


def _json_ok(image_path: str, iterations: int, metadata: dict | None = None):
    """Print success JSON and exit."""
    print(json.dumps({
        "status": "ok",
        "image_path": str(image_path),
        "iterations": iterations,
        "metadata": metadata or {},
    }))
    sys.exit(0)


def _json_error(message: str):
    """Print error JSON and exit."""
    print(json.dumps({"status": "error", "message": str(message)}))
    sys.exit(1)


def _build_settings(args):
    """Build Settings from CLI args, supporting all new parameters."""
    from paperbanana.core.config import Settings

    kwargs = {"refinement_iterations": args.iterations}

    # New features from latest PaperBanana
    if hasattr(args, "aspect_ratio") and args.aspect_ratio:
        pass  # aspect_ratio goes into GenerationInput, not Settings
    if hasattr(args, "optimize") and args.optimize:
        kwargs["optimize_inputs"] = True
    if hasattr(args, "auto_refine") and args.auto_refine:
        kwargs["auto_refine"] = True
    if hasattr(args, "save_prompts") and args.save_prompts:
        kwargs["save_prompts"] = True

    return Settings(**kwargs)


def _add_common_args(parser):
    """Add arguments shared between diagram and plot subcommands."""
    parser.add_argument("--output-dir", default=None,
                        help="Directory to copy the final image to")
    parser.add_argument("--filename", default=None,
                        help="Output filename (e.g. fig1_model.png)")
    parser.add_argument("--iterations", type=int, default=3,
                        help="Refinement iterations (default: 3)")
    parser.add_argument("--aspect-ratio", default=None,
                        help="Aspect ratio: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9")
    parser.add_argument("--optimize", action="store_true",
                        help="Enrich context and sharpen caption before generation")
    parser.add_argument("--auto-refine", action="store_true",
                        help="Let critic loop until satisfied (max 30 iterations)")
    parser.add_argument("--save-prompts", action="store_true", default=True,
                        help="Save formatted agent prompts in run artifacts (default: True)")


def _copy_result(result, args) -> str:
    """Copy result image to output directory, return final path."""
    final_path = str(result.image_path)
    if args.output_dir:
        out_dir = Path(args.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        if args.filename:
            dest = out_dir / args.filename
        else:
            dest = out_dir / Path(result.image_path).name
        shutil.copy2(str(result.image_path), str(dest))
        final_path = str(dest)
    return final_path


async def _generate_diagram(args):
    from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType

    settings = _build_settings(args)
    pipeline = PaperBananaPipeline(settings=settings)

    gen_input = GenerationInput(
        source_context=args.source_context,
        communicative_intent=args.caption,
        diagram_type=DiagramType.METHODOLOGY,
        aspect_ratio=getattr(args, "aspect_ratio", None),
    )

    result = await pipeline.generate(gen_input)
    final_path = _copy_result(result, args)

    _json_ok(
        image_path=final_path,
        iterations=len(result.iterations),
        metadata=result.metadata,
    )


async def _generate_plot(args):
    from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType

    raw_data = json.loads(args.data)

    settings = _build_settings(args)
    pipeline = PaperBananaPipeline(settings=settings)

    gen_input = GenerationInput(
        source_context=f"Data for plotting:\n{args.data}",
        communicative_intent=args.caption,
        diagram_type=DiagramType.STATISTICAL_PLOT,
        raw_data=raw_data,
        aspect_ratio=getattr(args, "aspect_ratio", None),
    )

    result = await pipeline.generate(gen_input)
    final_path = _copy_result(result, args)

    _json_ok(
        image_path=final_path,
        iterations=len(result.iterations),
        metadata=result.metadata,
    )


async def _evaluate(args):
    from paperbanana.core.config import Settings
    from paperbanana.core.utils import find_prompt_dir
    from paperbanana.evaluation.judge import VLMJudge
    from paperbanana.providers.registry import ProviderRegistry

    settings = Settings()
    vlm = ProviderRegistry.create_vlm(settings)
    judge = VLMJudge(vlm_provider=vlm, prompt_dir=find_prompt_dir())

    scores = await judge.evaluate(
        image_path=args.generated,
        source_context=args.context,
        caption=args.caption,
        reference_path=args.reference,
    )

    print(json.dumps({
        "status": "ok",
        "faithfulness": {"winner": scores.faithfulness.winner, "reasoning": scores.faithfulness.reasoning},
        "conciseness": {"winner": scores.conciseness.winner, "reasoning": scores.conciseness.reasoning},
        "readability": {"winner": scores.readability.winner, "reasoning": scores.readability.reasoning},
        "aesthetics": {"winner": scores.aesthetics.winner, "reasoning": scores.aesthetics.reasoning},
        "overall_winner": scores.overall_winner,
        "overall_score": scores.overall_score,
    }))
    sys.exit(0)


async def _download_references(args):
    from paperbanana.data.manager import DatasetManager

    dm = DatasetManager()

    if dm.is_downloaded() and not args.force:
        info = dm.get_info() or {}
        print(json.dumps({
            "status": "ok",
            "message": "Reference set already cached",
            "location": str(dm.reference_dir),
            "examples": dm.get_example_count(),
            "version": info.get("version", "unknown"),
        }))
        sys.exit(0)

    count = dm.download(force=args.force)
    print(json.dumps({
        "status": "ok",
        "message": f"Downloaded {count} reference examples",
        "location": str(dm.reference_dir),
        "examples": count,
    }))
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Direct PaperBanana API wrapper (bypasses MCP transport)",
        epilog="Supports Gemini, OpenAI, Anthropic Claude, OpenRouter, and AWS Bedrock providers.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- diagram ---
    p_diag = sub.add_parser("diagram", help="Generate a methodology diagram")
    p_diag.add_argument("--source-context", required=True,
                        help="Methodology text or paper excerpt")
    p_diag.add_argument("--caption", required=True,
                        help="Figure caption / communicative intent")
    _add_common_args(p_diag)

    # --- plot ---
    p_plot = sub.add_parser("plot", help="Generate a statistical plot")
    p_plot.add_argument("--data", required=True,
                        help="JSON string with plot data")
    p_plot.add_argument("--caption", required=True,
                        help="Plot intent / description")
    _add_common_args(p_plot)

    # --- evaluate ---
    p_eval = sub.add_parser("evaluate", help="Evaluate a diagram against a reference")
    p_eval.add_argument("--generated", required=True,
                        help="Path to generated image")
    p_eval.add_argument("--reference", required=True,
                        help="Path to reference image")
    p_eval.add_argument("--context", required=True,
                        help="Original methodology text")
    p_eval.add_argument("--caption", required=True,
                        help="Figure caption")

    # --- download-references ---
    p_dl = sub.add_parser("download-references",
                          help="Download expanded reference set (~294 examples from PaperBananaBench)")
    p_dl.add_argument("--force", action="store_true",
                      help="Re-download even if already cached")

    args = parser.parse_args()

    _load_env()

    # Check for at least one API key (except for download-references which doesn't need one)
    if args.command != "download-references":
        has_key = any(os.environ.get(k) for k in [
            "GOOGLE_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY",
            "ANTHROPIC_API_KEY", "AWS_PROFILE",
        ])
        if not has_key:
            _json_error(
                "No API key found. Set GOOGLE_API_KEY in ~/.paperbanana.env or .env, "
                "or set OPENAI_API_KEY, ANTHROPIC_API_KEY, or OPENROUTER_API_KEY."
            )

    try:
        if args.command == "diagram":
            asyncio.run(_generate_diagram(args))
        elif args.command == "plot":
            asyncio.run(_generate_plot(args))
        elif args.command == "evaluate":
            asyncio.run(_evaluate(args))
        elif args.command == "download-references":
            asyncio.run(_download_references(args))
    except Exception as e:
        _json_error(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
