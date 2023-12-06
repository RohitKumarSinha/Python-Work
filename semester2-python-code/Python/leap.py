#checking whether a year is leap or not
def leapYear():
    year = eval(input("Enter a year :- "))
    flag = 0
    if (year % 4 == 0):
        flag = 1
    if (year % 400 == 0 or year % 100 == 0):
        flag = 1

    if (flag == 1):
        print("This year is leap year")
    else:
        print("This is not a leap year")


leapYear()
        
