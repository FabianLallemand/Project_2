import pygame
import playboard

#import colors

brown = (139,69,19)


class Ship:
    def __init__(self, color, length, x, y, middle , speed, board, health, range):
        self.Color = color
        self.ShipLength = length
        self.PosX = x
        self.PosY = y 
        self.Middle = middle
        self.Speed = speed
        self.Board = board
        self.Health = health
        self.Range = range

    def draw(self):
        for length in range(self.ShipLength + 1):
                playboard.Grid.get(self.Board, self.PosX, self.PosY).update(brown, 0)             
