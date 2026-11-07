"""Compatibility entry point for ``python validation_script.py``."""

import runpy
from pathlib import Path

runpy.run_path(
    str(Path(__file__).resolve().parent / "scripts" / "validation_script.py"),
    run_name="__main__",
)
