from textwrap import dedent
from question8 import *


class question_seven(question_eight):

    def enter(self):
        print(dedent("""
        Here is your seven question .
        Q7. which of these viruses take it's name
        from a place in malaysis .

        1. ebola                       2. influenza
        3. nipah                       4. HIv


        Answer your question in 1, 2, 3, 4 form .
        if you want to exit the game press 5 .
        if you want to use life line press 0 .
        Input your Answer .
        """))

        choice = input("> ")

        if choice == "1":
            print("Wrong Answer !!!")
            print("You won 10,000 rupees")
            exit(0)

        elif choice == "2":
            print("Wrong Answer !!!")
            print("You won 10,000 rupees")
            exit(0)

        elif choice == "3":
            print("Right answer !!!")
            print("You Won 80,000 rupees .")
            print("We are asking you next question .")
            a = question_eight()
            a.enter()

        elif choice == "4":
            print("Wrong Answer !!!")
            print("You won 10,000 rupees")
            exit(0)


        elif choice == "5":
            print("you are going to exit the game .")
            print("you won 40,000 rupees .")
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

                    x = question_seven()
                    x.enter()


                elif choice == "2":
                    print("you take 50 : 50")
                    print("option 2 and 4 are not the answer")

                    x = question_seven()
                    x.enter()

                elif choice == "3":
                    print("you take audience pole")
                    print(" a = 40 %\nb = 10%\nc = 45%\n d = 5%")

                    x = question_seven()
                    x.enter()

                else:
                    print("you can't choose any option please choose a option")

            lifeline()

        else:
            print("you can't choose any option ")
            a = question_seven()
            a.enter()
