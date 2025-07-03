import tensorflow as tf
from tensorflow import keras
import numpy as np
import random

my_model = keras.Sequential([
    keras.layers.Flatten(input_shape=(10, 2)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])
my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def train(data0, data1):
    X = np.array([[ [data0[i + j], data1[i + j]] for j in range(10) ] for i in range(len(data0) - 10)])
    y = np.array([data0[i + 10] for i in range(len(data0) - 10)])
    my_model.fit(X, y, epochs=5, verbose=0)

def predict(data):
    return np.argmax(my_model.predict(data, verbose=0), axis=1)[0]

def beat(guess):
    match guess:
        case 0:
            return "P"
        case 1:
            return "S"
        case 2:
            return "R"

def player(prev_play, opponent_history=[], my_history=[]):
    # First 10 plays
    if len(my_history) < 20:
        play = random.choice([0, 1, 2])
        if prev_play:
            opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
        my_history.append(play)
        return ("R" if play == 0 else "P" if play == 1 else "S")
    
    # Train model
    if len(my_history) == 20:
        train(opponent_history, my_history)

    # Train model
    if len(my_history) == 100:
        train(opponent_history, my_history)
    
        # Train model
    if len(my_history) == 200:
        train(opponent_history, my_history)

    # Start cheating
    opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
    my_move = predict(np.array([[ [opponent_history[i], my_history[i]] for i in range(-10, 0) ]]))
    my_history.append(my_move)
    return beat(my_move)

# rock 0, paper 1, cissors 2