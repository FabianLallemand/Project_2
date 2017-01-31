import pygame, playboard


class Ship:
    def __init__(self, color, length, x, y, middle , steps, board, health, range,xylist,name, offensive):
        self.Color = color
        self.ShipLength = length
        self.PosX = x
        self.PosY = y 
        self.Middle = middle
        self.Steps = steps
        self.Board = board
        self.Health = health
        self.Range = range
        self.XYlist = xylist
        self.Name = name
        self.Shots = 1
        self.Damage = 1
        self.Offensive = offensive
        

    def draw(self):
        if self.Offensive:
            for length in range(1, self.ShipLength +1):            
                playboard.Grid.get(self.Board, self.PosX, self.PosY + length -1).update(self.Color, 0)
        else:
            for length in range(1, self.ShipLength +1):            
                playboard.Grid.get(self.Board, self.PosX + length - 1, self.PosY).update(self.Color, 0)