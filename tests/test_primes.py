import pytest

from imdb_sentiment.primes import calculator


def test_demo_value_nine(capsys):
    calculator(9).prime()
    assert capsys.readouterr().out == "not prime\n"


@pytest.mark.parametrize("value", [2, 3, 5])
def test_values_the_original_loop_calls_prime(value, capsys):
    calculator(value).prime()
    assert capsys.readouterr().out == "prime\n"


@pytest.mark.parametrize("value", [4, 9, 15])
def test_composites(value, capsys):
    calculator(value).prime()
    assert capsys.readouterr().out == "not prime\n"


def test_values_below_three_take_the_empty_range_path(capsys):
    calculator(1).prime()
    assert capsys.readouterr().out == "prime\n"
    calculator(0).prime()
    assert capsys.readouterr().out == "prime\n"
