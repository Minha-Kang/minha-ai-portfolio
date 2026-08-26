# -*- coding: utf-8 -*-
"""Run CLEAN_HOTEL 1,000 through Agent 1-4 and then Agent 5/6 + RAG judge."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--agent14-only", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument(
        "--agent14-output",
        type=Path,
        default=base / "outputs_full1000_agent1_4",
    )
    parser.add_argument(
        "--final-output",
        type=Path,
        default=base / "outputs_full1000_agent5_6_rag",
    )
    parser.add_argument(
        "--literature-dir",
        type=Path,
        default=base / "literature",
    )
    args = parser.parse_args()

    legacy_runner = (
        base / "legacy_agent1_4_v8_2" / "run_architecture_compare_v8.py"
    )
    clean_input = base / "input" / "clean_hotel_1000_input.xlsx"
    agent14_cmd = [
        sys.executable,
        str(legacy_runner),
        "--input",
        str(clean_input),
        "--sheet_name",
        "CLEAN_HOTEL_1000",
        "--output_dir",
        str(args.agent14_output),
        "--architectures",
        "orchestrator_dynamic",
        "--save_every",
        "10",
    ]
    if args.limit:
        agent14_cmd.extend(["--limit", str(args.limit)])
    if args.resume:
        agent14_cmd.append("--resume")
    subprocess.run(agent14_cmd, check=True, cwd=legacy_runner.parent)

    if args.agent14_only:
        return
    predictions_dir = args.agent14_output / "orchestrator_dynamic"
    final_cmd = [
        sys.executable,
        str(base / "hotel_agent56_pipeline.py"),
        "--mode",
        "full1000",
        "--predictions-dir",
        str(predictions_dir),
        "--output-dir",
        str(args.final_output),
        "--state-dir",
        str(base / "state_full1000"),
        "--literature-dir",
        str(args.literature_dir),
    ]
    subprocess.run(final_cmd, check=True, cwd=base)


if __name__ == "__main__":
    main()


