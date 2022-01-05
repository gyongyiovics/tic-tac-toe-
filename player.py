import game
from random import randint

# player related functions

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    while True:
        user_input = input(
            "Player {}'s turn. What's your move?(Example: A1):\n".format(player))
        if len(user_input) == 2:
            if int(user_input[1]) < 4 and int(user_input[1]) > 0:
                if user_input[0] == 'A' or user_input[0] == 'a':
                    row = 0
                    col = int(user_input[1])-1
                    if board[row][col] == 0:
                        return (row, col)
                elif user_input[0] == 'B' or user_input[0] == 'b':
                    row = 1
                    col = int(user_input[1])-1
                    if board[row][col] == 0:
                        return (row, col)
                elif user_input[0] == 'C' or user_input[0] == 'c':
                    row = 2
                    col = int(user_input[1])-1
                    if board[row][col] == 0:
                        return (row, col)
        elif user_input == "quit":
            game.quit_game()
        elif user_input == "clear":
            game.clear()
        print("Invalid move.")


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    if game.is_full(board):
        return None
    # winning move if possible
    for x in range(len(board)):
        pf = 0
        ef = 0
        pv = 0
        ev = 0
        env = 0
        enf = 0
        for y in range(len(board[x])):
            if board[x][y] == player:
                pv += 1
            elif board[x][y] == 0:
                ev += 1
                if ev == 1:
                    rowv, colv = x, y
            else:
                env += 1
            if board[y][x] == player:
                pf += 1
            elif board[y][x] == 0:
                ef += 1
                if ef == 1:
                    rowf, colf = y, x
            else:
                enf += 1
        if pv == 2 and ev == 1 or env == 2 and ev == 1:
            return rowv, colv
        if pf == 2 and ef == 1 or enf == 2 and ef == 1:
            return rowf, colf
    k = 0
    e = 0
    enk = 0
    # cross from top left to bottom right
    for i in range(0, 3):
        if board[i][i] == player:
            k += 1
        elif board[i][i] == 0:
            e += 1
            if e == 1:
                row, col = i, i
        else:
            enk += 1
    if k == 2 and e == 1 or enk == 2 and e == 1:
        return row, col
    # cross from top right to bottom left
    k = 0
    e = 0
    enk = 0
    if board[0][2] == player:
        k += 1
    elif board[0][2] == 0:
        e += 1
        if e == 1:
            row, col = 0, 2
    else:
        enk += 1
    if board[1][1] == player:
        k += 1
    elif board[1][1] == 0:
        e += 1
        if e == 1:
            row, col = 1, 1
    else:
        enk += 1
    if board[2][0] == player:
        k += 1
    elif board[2][0] == 0:
        e += 1
        if e == 1:
            row, col = 2, 0
    else:
        enk += 1
    if k == 2 and e == 1 or enk == 2 and e == 1:
        return row, col
    # corner
    used = []
    while len(used) < 4:
        x = randint(0, 3)
        if x not in used and x == 0:
            if board[0][0] == 0:
                return 0, 0
            used.append(x)
        if x not in used and x == 1:
            if board[0][2] == 0:
                return 0, 2
            used.append(x)
        if x not in used and x == 2:
            if board[2][0] == 0:
                return 2, 0
            used.append(x)
        if x not in used and x == 3:
            if board[2][2] == 0:
                return 2, 2
            used.append(x)
        # sides
        used = []
        while len(used) < 4:
            x = randint(0, 3)
            if x not in used and x == 0:
                if board[0][1] == 0:
                    return 0, 1
                used.append(x)
            if x not in used and x == 1:
                if board[1][0] == 0:
                    return 1, 0
                used.append(x)
            if x not in used and x == 2:
                if board[1][2] == 0:
                    return 1, 2
                used.append(x)
            if x not in used and x == 3:
                if board[2][1] == 0:
                    return 2, 1
                used.append(x)
        return 1, 1


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    try:
        board[row][col] = int(player)
        return board
    except IndexError:
        print("Index is out of range")
        pass

