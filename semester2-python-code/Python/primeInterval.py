#print all the prime number between two intervals
def primeInterval():
    lower = int(input("Enter the first number :- "))
    upper = int(input("Enter the second number :- "))

    for number in range (lower, upper + 1):
        flag = 0
        for i in range (2, number):
            if (number % i) == 0:
                flag = 1
        if (flag == 0):
            print(number)

primeInterval()
    
