#sum of natural number using loop
def sum():
    num = eval(input("Enter a number :- "))
    count = 0
    for i in range(num+1):
        count += i

    print("sum of n natural number is ", count)

sum()

    
