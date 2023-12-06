# write a program to find the fibnocci series in python taking number less than the user
def fibnocci_series():
    num = eval(input("Enter the terms :- "))
    n1 =  0
    n2 = 1

    for i in range(num+1):
        print(n1)
        
        temp = n1
        n1 = n1 + n2;
        n2 = temp


fibnocci_series()

    
