"""Compatibility entry point for ``python prime_number_class_objects.py``."""

import runpy
from pathlib import Path

_TARGET = Path(__file__).resolve().parent / "scripts" / "prime_number_class_objects.py"

if __name__ == "__main__":
    runpy.run_path(str(_TARGET), run_name="__main__")
else:
    _namespace = runpy.run_path(str(_TARGET))
    calculator = _namespace["calculator"]
