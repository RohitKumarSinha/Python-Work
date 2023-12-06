from textwrap import dedent
from question4 import *


class question_three(question_four):

    def enter(self):
        print(dedent("""
        Here is your third question .
        Q3. Which state of india has the shortest
        coastline .

        1. Goa                             2. Maharashtra
        3. odisha                          4. West Bengal


        Answer your question in 1, 2, 3, 4 form .
        if you want to exit the game press 5 .
        if you want to use life line press 0 .
        Input your Answer .
        """))

        choice = input("> ")

        if choice == "1":
            print("Right answer !!!")
            print("You Won 5,000 rupees .")
            print("We are asking you next question .")
            a = question_four()
            a.enter()


        elif choice == "2":
            print("Wrong Answer !!!")
            print("You won nothing")
            exit(0)

        elif choice == "3":
            print("Wrong Answer !!!")
            print("You won nothing")
            exit(0)


        elif choice == "4":
            print("Wrong Answer !!!")
            print("You won nothing")
            exit(0)

        elif choice == "5":
            print("you are going to exit the game .")
            print("you won 2,000 rupees .")
            exit(0)

        elif choice == "0":
            def lifeline():
                print("which life line you want to choose")
                print("if you want expert advice press 1")
                print("if you want 50 : 50 press 2")
                print("if you want  audience pole press 3")

                choice = input("> ")

                if choice == "1":
                    print("you take expert advice .")
                    print("i think its 1 but i am not sure .")

                    x = question_three()
                    x.enter()


                elif choice == "2":
                    print("you take 50 : 50")
                    print("option 2 and 4 are not the answer")

                    x = question_three()
                    x.enter()

                elif choice == "3":
                    print("you take audience pole")
                    print(" a = 40 %\nb = 10%\nc = 45%\n d = 5%")

                    x = question_three()
                    x.enter()

                else:
                    print("you can't choose any option please choose a option")

            lifeline()

        else:
            print("you can't choose any option ")
            a = question_three()
            a.enter()
