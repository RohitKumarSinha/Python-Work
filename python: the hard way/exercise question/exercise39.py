# create a mapping of state to abbrevation

states = {
      "Bihar" : "BR",
      "Uttar Pradesh" : "UP",
      "Delhi" : "DL",
      "Madya Pradesh" : "MP",
      "Maharastra" : "MA"
}

# create a basic set of states and some cities in them

cities = {
      "BR" : "Patna",
      "UP" : "Agra",
      "DL" : "Gurgoen",
      "MP" : "Bhopal",
      "MA" : "Munbai"
}

# add more cities

cities['RJ'] = 'kach',
cities['WB'] = "Durgapur"

# print out some cities

print("-" * 20)
print("RJ state has : ",cities['RJ'])
print("wB state has : ",cities['WB'])

# print out some states

print("-" * 20)
print("Bihar abbereviation is : ",states['Bihar'])
print("Delhi abbereviation is : ",states['Delhi'])

# do it by using the state then cities dict

print("-" * 20)
print("Bihar has : ",cities[states['Bihar']])
print("Delhi has : ",cities[states['Delhi']])

#  print every state abbereviation

print("-" * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbereviation {abbrev}")

# print every city in state

print("-" * 20)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time

print("-" * 20)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbereviation {abbrev}")
    print(f"and has cities {cities[abbrev]} ")

print('-' * 20)

# safely get a abbereviation by state that might not be there

state = states.get('Texas')

if not state:
    print("sorry, no Texas")

# get a city with a default value

city = cities.get("Tx", "Does not exist")
print(f"The cities for the state 'Tx' is : {city} ")
