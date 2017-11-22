#!/usr/bin/env python3

# BlackJack For Console.
# Copyright (C) 2017 Erik Bodell and Jerome Sterin.
# BlackJack For Console is distributed under the terms of the GNU General Public License v3.0.
# Be sure to read it before using this program. 
# This program comes with NO warranty or support.

import random
import os
import time

deck = ["2","3","4","5","6","7","8","9","10","KN","D","K","A"]*20

#Funktion för att rensa skärmen

def clearScreen():
    #os.system("cls") #För windows
    os.system("clear") #För linux 

#Liten funktion för välkommstext

def welcome():
    print("Blackjack För Console!")
    print("Licensierad av GPL v3.0")

#Kör programmet så länge variabeln "cash" är över 0.
cash = 200
bet = 0
playerblackjack = 0
playerwin = 0
computerblackjack = 0
computerwin = 0
while cash > 0:
    totalcomputer = 0
    totalplayer = 0
    clearScreen()
    player = [] 
    computer = []
    random.shuffle(deck) 
    playerbust = False
    computerbust = False

    def computerCards(i):
        global totalcomputer
        if i == "A":
            totalcomputer += 11
        elif i == "K":
            totalcomputer += 10
        elif i == "D":
            totalcomputer += 10
        elif i == "KN":
            totalcomputer += 10
        else:
            totalcomputer += int(i)
 
    def playerCards(i):
        global totalplayer
        if i == "A":
            totalplayer += 11
        elif i == "K":
            totalplayer += 10
        elif i == "D":
            totalplayer += 10
        elif i == "KN":
            totalplayer += 10
        else:
            totalplayer += int(i)

    
    for i in range(2):
        x = random.randint(1,13)
        y = random.randint(1,13)
        playerCards(deck[x])
        player.append(deck[x])
        computerCards(deck[y])
        computer.append(deck[y])
        
    
    
    welcome()
    print("\nDu har {} marker".format(cash))
    
    while True:
        try:
            bet = int(input("Hur mycket vill du satsa?"))
            break
        except ValueError:
            print("Välj enbart ett heltal att satsa!")

    
#Kolla så att man inte kan "betta" för mer pengar än var variabeln "cash" innehåller
    
    while bet > cash:                               
        print("Du har inte tillräckligt med marker!")
        while bet > cash:
            try:       
                bet = int(input("Hur mycket vill du satsa?"))
                break
            except ValueError:
                print("Välj enbart ett heltal att satsa!")


#För spelarens kort.
    
    while True:

        print("Delar ut kort....")
        time.sleep(3)
        print("Datorn har följande kort: {}, totalt: {}".format(computer,(totalcomputer)))
        print("Spelaren har följande kort: {}, totalt: {}".format(player,(totalplayer)))
        

        if totalplayer > 21:
            print ("Spelaren BUSTED!")
            playerbust = True
            break
        
        elif totalcomputer == 21:
            print("--- BLACKJACK ---")
            computerblackjack +=1
            break
        elif totalplayer == 21:
            print ("--- BLACKJACK ---")
            print ("+20")
            cash = cash + 20
            playerblackjack +=1
            break 
        else:
            hit = input("[K]ort eller [S]tanna").upper()
            if "K" not in hit:
                break
            else:
                x = random.randint(1,13)
                playerCards(deck[x])
                player.append(deck[x])

#Dela ut datorns kort.
   
    
    while totalcomputer  <=16 and playerbust == False and totalplayer != 21:
            x = random.randint(1,13)
            computerCards(deck[x])
            computer.append(deck[x])
            print("Delar ut kort ...")
            time.sleep(3)
            print("Datorn har följande kort:, {} totalt: {}".format(computer,totalcomputer))
             
#Kolla vem som har vunnit
    if totalcomputer == 21:
        print("--- BLACKJACK ---")
        computerblackjack +=1 
    if totalcomputer > 21:
        print("Datorn BUSTED!")
        computerbust = True   
        
        if playerbust == False:
            print("Spelaren VINNER!")
            print("+{}".format(bet*2))
            playerwin +=1
            cash = cash + bet*2
        
        elif playerbust and computerbust == True:
            print("Ingen VINNARE!")
            
    
    elif totalcomputer > totalplayer:
        print("Datorn VINNER!")
        print("-{}".format(bet))
        computerwin +=1
        cash = cash - bet
        
    elif totalcomputer == totalplayer:
        print("OAVGJORT! Ingen VINNARE!")
        
    elif totalplayer > totalcomputer:
        
        if playerbust == False:
            print("Spelaren VINNER!")
            print("+{}".format(bet*2))
            playerwin +=1
            cash = cash + bet*2
            
        elif computerbust == False:
            print("Datorn VINNER!")
            print("-{}".format(bet))
            computerwin +=1
            cash = cash - bet          
    print("Beräknar resultat ...")
    time.sleep(6)
    clearScreen()
    welcome()
    print("\nSpelaren: {}\nAntal Blackjacks: {}\nDatorn: {}\nAntal Blackjacks: {}\n".format(playerwin,playerblackjack,computerwin,computerblackjack))
    exit = input("Tryck på valfri tangent för att spela igen eller [N]ej för att avsluta!").upper()
    if "N" in exit:
        break
    else :
        print("Du har slut på marker! GAME OVER")
print ("Tack för att du spelade!") 
