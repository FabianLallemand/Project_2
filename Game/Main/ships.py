import pygame, playboard


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
        for length in range(1, self.ShipLength +1):
            
            playboard.Grid.get(self.Board, self.PosX, self.PosY + length -1).update(self.Color, 0)
