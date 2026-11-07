"""Score validation_dataset.csv with a saved Keras model.

The uploaded file did not parse. A model-export fragment was spliced into the
LabelEncoder import and mentioned ``model`` and ``X_train``, which this file
never defined. What follows is the validation run and the manual sentence
check that were below that splice.

Run this with the repository root as the working directory. ``model.json`` and
``model.h5`` are required and are not in the repository.
"""

import pandas as pd
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import one_hot
from keras.utils.np_utils import to_categorical
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

dataset = pd.read_csv("validation_dataset.csv")
text_data = dataset["text"].tolist()
label = dataset["label"].tolist()

encoder = LabelEncoder()
encoder.fit(label)
y_test = encoder.fit_transform(label)
temp = y_test
to_categorical(y_test)

vocab_size = 20000
encoded_docs1 = [one_hot(d, vocab_size) for d in text_data]

max_length = 400
padded_docs1 = pad_sequences(encoded_docs1, maxlen=max_length, padding="post")

with open("model.json") as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

submit = loaded_model.predict(padded_docs1)
predictions = submit.argmax(axis=-1)

print("The accuracy_score is:", accuracy_score(temp, predictions) * 100)
print(classification_report(temp, predictions))

text1 = """ An extremely dark and brooding show with an excellent cast. One of the few shows that I try to watch on a regular basis. Glad to see Bebe Neuwirth in a recurring role, but feel Andre Braugher is underutilized. He is one intense actor! Hope CBS gives it a better time slot next season."""

text_set = []
text_set.append(text1)
vocab_size = 20000
encoded_docs1 = [one_hot(d, vocab_size) for d in text_set]

max_length = 400
padded_docs1 = pad_sequences(encoded_docs1, maxlen=max_length, padding="post")

submit = loaded_model.predict(padded_docs1)
predictions = submit.argmax(axis=-1)

print("True class label is: Pos")
print("\n")
print(text1)

if predictions == 0:
    print("The predicted_class label is:Neg")
else:
    print("The predicted_class label is:Pos")
