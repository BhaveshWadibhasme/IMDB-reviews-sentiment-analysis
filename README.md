# Sentiment analysis on IMDB dataset using Deep Learning algorithm in python

Scripts for an IMDB-review sentiment example: pad the Keras IMDB sequences, score a saved model on a 5,000-review validation file, and score eleven hand-written sentences. A separate `calculator` class prints whether an integer is prime.

## Layout

- `scripts/` holds the runnable scripts.
- `imdb_sentiment/` holds the pure helpers those scripts can share: `calculator` and the sentence-rating thresholds.
- The original filenames at the repository root (`IMDB_data_model_standard.py`, `valid_sent.py`, `validation_script.py`, `prime_number_class_objects.py`) forward to `scripts/`, so the old commands still work.
- `validation_dataset.csv` and `valid_data_sent.csv` stay at the repository root.

Run the scripts with the repository root as the working directory. They open these relative paths:

- `validation_dataset.csv`
- `valid_data_sent.csv`
- `model.json`
- `model.h5`

## Setup

The checked commands use Python 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

`requirements.txt` pins NumPy, pandas, and scikit-learn for CSV loading, label encoding, and the accuracy report. `requirements-dev.txt` adds pytest and Ruff.

## Commands

```bash
python prime_number_class_objects.py
python IMDB_data_model_standard.py
python valid_sent.py
python validation_script.py
```

The same four files can be started from `scripts/`. `python prime_number_class_objects.py` prints `not prime` for the built-in example value `9`. Importing `prime_number_class_objects` exposes `calculator` and does not print.

## Data

| File | Bytes | Rows | Columns |
| --- | ---: | ---: | --- |
| `validation_dataset.csv` | 6,704,589 | 5,000 | unnamed index, `text`, `label` (`pos` 2,515, `neg` 2,485) |
| `valid_data_sent.csv` | 557 | 11 | `Text`, `classess` (six `1`s and five `0`s) |

`classess` is the column name stored in the sentence file. `sklearn.preprocessing.LabelEncoder` sorts the validation labels, so `neg` is 0 and `pos` is 1. The manual check at the bottom of `validation_script.py` uses that encoding.

Both CSVs remain in git. Their SHA-256 values are locked in `tests/test_datasets.py`.

### Model files the scoring scripts expect

`valid_sent.py` and `validation_script.py` load `model.json` and `model.h5` from the working directory. Those files are absent from the repository, so both commands raise `FileNotFoundError` before they can print a score.

### Keras imports

The deep-learning scripts use the Keras 2 import layout:

- `keras.datasets.imdb`
- `keras.preprocessing.sequence`
- `keras.preprocessing.text.one_hot`
- `keras.models.model_from_json`
- `keras.utils.np_utils.to_categorical`

`IMDB_data_model_standard.py` calls `imdb.load_data`, which downloads the packaged IMDB word index. The uploaded file never called `model.fit`. The training recipe remains comments: an embedding of the top 5,000 words into 32 dimensions, a flatten, a 250-unit ReLU layer, a sigmoid output, binary cross-entropy, Adam, two epochs, and batch size 128.

TensorFlow and Keras are not pinned. Keras 3 removed `keras.preprocessing` and `keras.utils.np_utils`, and the weight file the scoring scripts open was never committed. Installing current Keras would not let those entry points finish.

## Checks

```bash
ruff check .
ruff format --check .
pytest
```

GitHub Actions runs those commands on Python 3.12 for pull requests and for pushes to `master`.

## Behavior notes

- Print statements are Python 3 function calls. Under Python 3 the printed text matches the original print statements.
- `validation_script.py` on `master` does not parse. The restored script reads `validation_dataset.csv`, encodes `label`, one-hot encodes `text` with vocabulary 20,000, pads to length 400, loads `model.json` and `model.h5`, and prints accuracy plus a classification report. It then encodes the original manual sentence and prints the predicted class. The spliced model-export fragment is gone because it referenced names this file never defined.
- The manual check still evaluates `if predictions == 0` on the NumPy array returned by `argmax`. NumPy raises `ValueError` for the truth value of that array, so a run that finds the model files still stops there.
- Rating thresholds live in `imdb_sentiment.ratings.rating_for_class_probability`, and `valid_sent.py` prints those sentences. A class-1 probability times 10 maps above 7.6 to Best, through 6.5 to Better, through 5.2 to Good, below 5.0 and above 4.5 to Negative, through 3.5 to Bad, and at or below 3.5 to `worst`. Scores from 5.0 up to but not including 5.2 print `Coin_toss..........`.
- `valid_sent.py` still prints the CSV head and the frame type before it imports Keras.
- `calculator.prime` still uses `range(2, n - 1)`. Values below 3 take the empty-loop path and print `prime`. Commented-out addition and subtraction methods were removed.
- The IMDB padding script still prints `X_test.shape` on the line labeled `y_train`.
- `scripts/prime_number_class_objects.py` and `scripts/valid_sent.py` insert the repository root on `sys.path` so they can import `imdb_sentiment` when started by file path.

## Migration candidates

These stay where they are in this pass. No external storage URL is assigned.

- `validation_dataset.csv` (6,704,589 bytes, 5,000 reviews) is the only sizeable data file. It fits in git. A later pass can move it to Git LFS or other storage if model weights or larger dumps are added.
- `valid_data_sent.csv` (557 bytes, 11 rows) stays in the repository.
- `model.h5`, once the missing weights exist, is the binary file that would belong in that later decision. It is not gitignored, because the scoring scripts treat it as an input. `model.json` is the matching architecture file and is also absent.
