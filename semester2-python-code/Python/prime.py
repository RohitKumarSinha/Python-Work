#check a number is prime or not
def prime():
    num = eval(input("Enter a positive number :- "))
    flag = 1
    for i in range(2, num):
        if (num % i == 0):
            flag = 0


    if (flag == 1):
        print("it is a prime number")

    if (flag == 0):
        print("it is not a prime number")


prime()
