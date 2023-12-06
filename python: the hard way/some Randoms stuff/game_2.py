from last_level import *


def doorB():
    print("""
    you're in Top floor .
    in front of you there are three rooms ...
    which room you want to go ....
    room A, room B, and room C ....
    press 1 for room A ...
    press 2 for room B ...
    press 1 for room C ...
    """)

    choice = input("> ")

    if choice == "1":
        roomA()

    elif choice == "2":
        roomB()

    elif choice == "3":
        roomC()

    else:
        print("you don't pick any room please try one more time...")
        doorB()

def roomA():
    print("""
    you're in Room A ....
    in this room there is a door which ask a # QUESTION:  ...
    if you answer is right then the door will open otherwise it will not open ....
    if your answer is wrong you go to backward ....
    what does's Virat Kohli father do ?
    Here There's two option for you ...
    press 1 for advocate...
    press 2 for a employee in company ...
    press 3 for exit
    """)

    choice = input("> ")

    if choice == "1":
        print("you're going to forward the game ...")
        goahead()

    elif choice == "2":
        print("you're going to backward the game...")
        roomA()

    elif choice =="3":
        print("you're going to exit the game...")

    else:
        print("you didn't choose any option. try one more time...")
        roomA()



def goahead():
    print("""
    Here you're going ahead in this room ...
    infront of you There are two door ....
    one door of room B ....
    another door of room c ....
    press 1 for room B ...
    press 2 for room C ...
    """)

    choice = input("> ")

    if choice == "1":
        print("you are going in room B ....")
        roomB()

    elif choice == "2":
        print("you are going in room B ....")
        roomC()

    else:
        print("you didn't pick any option . please try one more time ...")
        goahead()


def roomB():
    print("""
    you are in room B ....
    infront of you there are three door ....
    one door go to the room A ...
    second door go to the room C ...
    third door go to the outside of the castle ...
    But the problem is that you don't know which door goes where ...
    press 1 for first door ....
    press 2 for second door ...
    press 3 for third door ...
    press 4 for exit the game ....
    """)

    choice = input("> ")

    if choice == "1":
        print("you're going to the backward the game...")
        roomB()

    elif choice == "2":
        print("you're going to the room A ...")
        roomA()

    elif choice == "3":
        print("you're going to room C ...")
        roomC()

    elif choice == "4":
        print("you're going to be exit the game ...")
        exit(0)

    else:
        print("you didn't pick any option . please try one more time ...")
        roomB()

def roomC():
    print("""
    you're in room C ....
    infront of you there is another a door ....
    which ask you two # QUESTION:  ...
    if your answer is right then you are going to last level ...
    if your answer is wrong then you go backward ...
    Q1. does ginger eats in cold ...
    Q2. rohit sharma has most centuries against ....
    Here you've four option ....
    press 1 yes and srilanka ...
    press 2 no and newzleand ...
    press 3 yes and australia ...
    press 4 no and australia ...
    """)

    choice = input("> ")

    if choice == "1":
        print("oops ! you are going to room B")
        roomB()

    elif choice == "2":
        print(" oops ! you're going to room A ....")
        roomA()

    elif choice == "3":
        print("congrats ! you're middle floor..")
        middle()

    elif choice == "4":
        print("sorry ! you're going backward the game..")
        roomC()

    elif choice == "5":
        print("you are going to exit the game..")
        exit(0)

    else:
        print("you didn't pick any option . please try one more time ...")
        roomC()
