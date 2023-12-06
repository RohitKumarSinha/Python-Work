from sys import exit

def gold_room():
    print("this room is full of gold.\t How much you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("Man, learn to type a number. ")

    if how_much < 50:
        print("nice, you're not greedy, you win!")

    else:
        print("you greedy bastard!")

def bear_room():
    print("there is a bear here")
    print("the bear has a bunchy of honey!!!")
    print("the fat bear is in front of another door.")
    print("how are you going to move the bear ?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off .")

        elif choice == "taunt bar" and not bear_moved:
            print("the bear has moved from the door . ")
            print("you can go through it now .")
            bear_moved = True

        elif choice == "taunt bar" and bear_moved:
            dead("The bear gets pissed off and chews your legs off .")

        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print("I got no idea what that means.")


def evil_room():
    print("here you see the great evil rohit")
    print("He, it, whatever stares at you and you go insane .")
    print("Do you flee for your life or eat your head .")

    choice = input("> ")

    if "flee" in choice:
        start()

    elif "head" in choice:
        dead("well that was tasty!")

    else:
        evil_room()


def dead(why):
    print(why , "good job!")
    exit(0)

def start():
    print("you are in dark room .")
    print("There is a door to your right and left .")
    print("which one do you take ?")

    choice = input("> ")

    if choice == "left":
        bear_room()

    elif choice == "right":
        evil_room()

    else:
        dead("you stumble around the room until you starve .")

start()
