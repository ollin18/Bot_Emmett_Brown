#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import tweepy
from credentials import *
from random import randint
import numpy
import sys
import re

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

filename = "../data/all_doc.txt"
raw_text = open(filename,encoding='latin1').read()
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

filename = "../data/best_weights.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

int_to_char = dict((i, c) for i, c in enumerate(words))

start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[start]
no_sym=re.compile(r'[.!]')
for mention in mentions:
    if mention.created_at>datetime.datetime.now()-datetime.timedelta(hours=1):
        frase = []
        count = 0
        while True:
            x = numpy.reshape(pattern, (1,len(pattern),1))
            x = x/float(n_vocab)
            prediction = model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = int_to_char[index]
            seq_in = [int_to_char[value] for value in pattern]
            frase.append(result)
            frase.append(' ')
            pattern.append(index)
            pattern = pattern[1:len(pattern)]
            word = frase[-2]
            count += 1
            if no_sym.search(word[len(word)-1:len(word)]) or count > 40:
                break
        doc_says = ''.join(frase).capitalize()
        if doc_says != None:
            who=mention.user.screen_name
            api.update_status(status="@"+who+" "+doc_says, in_reply_to_status_id=mention.id_str)
