#swapping the numbers 
def swap():
    num1 = eval(input("Enter first number:- "))
    num2 = eval(input("Enter second number:- "))

    temp = num1
    num1 = num2
    num2 = temp

    print("Your first and second number are :- ", num1, num2)

swap()
