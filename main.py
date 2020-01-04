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
from src.deck import Deck
from src.player import Player
from src.util import getConf, clear

#The game loop
def startGame(players):
    deck=Deck()
    
    for handCount in range(1, 26):
        hand=handCount if handCount<14 else 26-handCount
        deck.shuffle()

        #Deal the cards
        for dealing in range(hand):
            for player in players:
                player.deal(deck, deck.cards[0])

        bets=[]
        #for i in range(len(players)):
        #   bets[i]=players[i].bet()

        table=[]
        #Play hand

        #Cleanup table, cards go back to deck        
        for i in range(len(table)):
            deck.cards.add(table[i])
            table.remove(table[i])


#Main Method=============================================#
def main():
    clear()

    players=[]
    for i in range(4):
        #Bots can be passed along command line, remove this
        if i<len(sys.argv[1:]):
            players.append(Player(sys.argv[1:][i], True))
            continue
        
        name=input("Enter player "+str(i+1)+"\'s name: ")
        isBot=getConf("Is this player a bot?")    
        players.append(Player(name, isBot))
        print("")

    for i in range(len(players)):
        for j in range(len(players)):
            if j!=i and players[i].name==players[j].name:
                players[i].name+="1"
                players[j].name+="2"
    
    print("Welcome to \'Oh Well\'")
    time.sleep(3)
    clear()
    startGame(players)

if __name__=="__main__":
    main()