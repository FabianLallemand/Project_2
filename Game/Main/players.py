import pygame, game


class Player:
    def __init__(self, name, icolor,acolor):
        self.Name = name
        self.aColor = acolor
        self.iColor = icolor
        
        self.Cards = []
        self.Turn = False
        self.shipsplaced = 0