import random
from src.card import Card, SUITS, RANKS

class Deck:

    #Instance methods=======================================================================

    #Constructor
    def __init__(self):
        self.cards=[]
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    #Instance shuffle method
    def shuffle(self):
        for i in range(10): #Give it a good shufflin'
            random.shuffle(self.cards)
    
    #Class methods================================================================================

    @staticmethod
    #Sort into sub-decks by suit, then sort those by rank
    def sort(cards):
        bySuit=[[],[],[],[]]
        for card in cards:
            index=SUITS.index(card.suit)
            bySuit[index].append(card)

        sorted=[]
        for suit in bySuit:
            while len(suit)>0:
                card=Card.highest(suit, suit[0].suit)
                sorted.append(card)
                suit.remove(card)     
        return sorted         