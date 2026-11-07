def rating_for_class_probability(probability):
    """Map a class-1 probability to the sentence printed by ``valid_sent.py``.

    The uploaded script multiplied the probability by 10 and compared that
    score with the cutoffs below. Scores from 5.0 up to but not including 5.2
    print ``Coin_toss..........``.
    """
    score = probability * 10
    if score > 7.6:
        return "Rating for this example is: Best"
    elif score <= 7.6 and score > 6.5:
        return "Rating for this example is: Better"
    elif score <= 6.5 and score >= 5.2:
        return "Rating for this example is: Good"
    elif score < 5.0 and score > 4.5:
        return "Rating for this example is: Negative"
    elif score <= 4.5 and score > 3.5:
        return "Rating for this example is: Bad"
    elif score <= 3.5:
        return "Rating for this example is: worst"
    else:
        return "Coin_toss.........."
