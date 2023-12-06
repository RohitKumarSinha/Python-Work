#printing the power of two upto terms using lambda functions
def powerOfTwo():
    num = int(input("Enter the number :- "))
    result = list(map(lambda x: 2 ** x, range(num + 1)))
    for i in range(num + 1):
        print("2 raised to power",i,"is",result[i])


powerOfTwo()
