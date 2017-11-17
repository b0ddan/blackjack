#!/usr/bin/env python3

import random 
import os

deck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4

playerwin = 0
computerwin = 0

while True:
    os.system("clear")
    player = [] 
    random.shuffle(deck)
    playerbust = False
    computerbust = False
    
    for i in range(2):
        player.append(random.choice(deck))

    while True:

        totalplayer = sum(player)
        print("Spelaren har följande kort: {}, totalt: {}".format(player,totalplayer))

        if totalplayer > 21:
            print ("Spelaren BUSTED!")
            playerbust = True
            break
        
        elif totalplayer == 21:
            print ("--- BLACKJACK ---")
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
                playerwin +=1
        
        elif totalcomputer > totalplayer:
            print("Datorn VINNER!")
            computerwin +=1
        
        elif totalcomputer == totalplayer:
            print("OAVGJORT!")
        
        elif totalplayer > totalcomputer:
            if playerbust == False:
                print("Spelaren VINNER!")
                playerwin +=1
            elif computerbust == False:
                print("Datorn VINNER!")
                computerwin +=1
        break    
    
    print("Spelaren: {}, Datorn: {}".format(playerwin,computerwin))
    exit = input("Spela igen? [J]a eller [N]ej").upper()
    if "N" in exit:
        break

print ("Tack för att du spelade!") 
