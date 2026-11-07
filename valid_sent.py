"""Compatibility entry point for ``python valid_sent.py``."""

import runpy
from pathlib import Path

runpy.run_path(
    str(Path(__file__).resolve().parent / "scripts" / "valid_sent.py"),
    run_name="__main__",
)
