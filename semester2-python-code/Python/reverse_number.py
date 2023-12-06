#write a program to reverse the user number

def reverse():
    num = 1234
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print(reversed_num)


reverse()
