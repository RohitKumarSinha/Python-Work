#converting number to celsius to fahrenheit 
def celToFah(num):
    temp = 9/5 * num + 32
    print("your number after converting fahrenheit to celsius  ", temp)

#converting number feet to inches
def feetToinch(num):
    inch = num * 12
    print("inch of your number is ", inch)

#converting number kilo to pound
def kiloTopound(num):
    pound = num * 2.205
    print("pound of your kilogram is ", pound)

#converting number meter to cm
def metTocm(num):
    cm = num * 100
    print("centimeter of yor meter is ", cm)


#calling the functions
num = eval(input("Enter your number :- "))
celToFah(num)
feetToinch(num)
kiloTopound(num)
metTocm(num)
