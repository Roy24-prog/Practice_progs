from board_states import *
from board_render import *


def next_board_state(board_state):
    next_state = []
    for yCoord in range(len(board_state)):
        next_state.append([])
        for xCoord in range(len(board_state[yCoord])):
         # Checking in the row above
            aliveNeighbours = 0
            if yCoord != 0 and xCoord != 0:
                aliveNeighbours += board_state[yCoord - 1][xCoord - 1]
            if yCoord != 0:
                aliveNeighbours += board_state[yCoord - 1][xCoord]
            if yCoord != 0 and xCoord != (len(board_state[yCoord]) - 1):
                aliveNeighbours += board_state[yCoord - 1][xCoord + 1]
        # Checking in the cell row 
            if xCoord != 0:
                aliveNeighbours += board_state[yCoord][xCoord - 1]                 
            if xCoord != (len(board_state[yCoord]) - 1): 
                aliveNeighbours += board_state[yCoord][xCoord + 1]
        # Checking in the row below 
            if yCoord != (len(board_state) - 1) and xCoord != 0:
                aliveNeighbours += board_state[yCoord + 1][xCoord - 1]
            if yCoord != (len(board_state) - 1):
                aliveNeighbours += board_state[yCoord + 1][xCoord]
            if yCoord != (len(board_state) - 1) and xCoord != (len(board_state[yCoord]) - 1):
                aliveNeighbours += board_state[yCoord + 1][xCoord + 1]
        # rules based on cell state and number of alive neighbours
            if aliveNeighbours < 2 or aliveNeighbours > 3:
             next_state[yCoord].append(0)
            elif aliveNeighbours == 2:
                next_state[yCoord].append(board_state[yCoord][xCoord])
            elif aliveNeighbours == 3:
                next_state[yCoord].append(1)
    return next_state


init = [[1,0,0],
        [1,1,1],
        [1,1,0]]

render(init)
render(next_board_state(init))