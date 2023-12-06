#downward pattern printing
def downwardPyramid():
    num = eval(input("Enter the value of n :- "))
    for i in range(num, 0, -1):
        for j in range(0, i):
            print("* " ,end="")
        print("\r")


downwardPyramid()

