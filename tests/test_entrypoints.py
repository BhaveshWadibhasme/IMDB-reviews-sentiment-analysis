import importlib
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ENTRY_POINTS = [
    "prime_number_class_objects.py",
    "IMDB_data_model_standard.py",
    "valid_sent.py",
    "validation_script.py",
]


def test_python_files_compile():
    paths = list((ROOT / "imdb_sentiment").glob("*.py"))
    paths += list((ROOT / "scripts").glob("*.py"))
    paths += list((ROOT / "tests").glob("*.py"))
    paths += [ROOT / name for name in ENTRY_POINTS]
    assert paths
    for path in paths:
        py_compile.compile(str(path), doraise=True)


def test_root_entry_points_forward_to_scripts():
    for name in ENTRY_POINTS:
        source = (ROOT / name).read_text()
        assert "scripts" in source
        assert name in source
        assert (ROOT / "scripts" / name).is_file()


def test_prime_entry_points_print_the_demo_result():
    for script in (
        ROOT / "prime_number_class_objects.py",
        ROOT / "scripts" / "prime_number_class_objects.py",
    ):
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        assert completed.stdout == "not prime\n"


def test_importing_prime_entry_point_exports_calculator_without_printing(capsys):
    sys.modules.pop("prime_number_class_objects", None)
    module = importlib.import_module("prime_number_class_objects")
    assert capsys.readouterr().out == ""
    module.calculator(9).prime()
    assert capsys.readouterr().out == "not prime\n"
