from cla import *

class song1():

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def song(self):
        for line in self.lyrics:
            print(line)

kishore = song1(["aaj mausam bada baimaan hai bada",
                 "aaj mausam..."])

kishore1 = song1(["ooo jane janna dudhe tuhe dewaana",
                  "sapno mai roj aay aa zindgi mai aana"])

print("""hello what do you want ...

do you want listen song
or do you want to give your intro
or do you want to give the details of your dream phone
press 1 for song
press 2 for intro
press 3 for dream phone""")

choice = input("> ")

if choice == "1":
    kishore.song()
    kishore1.song()

elif choice == "2":
    details = profile('233','233','344','344','344','3444','344')
    details.get()
    details.post()

elif choice == "3":
    details = mobile('233','233','344','344','344','3444','344')
    details.get()
    details.post()

else:
    print("you can't choose any option")
