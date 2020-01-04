SUITS = ["♥", "♣", "♦", "♠"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
    
    #Instance methods ==============================================

    #Constructor
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank

    def beats(self, card):
        return card.suit==self.suit and RANKS.index(self.rank)>RANKS.index(card.rank)

    def __str__(self):
        return self.rank+self.suit

    #Class methods =================================================

    @staticmethod
    #Return the highest card in a set of suit specified
    def highest(cards, suit):
        if len(cards)==0:return None
        toCheck=[]
        for card in cards:
            if card.suit==suit:toCheck.append(card)

        if len(toCheck)==0:return None
        highest=toCheck[0]
        for card in toCheck:
            if card.beats(highest):highest=card
        return highest

    @staticmethod
    #Return the lowest card in a set of suit specified
    def lowest(cards, suit):
        if len(cards)==0:return None
        toCheck=[]
        for card in cards:
            if card.suit==suit:toCheck.append(card)

        if len(toCheck)==0:return None
        lowest=toCheck[0]
        for card in toCheck:
            if lowest.beats(card):lowest=card
        return lowest