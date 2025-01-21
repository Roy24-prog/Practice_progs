from board_states import *

def render(board_state):
    rendered_board = "-" * (len(board_state[1]) + 2)
    for row in range(len(board_state)):
        rendered_board += "\n|"
        for column in board_state[row]:
            if column == 1:
                rendered_board += "*"
            else: rendered_board += " "
        rendered_board += "|"
    rendered_board += "\n" + "-" * (len(board_state[1]) + 2)
    print (rendered_board)

