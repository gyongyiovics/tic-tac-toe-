# board related functions

def init_board():
    board = [[0 for x in range(3)] for y in range(3)]
    return board

def make_board_visible(board):
    vis_board = []

    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                vis_board.append("X")
            elif board[x][y] == 2:
                vis_board.append("0")
            else:
                vis_board.append(".")    

    return vis_board


def print_board(board):
    visible_board = make_board_visible(board)

    print("""
   1   2   3
A  {} | {} | {}
  ---+---+---
B  {} | {} | {}
  ---+---+---
C  {} | {} | {}
""".format(visible_board[0], visible_board[1], visible_board[2], visible_board[3], 
    visible_board[4], visible_board[5], visible_board[6], 
    visible_board[7], visible_board[8]))