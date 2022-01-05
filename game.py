import os
from time import sleep

#tic-tac-toe game in python language 
# move, menu and game related functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    gamemode = input('Choose gamemode: ')
    print(gamemode)


def quit_game():
    print("Good bye") 
    sleep(2)
    clear()
    exit()


def is_full(board):
    """Returns True if board is full (any of the board fields is not 0, but "0" or "X")."""
    if any(0 in sublist for sublist in board) is True:
        return False
    return True


def has_won(board, player):
    """Returns True if player has won the game."""
    for x in range(len(board)):
        if board[x][0] == player and board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return True
        elif board[0][x] == player and board[0][x] == board[1][x] and board[1][x] == board[2][x]:
            return True
    if board[0][0] == player and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    elif board[0][2] == player and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False



def print_result(winner):
    if winner == 1:
        print("X won.")
    elif winner == 2:
        print("0 won.")
    else:
        print("It's a tie.")



if __name__ == '__main__':
    clear()
    #main_menu()