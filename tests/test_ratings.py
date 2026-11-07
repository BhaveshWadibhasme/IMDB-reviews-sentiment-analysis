import pytest

from imdb_sentiment.ratings import rating_for_class_probability


@pytest.mark.parametrize(
    ("probability", "sentence"),
    [
        (0.77, "Rating for this example is: Best"),
        (0.76, "Rating for this example is: Better"),
        (0.66, "Rating for this example is: Better"),
        (0.65, "Rating for this example is: Good"),
        (0.52, "Rating for this example is: Good"),
        (0.51, "Coin_toss.........."),
        (0.50, "Coin_toss.........."),
        (0.49, "Rating for this example is: Negative"),
        (0.46, "Rating for this example is: Negative"),
        (0.45, "Rating for this example is: Bad"),
        (0.36, "Rating for this example is: Bad"),
        (0.35, "Rating for this example is: worst"),
        (0.0, "Rating for this example is: worst"),
    ],
)
def test_rating_thresholds(probability, sentence):
    assert rating_for_class_probability(probability) == sentence
