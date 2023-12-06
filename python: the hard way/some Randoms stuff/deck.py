import random

def MakeDeck():
    deck = []
    c = 0
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for v in values:
        for s in suits:
            deck.append([v,s])


    random.shuffle(deck)

    return deck

print(MakeDeck())
