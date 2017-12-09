#!/usr/bin/env python

import numpy
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from random import randint

filename = "../data/all_doc.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

words = raw_text.split()
words_to_int = dict((c, i) for i, c in enumerate(words))

chars = sorted(list(set(words)))
char_to_int = dict((c, i) for i, c in enumerate(words))

n_chars = len(words)
n_vocab = len(chars)

seq_length = 5
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = words[i:i + seq_length]
    seq_out = words[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

n_patterns = len(dataX)
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(n_vocab)
y = np_utils.to_categorical(dataY)

model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='Nadam')

filepath = "../data/best_weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs=5000, batch_size=64, callbacks=callbacks_list)
