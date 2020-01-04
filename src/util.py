import os

#Get confirmation from a y/n question
def getConf(message):
    answer=None
    acceptable=["y", "ye", "yes", "n", "no"]
    while not answer in acceptable:
        if answer!=None:
            print("Error: must specify yes or no.")
        answer=input(message+" (yes/no): ").lower()
    return acceptable.index(answer)<3

#Clear the console screen
def clear():
    os.system("cls" if os.name=="nt" else "clear")