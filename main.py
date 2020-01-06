import sys
import os
import time

#Require Python 3
if sys.version_info < (3, 0):
    print("Sorry, please run with Python 3.")
    os.system("python -V")
    sys.exit()

#Access src folder
sys.path.insert(1, "/src")
sys.path.insert(1, "/src/bots")
from src.deck import Deck
from src.player import Player
from src.util import getConf, clear
from src.bots.learner import LearnBot

#The game loop
def startGame(players):
    deck=Deck()
    
    for handCount in range(1, 26):
        hand=handCount if handCount<14 else 26-handCount
        
        #Shuffle the deck
        deck.shuffle()

        #Deal the cards
        for dealing in range(hand):
            for player in players:
                player.deal(deck, deck.cards[0])
        
        #Determine trump suit
        trump=deck.getTrump()
        print("Trump is "+trump)

        #Make bets
        bets=[]
        for player in players:
            i=players.index(player)
            bets.append(player.bet(hand, trump, i==0))
            print(str(player)+" bets "+str(bets[i]))

        sys.exit(0)

        #Play hand
        table=[]
        

        #Cleanup table, cards go back to deck        
        for i in range(len(table)):
            deck.cards.add(table[i])
            table.remove(table[i])


#Main Method=============================================#
def main():
    clear()

    players=[LearnBot(), LearnBot(), LearnBot()]
    for i in range(len(players), 4):
        name=input("Enter player "+str(i+1)+"\'s name: ")  
        players.append(Player(name, False))
        print("")
    
    print("Welcome to \'Oh Well\'")
    #time.sleep(3)
    clear()
    startGame(players)

if __name__=="__main__":
    main()