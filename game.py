#!/usr/bin/env python3

# BlackJack For Console.
# Copyright (C) 2017 Erik Bodell.
# BlackJack For Console is distributed under the terms of the GNU General Public License v3.0.
# Be sure to read it before using this program. 
# This program comes with NO warranty or support.

import random
import os

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4

playerwin = 0
computerwin = 0

cash = 200
bet = 0

#Funktion för att rensa skärmen

def clearScreen():
    os.system("cls") #För windows
    os.system("clear") #För linux 

#Kör programmet så länge variabeln "cash" är över 0.

while cash > 0:
    os.system("clear")
    player = [] 
    random.shuffle(deck) 
    playerbust = False
    computerbust = False
    
    for i in range(2):
        player.append(random.choice(deck))
    
    
    print("BlackJack for console")   
    print("GPL v3.0\n")
    print("Du har {} marker".format(cash))
    
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
            except ValueError:
                print("Välj enbart ett heltal att satsa!")


#För spelarens kort.
    
    while True:
        totalplayer = sum(player)
        print("Spelaren har följande kort: {}, totalt: {}".format(player,totalplayer))

        if totalplayer > 21:
            print ("Spelaren BUSTED!")
            playerbust = True
            break
        
        elif totalplayer == 21:
            print ("--- BLACKJACK ---")
            print ("+20")
            cash = cash + 20
            break 
        else:
            hit = input("[K]ort eller [S]tanna").upper()
            if "K" not in hit:
                break
            else:
                player.append(random.choice(deck))

#Dela ut datorns kort.
   
    computer = []
    random.shuffle(deck)
    computer.append(random.choice(deck))
    
    while True:

        totalcomputer = sum(computer)          
        
        if totalcomputer < 18:
            computer.append(random.choice(deck))
             
        else:
            break
        
    print("Datorn har följande kort: {}, totalt: {}".format(computer,totalcomputer))

#Kolla vem som har vunnit

    if totalcomputer == 21:
        print("--- BLACKJACK ---")

    if totalcomputer > 21:
        print("Datorn BUSTED!")
        computerbust = True
           
        if playerbust == False:
            print("Spelaren VINNER!")
            print("+{}".format(bet*2))
            playerwin +=1
            cash = cash + bet*2

    elif totalcomputer > totalplayer:
        print("Datorn VINNER!")
        print("-{}".format(bet))
        computerwin +=1
        cash = cash - bet
    elif totalcomputer == totalplayer:
        print("OAVGJORT!")
        
    elif totalplayer > totalcomputer:
        
        if playerbust == False:
            print("Spelaren VINNER!")
            print("+{}".format(bet*2))
            playerwin +=1
            cash = cash + bet*2

        elif computerbust == False:
            print("Datorn VINNER!")
            print("-{},".format(bet))
            computerwin +=1
            cash = cash - bet    
        
    print("Spelaren: {}, Datorn: {}".format(playerwin,computerwin))
    exit = input("Tryck på valfri tanget för att spela igen eller [N]ej för att avsluta!").upper()
    if "N" in exit:
        break
    else:
        print("Du har slut på marker! GAME OVER")
print ("Tack för att du spelade!") 
