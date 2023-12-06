people = 20
cats = 30
dogs = 15

if people < cats and dogs < cats:
    print("cats is larger in quantity than human beings!!!")

if people > cats or people > dogs:
    print("human beings are always larger in quantity than other animals!!!")

if not(people > dogs or dogs > cats):
    print("we are increasing in very fast in quantity!!!")

if not(people < dogs and dogs > cats):
    print("okk ! supringly dogs are greater in quantity than human beings")

dogs += 5
people -= 3
cats *= 2

if people != dogs:
    print("peple is greater than or equal to dogs!!!")

if people <= dogs:
    print("peple is lesser than or equal to dogs!!!")

if people == dogs:
    print("supringly peple is equal to dogs!!!")

if cats >= people and cats >= dogs:
    print("cats have larger in quantity than all of that!!!")
