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

    #Shuffle method
    def shuffle(self):
        for i in range(10): #Give it a good shufflin'
            random.shuffle(self.cards)

    #Find out what trump suit is
    def getTrump(self):
        if len(self.cards)==0:
            return random.choice(SUITS)
        return self.cards[0].suit
    
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