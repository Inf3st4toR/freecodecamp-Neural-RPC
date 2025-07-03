import tensorflow as tf
from tensorflow import keras
import numpy as np

my_model = keras.Sequential([
    keras.layers.Flatten(input_shape=(5, 2)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(3, activation='softmax')
])
my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def train(data0, data1):
    X = np.array([[ [data0[i + j], data1[i + j]] for j in range(5) ] for i in range(len(data0) - 5)])
    y = np.array([data0[i + 5] for i in range(len(data0) - 5)])
    my_model.fit(X, y, epochs=1)

def predict(data):
    return np.argmax(my_model.predict(data), axis=1)[0]

def beat(guess):
    match guess:
        case 0:
            return "P"
        case 1:
            return "C"
        case 2:
            return "R"

def player(prev_play, opponent_history=[], my_history=[]):
    # First 10 plays
    if len(my_history) < 10:
        play = len(my_history) % 3
        if prev_play:
            opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
        my_history.append(play)
        return ("R" if play == 0 else "P" if play == 1 else "S")
    
    # Train model
    if len(my_history) % 10 == 0:
        train(opponent_history[-10:], my_history[-10:])
    

    # Start cheating
    opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
    my_move = beat(predict(np.array([[ [opponent_history[i], my_history[i]] for i in range(-5, 0) ]])))
    my_history.append(0 if my_move == "R" else 1 if my_move == "P" else 2)
    return my_move

# rock 0, paper 1, cissors 2