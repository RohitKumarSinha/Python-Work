from sys import exit

def chinese():
    print("Do you want to eat role or noodles")
    print("for role press 1")
    print("for noodles press 2")

    choice = input("> ")

    if choice == "1":
        print("okk which type of role of you want")
        roles()

    elif choice == "2":
        print("okk which type of noodles of you want")
        noodles()

    else:
        print("you can't choose any option")
        chinese()

def roles():
    print("which types of role you want ?")
    print("press 1 for chicken role")
    print("press 2 for paneer role")
    print("press 3 for mutton role")
    print("press 4 for egg role")

    choice = input("> ")

    if choice == "1":
        print("pay 60 rupees")
        print("Here is your role")
        exit(0)

    elif choice == "2":
        print("pay 50 rupees")
        print("Here is your role")
        exit(0)

    elif choice == "3":
        print("pay 80 rupees")
        print("Here is your role")
        exit(0)

    elif choice == "4":
        print("pay 30 rupees")
        print("Here is your role")
        exit(0)

    else:
        print("you can't enter any option please, try one more time")
        roles()


def noodles():
    print("which types of noodles you want ?")
    print("press 1 for chicken noodles")
    print("press 2 for paneer noodles")
    print("press 3 for manchurian noodles")
    print("press 4 for egg noodles")

    choice = input("> ")

    if choice == "1":
        print("pay 75 rupees")
        print("Here is your chicken noodles")
        exit(0)

    elif choice == "2":
        print("pay 60 rupees")
        print("Here is your paneer noodles")
        exit(0)

    elif choice == "3":
        print("pay 50 rupees")
        print("Here is your manchurian noodles")
        exit(0)

    elif choice == "4":
        print("pay 40 rupees")
        print("Here is your egg noodles")
        exit(0)

    else:
        print("you can't enter any option please, try one more time")
        noodles()


def italian():
    print("Do you want to eat pizza or burger")
    print("for pizza press 1")
    print("for burger press 2")

    choice = input("> ")

    if choice == "1":
        print("okk which type of pizza of you want")
        pizza()

    elif choice == "2":
        print("okk which type of burger of you want")
        burger()

    else:
        print("you can't choose any option")
        italian()

def pizza():
    print("which types of pizza you want ?")
    print("press 1 for chicken pizza")
    print("press 2 for paneer pizza")
    print("press 3 for cheese pizza")
    print("press 4 for pan pizza")

    choice = input("> ")

    if choice == "1":
        print("pay 250 rupees")
        print("Here is your chicken pizza")
        exit(0)

    elif choice == "2":
        print("pay 200 rupees")
        print("Here is your paneer pizza")
        exit(0)

    elif choice == "3":
        print("pay 180 rupees")
        print("Here is your cheese piza")
        exit(0)

    elif choice == "4":
        print("pay 120 rupees")
        print("Here is your pan pizza")
        exit(0)

    else:
        print("you can't enter any option please, try one more time")
        pizza()


def burger():
    print("which types of burger you want ?")
    print("press 1 for chicken burger")
    print("press 2 for paneer burger")
    print("press 3 for cheese burger")
    print("press 4 for egg burger")

    choice = input("> ")

    if choice == "1":
        print("pay 120 rupees")
        print("Here is your chicken burger")
        exit(0)

    elif choice == "2":
        print("pay 100 rupees")
        print("Here is your panner burger")
        exit(0)

    elif choice == "3":
        print("pay 80 rupees")
        print("Here is your cheese burger")
        exit(0)

    elif choice == "4":
        print("pay 50 rupees")
        print("Here is your egg burger")
        exit(0)

    else:
        print("you can't enter any option please, try one more time")
        burger()

def food():
    print("which type of food your you want")
    print("press 1 for chinese")
    print("press 2 for italian")

    choice = input("> ")

    if choice == "1":
        chinese()

    elif choice == "2":
        italian()

    else:
        print("you can't enter any option")
        food()

food()
