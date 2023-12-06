i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    print("numbers in the list ",numbers)

    i+= 1
    print(f"increment the value of 1 and now, the number is {i}")

print("the numbers:")

for num in numbers:
    print(num)
