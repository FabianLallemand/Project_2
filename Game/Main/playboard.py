import pygame


class Cell:
    def __init__(self, display_resolution, x, y, color, border):
        self.Height = 20
        self.Width = 20
        self.X  = x
        self.Y = y
        self.Screen = display_resolution
        self.Color = color
        self.Border = border

    def draw(self):
        pygame.draw.rect(self.Screen, self.Color, (self.X, self.Y, self.Width, self.Height), self.Border)

    def update(self, color, border):
        self.Color = color
        self.Border = border






class Grid:
    def __init__(self, display_resolution, color, border):
        self.Grid_Height = 20
        self.Grid_Length = 20
        self.Screen = display_resolution
        self.Border = border
        self.Color = color
        self.Cellstorage = []

        for height in range(1, self.Grid_Height + 1):
            for width in range(1, self.Grid_Length + 1):
                 self.Cellstorage.append(Cell(self.Screen, height * 20, width * 20, self.Color, self.Border))


    def get(self, x, y):
        for position in self.Cellstorage:
            if position.X == x * 20 and position.Y == y * 20:
                return position

        return None

    def draw(self):
        for cells in self.Cellstorage:
            cells.draw()


    def update(self, x, y, color, border):
        self.current_cell = self.get(x, y)
        self.current_cell.Color = color
        self.current_cell.Border = border

    def border(self):
        pass
    

