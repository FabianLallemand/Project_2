import pygame,game

def FMJ():
    gm = game.Game()
    gm.shiplist[gm.shipcnt].Shots += 1
    print(gm.player1.Turn)
    print(gm.player2.Turn)
    if gm.player1.Turn:
        gm.player1.Cards.remove(card1)
    elif gm.player2.Turn:
        gm.player2.Cards.remove(card1)
