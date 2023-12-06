#write a program to find the factorial of the number using recursion
def fact_rec(n):
    if (n == 1):
        return 1
    else:
        return n * fact_rec(n-1)


num = eval(input("Enter a number :- "))
print(fact_rec(num))
