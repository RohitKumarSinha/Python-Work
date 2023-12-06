ten_things = "apples oranges crows telephone light sugar"

print("wait there are not 10 things in that list . let's fix that. ")

stuff = ten_things.split(" ")

print(stuff)

more_stuff = ["Day", "night", "song", "girl", "boy", "banana", "corn"]


while len(stuff) != 10:
    next_one = more_stuff.pop(0)
    print("Adding : ",next_one)

    stuff.append(next_one)
    print(f"There are {len(stuff)} items now .")

print("there we go: ",stuff)

print("||".join(stuff))
