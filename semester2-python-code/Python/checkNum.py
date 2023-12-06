# check a number is positive, negative or zero
def checkNum():
    num = eval(input("Enter a number :-  "))
    if (num == 0):
        print("it is a zero number")

    if(num > 0):
        print("it is a positive number")

    if(num < 0):
        print("it is a negative number")

checkNum()
