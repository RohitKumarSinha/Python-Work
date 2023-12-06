#print the total marks of the subject and percentage
def subjectMarks():
    print("please Enter the marks of five subject")
    sub1 = eval(input("Enter the marks of first subject :- "))
    sub2 = eval(input("Enter the marks of second subject :- "))
    sub3 = eval(input("Enter the marks of third subject : - "))
    sub4 = eval(input("Enter the marks of fourth subject :- "))
    sub5 = eval(input("Enter the marks of five subject :- "))

    total = sub1 + sub2 + sub3 + sub4 + sub5
    print("Total subject marks is :- " , total)

    per = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
    print("percentage of your subject is :- " , per)

subjectMarks()
    

