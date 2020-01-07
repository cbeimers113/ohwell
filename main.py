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
from src.bots.bot import Bot
from src.bots.learner import LearnBot

#The game loop
def startGame(players):
    deck=Deck()
    
    for handCount in range(1, 26):
        hand=handCount if handCount<14 else 26-handCount
        
        leading=hand%4
        for trick in range(hand):
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
            print("\n\n"+players[leading].name+str(leading)+" leads\n")
            
            for player in players:
                i=players.index(player)
                if isinstance(player, Bot):
                    bets.append(player.bet(hand, trump, i==0))
                else:
                    bets.append(player.bet())
                
            for player in players:
                print(player.name+" bets "+str(bets[players.index(player)]), end="   ")

            print("")
            #Play hand
            table=[]
            for i in range(4):
                index=(i+leading)%4
                print(index)
                #table.append(players[index].play(table, trump, 0, bets[index]))
            print("")
            
            if hand==3:
                sys.exit(0)

            #Cleanup table, cards go back to deck        
            # for i in range(len(table)):
            #     deck.cards.append(table[i])
            #     table.remove(table[i])


#Main Method=============================================#
def main():
    clear()

    players=[LearnBot(), LearnBot(), LearnBot(), LearnBot()]
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