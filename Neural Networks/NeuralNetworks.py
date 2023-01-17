import sys
import numpy as np
from tensorflow import keras
import tensorflow as tf
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.models import Sequential
from keras.callbacks import LambdaCallback
from keras.models import load_model
import random

f = open("Data/Base.csv", "r")
fi = f.read()

chars = sorted(list(set(fi)))

charIndices = dict((c, i) for i, c in enumerate(chars))
indicesChar = dict((i, c) for i, c in enumerate(chars))


maxLen = 20
step = 3

sentences = []
nextChars = []

for i in range(0, len(fi) - maxLen, step):
    sentences.append(fi[i: i + maxLen])
    nextChars.append(fi[i + maxLen])

x = np.zeros((len(sentences), maxLen, len(chars)), dtype=bool)
y = np.zeros((len(sentences), len(chars)), dtype=bool)

for i, sentance in enumerate(sentences):
    for t, char in enumerate(sentance):
        x[i, t, charIndices[char]] = 1
    y[i, charIndices[nextChars[i]]] = 1

model = Sequential()
model.add(LSTM(256, input_shape=(maxLen, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation("softmax"))
optimizer = RMSprop(learning_rate=0.01)
model.compile(loss="categorical_crossentropy", optimizer=optimizer)
try:
    model = load_model("Data/Weights.hdf5")
except:
    pass

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def on_epoch_end(epoch, logs):
    # Function invoked at end of each epoch. Prints generated text.
    z = 0
    print()
    print('----- Generating text after Epoch: %d' % epoch)

    start_index = random.randint(0, len(fi) - maxLen - 1)
    for diversity in [0.2, 0.5, 1.0, 1.2]:
        print('----- diversity:', diversity)
        z += 1
        generated = ''
        sentence =  str(fi[start_index: start_index + maxLen])
        generated += sentence
        print('----- Generating with seed: "' + sentence + '"')
        sys.stdout.write(generated)

        for i in range(12):
            x_pred = np.zeros((1, maxLen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, charIndices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indicesChar[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
print_callback = LambdaCallback(on_epoch_end=on_epoch_end)



from keras.callbacks import ModelCheckpoint

filepath = "weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss',
                             verbose=1, save_best_only=True,
                             mode='min')


from keras.callbacks import ReduceLROnPlateau
reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2,
                              patience=1, min_lr=0.001)

callbacks = [print_callback,checkpoint, reduce_lr]




# model.fit(x, y, batch_size=8192, epochs=10, callbacks=callbacks)



def generate_text(length, diversity):
    # Get random starting text
    start_index = random.randint(0, len(fi) - maxLen - 1)
    generated = ''
    sentence = fi[start_index: start_index + maxLen]
    generated += sentence
    for i in range(length):
            x_pred = np.zeros((1, maxLen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, charIndices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indicesChar[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char
    return generated


print(generate_text(12, 0.2))