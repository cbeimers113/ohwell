import sys
import os

#Require Python 3
if sys.version_info < (3, 0):
    print("Sorry, please run with Python 3."+os.linesep+"Usage: python3 main.py")
    sys.exit()

#Access src folder
sys.path.insert(1, "/src")
from src.deck import Deck
from src.player import Player


#Main Method=============================================#
def main():
    deck=Deck()
    deck.shuffle()

    player=Player("Dave")

    for i in range(10):
        print("Dealing "+str(deck.cards[i])+" to "+str(player))
        player.deal(deck, deck.cards[i])

    print(str(player))    

if __name__=="__main__":
    main()