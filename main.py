import sys
import os
import time

#Require Python 3
if sys.version_info < (3, 0):
    print("Sorry, please run with Python 3.")
    os.system("python -V")
    sys.exit()

#Require Colorama
try:
    from colorama import init, Fore, Back, Style
    init()
except:
    print("This program requires Colorama. Installing now, then restart.")
    os.system("pip install colorama")

#Access src folder
sys.path.insert(1, "/src")
sys.path.insert(1, "/src/bots")
from src.deck import Deck
from src.card import SUITS
from src.player import Player
from src.util import getConf, clear
from src.bots.bot import Bot
from src.bots.learner import LearnBot

SHOWOUTPUT=True

#Determine who won the trick
def getWinner(table, trump):
    led=table[0]
    highest=led
    for card in table:
        if card==led:continue
        if card.suit == led.suit and card.beats(highest):highest=card
    
    if  led.suit!=trump:
        for card in table:
            if card==led:continue
            if card.suit==trump:
                if highest.suit != trump:highest=card
                else: 
                    if card.beats(highest):highest=card
    return table.index(highest)

#The game loop
def startGame(players):
    deck=Deck()
    scores=[0,0,0,0]

    for handCount in range(1, 26):
        hand=handCount if handCount<14 else 26-handCount
        leading=hand%4
        won=leading

        #Shuffle the deck
        deck.shuffle()
        
        #Deal the cards
        for dealing in range(hand):
            for player in players:
                player.deal(deck, deck.cards[0])
        
        #Display scores
        clear()
        for i in range(4):
            cols=[Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.YELLOW]
            print(cols[i]+players[i].name+": "+str(scores[i]), end=" ")
        print(Style.RESET_ALL+"")

        #Determine trump suit
        trump=deck.getTrump()
        fores=[Fore.RED, Fore.BLACK]
        if SHOWOUTPUT: print("\nTrump is "+fores[SUITS.index(trump)%2]+Back.WHITE+trump+" "+Style.RESET_ALL)

        #Make bets
        bets=[]
        tricks=[0,0,0,0]
        if SHOWOUTPUT: print("\n"+players[leading].name+" leads\n")
        
        for player in players:
            i=players.index(player)
            if isinstance(player, Bot):
                bets.append(player.bet(hand-1, trump, i==0))
            else:
                bets.append(player.bet())
            
        for player in players:
            if SHOWOUTPUT: print(player.name+" bets "+str(bets[players.index(player)]), end="   ")

        if SHOWOUTPUT: print("\n")
        
        #Play hand
        for trick in range(hand):
            table=[]
            for i in range(4):
                index=(i+won)%4
                played=players[index].play(table, trump, 0, bets[index])
                players[index].hand.remove(played)
                table.append(played)
                if SHOWOUTPUT: print(players[index].name+" plays "+str(played))

            winner=(getWinner(table, trump)+won)%4
            if SHOWOUTPUT: print("\n"+players[winner].name+" wins\n")
            won=winner
            tricks[winner]+=1
            
            #Cleanup table, cards go back to deck        
            while len(table)>0:
                deck.cards.append(table[0])
                table.remove(table[0])

        for i in range(4):
            scores[i]+=tricks[i]
            if tricks[i]==bets[i]:scores[i]+=5

        input("Press Enter to continue to next hand")



#Main Method=============================================#
def main():
    global SHOWOUTPUT
    if len(sys.argv)>1:
        try:
            SHOWOUTPUT=[False, True][int(sys.argv[1])]
        except:
            print("Show output on/off specified by 0/1")
            sys.exit(1)

    clear()

    players=[LearnBot(), LearnBot(), LearnBot(), LearnBot()]
    for i in range(4):
        players[i].name+=str(i)

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