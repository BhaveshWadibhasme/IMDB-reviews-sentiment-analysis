"""Compatibility entry point for ``python IMDB_data_model_standard.py``."""

import runpy
from pathlib import Path

runpy.run_path(
    str(Path(__file__).resolve().parent / "scripts" / "IMDB_data_model_standard.py"),
    run_name="__main__",
)
