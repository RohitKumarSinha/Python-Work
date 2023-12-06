#check whether a student is fail or pass in exam
def subjectMarks():
    print("please Enter the marks of five subject")
    sub1 = eval(input("Enter the marks of first subject out of 100 :- "))
    sub2 = eval(input("Enter the marks of second subject out of 100 :- "))
    sub3 = eval(input("Enter the marks of third subject out of 100 : - "))
    sub4 = eval(input("Enter the marks of fourth subject out of 100 :- "))
    sub5 = eval(input("Enter the marks of five subject out of 100 :- "))

    if (sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33):
        print("you fail in the examination !! better luck next time")

    else:
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total subject marks is :- " , total)

        per = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
        print("percentage of your subject is :- " , per)
        
subjectMarks()
    

