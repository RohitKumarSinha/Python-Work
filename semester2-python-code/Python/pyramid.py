#printing the pyramid pattern
def pyramid():
    num = eval(input("Enter the value of n :- "))
    for i in range(0, num):
        for j in range(0, i+1):
            print("* " ,end="")
        print("\r")


pyramid()

