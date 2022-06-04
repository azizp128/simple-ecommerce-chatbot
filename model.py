from data import intents

# import library
import nltk
#nltk.download("punkt")
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import tensorflow as tf
import numpy as np
import random
import string

def remove_punc(a):
  return a.translate(str.maketrans('', '', string.punctuation))

words = []
classes = []
documents = []

for intent in intents:
  for pattern in intent["patterns"]:
    pattern_2 = remove_punc(pattern)
    w = nltk.word_tokenize(pattern_2)
    words.extend(w)
    
    documents.append((w, intent["tag"]))

    if intent["tag"] not in classes:
      classes.append(intent["tag"])

words = [stemmer.stem(word.lower())  for word in words]
words = list(set(words))
words

y = []
X = []
for doc in documents:
  bag = []
  pattern_words = doc[0]
  pattern_words = [stemmer.stem(word.lower())  for word in pattern_words]
  for w in words:
    bag.append(1 if w in pattern_words else 0)
  y.append(classes.index(doc[1]))
  X.append(bag)

X, y = np.array(X), np.array(y)
from tensorflow.keras.utils import to_categorical
y = to_categorical(y)

# Model ANN
model = tf.keras.Sequential([

        # input layer
        tf.keras.layers.Flatten(input_shape=(X.shape[1], )),

        
        tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        
        tf.keras.layers.Dense(16, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        
        
        tf.keras.layers.Dense(len(classes), activation='softmax')
    ])

optimiser = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=optimiser,
                  loss='categorical_crossentropy',
                  metrics=['categorical_accuracy'])

history = model.fit(X, y, batch_size=8, epochs=1000, verbose = 0)