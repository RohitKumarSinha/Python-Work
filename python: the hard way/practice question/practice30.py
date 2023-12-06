people = 30.7
cars = 40.9
trucks = 15.3

if cars > people or trucks > people:
    print("we should take the cars!!!")

elif cars < people and cars > trucks:
    print("we should not take the cars!!!")

else:
    print("we can't decide!!!")


if trucks > cars and trucks < cars:
    print("that's too many trucks!!!")

elif trucks < cars or trucks > cars:
    print("maybe we could take the trucks!!!")

else:
    print("we can't still decide!!!")


if people > trucks and people > cars:
    print("alright, let's take the truck!!!")

else:
    print("Fine, let's stay home then.")
