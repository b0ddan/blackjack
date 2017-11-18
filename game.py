#!/usr/bin/env python3

import random 
import os

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4

playerwin = 0
computerwin = 0

cash = 200
bet = 0

while cash > 0:
    os.system("clear")
    player = [] 
    random.shuffle(deck)
    playerbust = False
    computerbust = False
    
    for i in range(2):
        player.append(random.choice(deck))
    

    print("Du har {} marker".format(cash))

    bet = int(input("Hur mycket vill du satsa?"))
    
    while bet > cash:
        print("Du har inte så mycket marker!")
        
        bet = int(input("Hur mycket vill du satsa?"))

        if bet <= cash:
            break

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
     
    while True:
         
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
        break    
    
    print("Spelaren: {}, Datorn: {}".format(playerwin,computerwin))
    exit = input("Spela igen? [J]a eller [N]ej").upper()
    if "N" in exit:
        break
    else:
        print("Du har slut på marker! GAME OVER")
print ("Tack för att du spelade!") 
