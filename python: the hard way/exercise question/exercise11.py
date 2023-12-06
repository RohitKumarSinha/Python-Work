from textwrap import dedent
from exercise12 import *


class question_eleven(question_twelve):

    def enter(self):
        print(dedent("""
        Here is your eleven question .
        Q11. according to the mahabharata, who was the
        father of chitrasena , vrishasena and satyasena .

        1. karna                       2. Dhritarashtra
        3. arjuna                        4. yudhishthira


        Answer your question in 1, 2, 3, 4 form .
        if you want to exit the game press 5 .
        if you want to use life line press 0 .
        Input your Answer .
        """))

        choice = input("> ")

        if choice == "1":
            print("Right answer !!!")
            print("You Won 12,50000 rupees .")
            print("We are asking you next question .")
            a = question_twelve()
            a.enter()

        elif choice == "2":
            print("Wrong Answer !!!")
            print("You won 1,60000 rupees")
            exit(0)

        elif choice == "3":
            print("Wrong Answer !!!")
            print("You won 1,60000 rupees")
            exit(0)

        elif choice == "4":
            print("Wrong Answer !!!")
            print("You won 1,60000 rupees")
            exit(0)


        elif choice == "5":
            print("you are going to exit the game .")
            print("you won 6,40000 rupees .")
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

                    x = question_eleven()
                    x.enter()


                elif choice == "2":
                    print("you take 50 : 50")
                    print("option 2 and 4 are not the answer")

                    x = question_eleven()
                    x.enter()

                elif choice == "3":
                    print("you take audience pole")
                    print(" a = 40 %\nb = 10%\nc = 45%\n d = 5%")

                    x = question_eleven()
                    x.enter()

                else:
                    print("you can't choose any option please choose a option")

            lifeline()

        else:
            print("you can't choose any option ")
            a = question_eleven()
            a.enter()
