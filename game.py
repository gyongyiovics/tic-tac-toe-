import os
from time import sleep
from random import randint

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