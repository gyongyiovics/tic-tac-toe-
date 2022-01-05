import os
from time import sleep
import board
import player

#tic-tac-toe game in python language 
# move, menu and game related functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def game(mode='HUMAN-HUMAN'):
    if mode == 'HUMAN-HUMAN':
        p1 = True
        p2 = True
    if mode == 'HUMAN-AI':
        p1 = True
        p2 = False
    elif mode == 'AI-HUMAN':
        p1 = False
        p2 = True
    elif mode == 'AI-AI':
        p1 = False
        p2 = False
    clear()
    board_display = board.init_board()
    while True:
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        board.print_board(board_display)
        # row, col = get_move(board, 1)
        if p1:
            player.mark(board_display, 1, *player.get_move(board_display, 1))
        else:
            player.mark(board_display, 1, *player.get_ai_move(board_display, 1))
            sleep(1)
        if has_won(board_display, 1):
            winner = 1
            break
        elif is_full(board_display):
            winner = 0
            break
        clear()

        board.print_board(board_display)
        # row, col = get_move(board, 2)
        if p2:
            player.mark(board_display, 2, *player.get_move(board_display, 2))
        else:
            player.mark(board_display, 2, *player.get_ai_move(board_display, 2))
            sleep(1)
        if has_won(board_display, 2):
            winner = 2
            break
        elif is_full(board_display):
            winner = 0
            break
        clear()
    clear()
    board.print_board(board_display)
    print_result(winner)



def main_menu():
    gamemode = input("Choose Gamemode:\n1. PLAYER VS PLAYER        2. HUMAN VS AI\n")
    if int(gamemode) == 1:
        game('HUMAN-HUMAN')
    elif int(gamemode) == 2:
        gamemode = input(
            "Do you want to go first, or let the AI do? (1 to go first, 2 to go second):\n")
        if int(gamemode) == 1:
            game("HUMAN-AI")
        elif int(gamemode) == 2:
            game("AI-HUMAN")




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
    main_menu()