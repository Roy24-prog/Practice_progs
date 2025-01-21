from random import randint

########################### Build a data structure of random 1 & 0

def dead_state(w, h):
    board_state = []
    for row in range((h)):
        board_state.append([])
        for column in range((w)):
            board_state[row].append(0)
    return board_state

def random_state(w, h):
    board_state = dead_state(w, h)
    for row in range((h)):
        for column in range((w)):
            board_state[row][column] = randint(0,1)
    return board_state
