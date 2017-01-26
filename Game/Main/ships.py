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
        for length in range(self.ShipLength):
                playboard.Grid.get(self.Board, self.PosX, self.PosY).update(self.Color, 0)
                self.PosY += 1            
