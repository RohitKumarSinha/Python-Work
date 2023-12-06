print("""
you enter a dark room with two doors.
Do you go through door #1 or door #2 ???
""")

door = input("> ")

if door == "1":
    print("there's a gaint bear here eating a cheese cake.")
    print("what do you do ?")
    print("1. Take the cake.")
    print("2. screams at the bear.")

    bear = input("> ")

    if bear == "1":
        print("okkk! i think you're smart and foodie..")

    elif bear == "2":
        print("okkk! you're brave and courageous...")

    else:
        print("you can't choose any option...")


elif door == "2":
    print("Here is a poor man. He is very hungry")
    print("what you can do ???")
    print("1. give him the money")
    print("2. give him the food")
    print("3. just walk through and didn't notice the poor man")

    poor = input("> ")

    if poor == "1" or poor == "2":
        print("you have a good heart...")

    elif poor == "3":
        print("please help the poor man. god! will help you")

    else:
        print("i think you can't choose any option")


else:
    print("you can't choose any option. Try one more time ")
