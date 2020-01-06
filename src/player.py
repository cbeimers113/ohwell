from math import log
from src.deck import Deck

class Player:

    def __init__(self, name, isBot):
        self.name=name
        self.hand=[]
        self.isBot=isBot

    #Bet the amount of tricks you'll win
    def bet(self):
        inp=input("How many trick would you like to bet?\n:")
        bid=None
        try:
            bid = int(inp)
            if bid < 0:throw=int("a string")
            return bid
        except:
            print("Error, bet amount must be positive integer.")
            return self.bet()

    #Deal card from source deck to player; deck is passed so that the card can be removed from it
    def deal(self, deck, card):
        self.hand.append(card)
        deck.cards.remove(card)
        self.hand=Deck.sort(self.hand)

    #toString method, display name and hand
    def __str__(self):
        string=self.name
        if len(self.hand)>0:string+=" ["
        for card in self.hand:
            string+=str(card)+(", " if self.hand.index(card)<len(self.hand)-1 else "]")
        return string