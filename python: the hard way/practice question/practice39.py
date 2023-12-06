items = {}

def welcome():

    print("welcome to dictionary ...")
    print("if you want to add items press 1")
    print("if you want to remove items press 2")
    print("if you want to see the items press 3")
    print("if you want to see the items price press 4")
    print("if you want to sum the item price press 5")
    print("if you want to exit the program press 6")

    choice = input("> ")

    if choice == "1":

        i = 1

        times = int(input("How many items you want to add in the list :-"))

        while i <= times:

            product = input("enter the item name :- ")
            price = float(input("enter the price of the item :- "))

            items.update({product:price})

            i += 1

        print(items)
        print("length of your items is : - ",len(items))
        welcome()

    elif choice == "2":

        rem = input("which items you want to remove  :- ")

        del items[rem]

        print("your items is remove now ")
        print(items)

    elif choice == "3":

        print("here is your items :- ")
        print(list(items.keys()))
        welcome()

    elif choice == "4":

        print("here is your price :-")
        print(list(items.values()))
        welcome()

    elif choice == "5":
        print("here is the sum of all price :-")
        print(sum(list(items.values())))
        welcome()

    elif choice == "6":
        print("you are going to exit the program")
        exit(0)

    else:
        print("you can't choose any option ... please choose one")
        welcome()

welcome()
