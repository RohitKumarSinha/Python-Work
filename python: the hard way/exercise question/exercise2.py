def name(para):

    a = para[::2]
    return a

print(name("rohit"))

def end_other(str1, str2):
    return str1.lower()[len(str2)-1:] == str2.lower() #str1.lower() has convert the lower case of all the alphabet in str1
    # len(str2) has return the length of str2 and -1 to it
    # by subtracting -1 now we slice the str 2

print(end_other('Hiabc', 'abc'))


def doubleChar(str1):
    final_str = ""  # assing empty_str to variable final_str
    for letter in str1:  # iterate the letter from str1
        final_str += letter + letter # adding the letter with himself and assing or adding to the final_str
    return final_str # return the final_str

print(doubleChar("rohit"))

def sum(a, b, c):
    if a >= 13:
        a = 0

    if b >= 13:
        b = 0

    if c >= 13:
        c = 0

    return a + b + c

print(sum(1, 2, 3))
print(sum(17, 2, 3))
print(sum(1, 21, 3))
print(sum(1, 2, 13))
