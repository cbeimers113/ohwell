#Access parent directory
import sys
sys.path.insert(1, "../")
from src.player import Player
from src.card import Card, SUITS, RANKS

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