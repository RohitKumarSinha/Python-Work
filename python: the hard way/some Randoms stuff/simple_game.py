import random          # import random module to generate random Number
def generate_code():   # define a function name generate_code and passing no argument
    digits = list(range(10))  # generate number from 1 to 10 and make them to list and assign to variabe digits
    random.shuffle(digits)  # shuffle the numbers from 1 to 10 numbers
    print(digits[:3])  # print the numbers and slicing the number from index position 0 to 3
    return (digits[:3]) # return the numbers and slicing the number from index position 0 to 3

def TakeNumbers():  # define a function name TakeNumbers and passing no argument
    # number = list(input("Enter your guess ?"))
    # here we do list comphrension
    # firstly we input the number and assign to variabe n and split with the help of , and convert the number into int form in list.
    number=[int(n) for n in input("Enter Number:").split(",")]
    return number # return the number to the function

def comp(gen_code,usr_inp):  # define a function name comp and passing argument gen_code and usr_inp

    if (gen_code==usr_inp): # if the expression is true then we return a string "code CRACKED"
        return "Code CRACKED!!"
    # code for comaparison of user input and generated code
    for count, elem in enumerate(gen_code):   # in count int form is assign and in elem we assign the sting
        if elem==usr_inp[count]: # if
            return "Match"
        elif elem==usr_inp:
            return "Close"
        else:
            return "Nope"

# Run Game
print (" Welcome to code breaker, Guess 3 digits")
# declaring return_code
return_code=""
#ask the user until he gives correct code
while (return_code != "Code CRACKED!!"):
    # take user guess
    usr_inp=TakeNumbers()
    # generate the numbers
    gen_code = generate_code()
    # comaparison
    return_code=comp(gen_code,usr_inp)
    # print result
    print(return_code)
