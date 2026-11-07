"""Score the eleven sentences in valid_data_sent.csv.

Run this with the repository root as the working directory. ``model.json`` and
``model.h5`` are required and are not in the repository.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from imdb_sentiment.ratings import rating_for_class_probability

dataset = pd.read_csv("valid_data_sent.csv")
text_data = dataset["Text"].tolist()
classes = dataset["classess"].tolist()
print(dataset.head())
print(type(dataset))

from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import one_hot
from sklearn.metrics import accuracy_score, classification_report

vocab_size = 20000
encoded_docs1 = [one_hot(d, vocab_size) for d in text_data]

max_length = 400
padded_docs1 = pad_sequences(encoded_docs1, maxlen=max_length, padding="post")

with open("model.json") as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

submit = loaded_model.predict(padded_docs1)
print("The probabilities are:\n", submit)

predictions = submit.argmax(axis=-1)

print("\n")
print("class_1_probability:\n", submit[:, 1])

print("\n")
for probability in submit[:, 1]:
    print(rating_for_class_probability(probability))

print("\n")
print("Move_to_precision_and_recall.........................")
print("The accuracy_score is:", accuracy_score(classes, predictions) * 100)
print(classification_report(classes, predictions))

print("The actual_class labels are:", classes)
print("The predicted_class labels are:", predictions)
