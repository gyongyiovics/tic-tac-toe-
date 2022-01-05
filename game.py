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

if __name__ == '__main__':
    #clear()
    #main_menu()