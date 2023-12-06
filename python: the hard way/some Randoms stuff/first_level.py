from my_game import *
from game_2 import *

def castle():
    print("""
    Hello welcome to the game ...
    infront of you there is a horror castle ..
    There is a queen inside the castle ...
    The Villian kidnapped the queen ..
    if you want to save the queen go inside the castle and kill the villian..
    The queen is in middle floor ...
    infront of you there are two door ...
    if you choose door A then you go to ground floor ...
    if you choose door B then you fo to top floor ....
    press 1 for door A ...
    press 2 for door B ...
    press 3 for exit the game ...
    """)

    choice = input("> ")

    if choice =="1":
        print("you are goint to be door A:")
        doorA()

    elif choice == "2":
        print("you are going to be door B")
        doorB()

    elif choice == "3":
        exit(0)

    else:
        print("you didn't enter any option. please try one more time ...")
        castle()

castle()
