"""Load and pad the Keras IMDB sequences.

The uploaded script kept the model-fit block inside a discarded string, so
running the file did not train. That recipe stays in comments. ``imdb.load_data``
still downloads the packaged IMDB word index when this file runs.
"""

import numpy
from keras.datasets import imdb
from keras.preprocessing import sequence

seed = 7
numpy.random.seed(seed)

top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)  # noqa: F841

print("Shape of X_train before padding:", X_train.shape)
print("Shape of X_test before padding:", X_test.shape)

max_words = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)

print("Shape of X_train_data after padding:", X_train.shape)
# Uploaded script printed X_test.shape on the line labeled y_train.
print("Shape of y_train data after padding:", X_test.shape)

print(X_train[0:1])

# model = Sequential()
# model.add(Embedding(top_words, 32, input_length=max_words))
# model.add(Flatten())
# model.add(Dense(250, activation="relu"))
# model.add(Dense(1, activation="sigmoid"))
# model.compile(
#     loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"]
# )
# print(model.summary())
# model.fit(
#     X_train,
#     y_train,
#     validation_data=(X_test, y_test),
#     epochs=2,
#     batch_size=128,
#     verbose=2,
# )
# scores = model.evaluate(X_test, y_test, verbose=0)
# print("Accuracy: %.2f%%" % (scores[1] * 100))
