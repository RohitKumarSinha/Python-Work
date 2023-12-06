from last_level import *

def doorA():
    print("""
    you're in ground floor .
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
        doorA()

def roomA():
    print("""
    you're in Room A ....
    in this room there are a lot of snake ...
    and also there is a bin which helps to handle the snake ....
    But the problem is the bin is surrounded by the Snake ....
    Here There's two option for you ...
    press 1 exit the game...
    press 2 fight with the snake ...
    """)

    choice = input("> ")

    if choice == "1":
        print("you're going to exit the room")
        exit(0)

    elif choice =="2":
        print("great, you're very brave person")
        fight()

    else:
        print("you didn't choose any option. try one more time...")
        roomA()

def fight():
    print("""
    Here you have two option for grab the bin ...
    press 1 for go slowly and grab the bin ....
    press 2 for go quickly and grab the bin...
    """)

    choice = input("> ")

    if choice == "1":
        print("""
        congrats, you grab the bin ....
        But you're badly hurted from your hands ...
        The snakes are in of control ...
        """)
        goahead()

    elif choice == "2":
        print("""
        congrats, you grab the bin ....
        But you're badly hurted from your legs ...
        The snakes are in of control ...
        """)
        goahead()

    else:
        print("you didn't pick any option . please try one more time ...")
        fight()

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
    infront of you there is a big dragon ....
    There is also a weapon to fight with dragon ...
    Here you've two option ....
    press 1 for grab the weapon and fight with the dragon ...
    press 2 for exit the game ...
    """)

    choice = input("> ")

    if choice == "1":
        print("great, you're so brave . go and fight with the dragon ...")
        weapon()

    elif choice == "2":
        print("you're going to exit the game ....")
        exit(0)

    else:
        print("you didn't pick any option . please try one more time ...")
        roomC()


def weapon():
    print("""
    you grab the weapon ...
    now its time to hit the dragon with the help of weapon ...
    you can hit the dragon three places ...
    but the problem is that if you hit wrong place you are going back to the game ...
    if you are hit right place then you will move forward to the game ....
    press 1 for hit head ...
    press 2 for hit tail ...
    press 3 for hit stomach ...
    press 4 for exit game ...
    """)

    choice = input("> ")

    if choice == "1":
        print("oops ! you are  going to room B")
        roomB()

    elif choice == "2":
        print("oops ! you are going to room A")
        roomA()

    elif choice == "3":
        print("congrats ! you are going to the last level of game !")
        middle()

    elif choice == "4":
        print("you are going to be exit the game !!!")
        exit(0)

    else:
        print("you didn't pick any option . please try one more time ...")
        weapon()
