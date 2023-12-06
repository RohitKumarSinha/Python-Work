#write a program for accepting a number and guessing what is the number.Number should be upto 10.
def GuessNo():
 num = eval(input("Enter the number :- "))

 print("your number is greater than 5 or not")
 num1 = eval(input("if your number is greater than 5 press 1 smaller than five press 2 otherwise press 3 :- "))

 if(num1 == 1):
    res = eval(input("if your number is odd press 1 if even press 2 :- "))
    if(res == 1):
        res1 = eval(input("if your number is divisible by 3 then press 1 or not 2 :- "))
        if (res1 == 1):
            print("your number is 9")
        else:
            print("your number is 7")
    if(res == 2):
        res2 = eval(input("if your number is divisible by 3 then press 1 divisible by 4 press 2 if divisible by 5 then press 3 :- "))
        if (res2 == 1):
            print("your number is 6")
        if (res2 == 2):
            print("your number is 8")
        if (res2 == 3):
            print("your number is 10")
 if(num1 == 2):
    res = eval(input("if your number is odd press 1 if even press 2 :- "))
    if(res == 1):
        res1 = eval(input("if your number is divisible by 3 then press 1 or not 2 :- "))
        if (res1 == 1):
            print("your number is 3")
        else:
            print("your number is 1")
    if(res == 2):
        res2 = eval(input("if your number is prime then press 1 if not then press 2 :- "))
        if (res2 == 1):
            print("your number is 2")
        if (res2 == 2):
            print("your number is 4")
       
    
 if (num1 == 3):
    print("your number is 5")
GuessNo()
