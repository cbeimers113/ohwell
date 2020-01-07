#Access parent directory
import sys
sys.path.insert(1, "../")
from src.player import Player
from src.card import Card, SUITS, RANKS
from random import choice
from time import sleep

class Bot(Player):

    def __init__(self, name, b_Ld_Tr, b_NLd_Tr, b_Ld_NTr, b_NLd_NTr):
        super().__init__(name, True)
        self.b_Ld_Tr=b_Ld_Tr #Min rank to bet for hand with n cards if leading and has trump
        self.b_Ld_NTr=b_Ld_NTr #Min rank to bet for hand with n cards if not leading and has trump
        self.b_NLd_Tr=b_NLd_Tr #Min rank to bet for hand with n cards if leading and has no trump
        self.b_NLd_NTr=b_NLd_NTr #Min rank to bet for hand with n cards if not leading and has no trump

    #Try to determine how many cards to bet
    def bet(self, num, trump, isLeading):
        bet=0
        for card in self.hand:
            rank=RANKS.index(card.rank)
            if card.suit==trump:
                bet+=1 if (rank>=RANKS.index(self.b_Ld_Tr[num]) and isLeading) or rank>=RANKS.index(self.b_NLd_Tr[num]) else 0
            else:
                bet+=1 if (rank>=RANKS.index(self.b_Ld_NTr[num]) and isLeading) or rank>=RANKS.index(self.b_NLd_NTr[num]) else 0
        return bet

    #TODO: don't play a trump if reached goal, bet more if leading and have high card, bet more if num cards is low 
    #Play a card
    def play(self, table, trump, tricks, bet):
        sleep(1)
        cards=[]
        for card in self.hand:
            cards.append(card)
            
        if len(table) > 0:
            led=table[0]
            follow=[]
            for card in cards:
                if card.suit==led.suit:
                    follow.append(card)
                    cards.remove(card)
            
            if len(follow)>0:
                lowest=follow[0]
                for card in follow:
                    if lowest.beats(card):lowest=card
                highest=follow[0]
                for card in follow:
                    if card.beats(highest):highest=card
                
                if tricks == bet: #Try to lose the trick
                    return lowest
                else: #Try to win more or conserve higher cards
                    #Check if can win hand
                    for card in table:
                        if card.rank == led.rank and card.beats(highest):
                            return lowest
                    return highest
                return choice(follow)
        
        trumps=[]
        for card in cards:
            if card.suit==trump:
                trumps.append(card)
                cards.remove(card)
        
        if len(trumps)>0:
            return choice(trumps)
        
        return choice(cards)