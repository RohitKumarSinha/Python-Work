print("here you can do multiple operations with multiple numbers ..")

num = []
i = 1
times = int(input('how many numbers you want to appenf :- '))

while i <= times:
    add = float(input("enter the number you want to operations on them ..."))
    num.append(add)


    i += 1


def doing():
    print("from this number what you want to do: ")
    print("press 1 for addition:- ")
    print("press 2 for subtraction :- ")
    print("press 3 for multiplication :- ")
    print("press 4 for Division :- ")
    print("press 5 for square the number :- ")
    print("press 6 for square root the number :- ")
    print("press 7 for exit the program :-")

    choice = input("> ")

    if choice == "1":
        for i in num:
            a = float(input("from which numbers you want to add all the numbers :- "))
            i += a
            print(i)

        doing()

    elif choice == "2":
        for i in num:
            a = float(input("from which numbers you want to subtract all the numbers :- "))
            i -= a
            print(i)

        doing()

    elif choice == "3":
        for i in num:
            a = float(input("from which numbers you want to multiple all the numbers :- "))
            i *= a
            print(i)

        doing()

    elif choice == "4":
        for i in num:
            a = float(input("from which numbers you want to divide all the numbers :- "))
            i /= a
            print(i)

        doing()

    elif choice == "5":
        for i in num:
            a = float(input("from which numbers you want to square all the numbers :- "))
            i **= a
            print(i)

        doing()

    if choice == "6":
        for i in num:
            a = float(input("from which numbers you want to square root all the numbers :- "))
            i /= 0.5
            print(i)

        doing()

    if choice == "7":
        print("you're going to exit the program ...")
        exit(0)

    else:
        print("you can't choose any option .. please choose one..")
        doing()

doing()
