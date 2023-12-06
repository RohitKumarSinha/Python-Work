from textwrap import dedent
from question1 import *

class intro(question_one):

    def enter(self):
        print(dedent("""
        welcome to kaun banega crorepati game .
        We have ask you 14 question .
        every question has a price tag .
        # QUESTION number 5 and 9 is stable question:
        you have 3 life line to help in question if any question you have problem .
        your first life line is 50 : 50
        your second life line is 'expert advice' .
        your last life line is 'audience pole' .
        you can quit the game any time .
        Here the price of your question .

        14. 1 crore
        13. 50,00000
        12. 25,00000
        11. 12,50000
        10. 6,40000
        9.  3,20000 *** stable question
        8.  1,60000
        7.  80000
        6.  40000
        5.  20000
        4.  10000 *** stable question
        3.  5000
        2.  2000
        1.  1000

        press 1 for start the game .
        otherwise enter anything to quit the game .
        """))

        choice = input("> ")

        if choice == "1":
            print("lets start the game .")
            b = question_one()
            b.enter()

        else:
            print("you're going to exit the game .")
            exit(0)

a = intro()
a.enter()
