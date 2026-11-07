import hashlib
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder

ROOT = Path(__file__).resolve().parents[1]

DATA_SHA256 = {
    "validation_dataset.csv": (
        "0f9df21c69fbac6ca09f2acf9996950e3250ab76bf53efc0b7ce9ddccf3fbca2"
    ),
    "valid_data_sent.csv": (
        "cb609126c4e8e33f41777b74c5b95f76916ee9c542d41b275677ca17ebe50092"
    ),
}

MANUAL_SENTENCE = (
    " An extremely dark and brooding show with an excellent cast. One of the "
    "few shows that I try to watch on a regular basis. Glad to see Bebe "
    "Neuwirth in a recurring role, but feel Andre Braugher is underutilized. "
    "He is one intense actor! Hope CBS gives it a better time slot next season."
)


def test_dataset_bytes_and_locations_unchanged():
    for name, digest in DATA_SHA256.items():
        path = ROOT / name
        assert path.is_file()
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
        assert not (ROOT / "data" / name).exists()


def test_validation_dataset_contract():
    frame = pd.read_csv(ROOT / "validation_dataset.csv")
    assert list(frame.columns) == ["Unnamed: 0", "text", "label"]
    assert len(frame) == 5000
    assert frame["text"].isna().sum() == 0
    assert frame["label"].value_counts().to_dict() == {"pos": 2515, "neg": 2485}


def test_sentence_dataset_contract():
    frame = pd.read_csv(ROOT / "valid_data_sent.csv")
    assert list(frame.columns) == ["Text", "classess"]
    assert len(frame) == 11
    assert frame["classess"].tolist() == [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


def test_label_encoder_order_matches_the_manual_check():
    labels = pd.read_csv(ROOT / "validation_dataset.csv")["label"].tolist()
    encoder = LabelEncoder()
    encoder.fit(labels)
    assert list(encoder.classes_) == ["neg", "pos"]
    assert int(encoder.transform(["neg"])[0]) == 0
    assert int(encoder.transform(["pos"])[0]) == 1


def test_relative_data_paths_remain_in_the_scripts():
    valid_sent = (ROOT / "scripts" / "valid_sent.py").read_text()
    validation = (ROOT / "scripts" / "validation_script.py").read_text()
    assert 'pd.read_csv("valid_data_sent.csv")' in valid_sent
    assert 'open("model.json")' in valid_sent
    assert 'load_weights("model.h5")' in valid_sent
    assert 'pd.read_csv("validation_dataset.csv")' in validation
    assert 'open("model.json")' in validation
    assert 'load_weights("model.h5")' in validation
    assert MANUAL_SENTENCE in validation
