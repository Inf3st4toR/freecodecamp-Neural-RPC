import tensorflow as tf
from tendorflow import keras

my_model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(3,)),
    keras.layers.Dense(3, activation='softmax')
])
my_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

def model(data0, data1):
    X = [data[i]]
    y = [data[i+1] for i in range(range)]

    my_model.fit(X, y, epochs=5)
    return prediction

def beat(guess):
    match guess:
        case 0:
            return "P"
        case 1:
            return "C"
        case 2:
            return "R"

def player(prev_play, opponent_history=[], my_history=[]):
    # First 3 plays
    if len(opponent_history) < 3:
        my_history.append(len(opponent_history))
        if prev_play:
            opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
        return ("R" if len(opponent_history) == 0 else "P" if len(opponent_history) == 1 else "S")
    
    # Start cheating
    opponent_history.append(0 if prev_play == "R" else 1 if prev_play == "P" else 2)
    prediction = model(opponent_history, my_history)
    my_move = beat(prediction)
    my_history.append(0 if my_move == "R" else 1 if my_move == "P" else 2)
    return my_move

# rock 0, paper 1, cissors 2