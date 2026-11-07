"""Run the original prime example (the value 9)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from imdb_sentiment.primes import calculator

if __name__ == "__main__":
    c = calculator(9)
    c.prime()
