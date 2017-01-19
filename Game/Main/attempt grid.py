import pygame
import sys

class Game:
    def __init__(self):
        screen_width = 440
        screen_height = 440
        screen_size = (screen_width, screen_height)
        pygame.init()
        self.Screen = pygame.display.set_mode(screen_size)
        self.name = pygame.display.set_caption("Battleport")
        self.Gameboard = board.Grid(self.Screen, (255, 255, 255), 1)

    def get_board(): return Gameboard

    def draw(self):
        self.Screen.fill((0,0,0))

        board.Grid.update(self.Gameboard, 10, 10, (255, 0, 0), 0)
        self.Gameboard.draw()
        
        pygame.display.flip()

    def game_loop(self):
        while not process_events():
            self.draw()
        sys.exit()
        pygame.QUIT

# process pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    
    return False

# create a program function
def program():
    game = Game()
    game.game_loop()

program()







class Cell:
    def __init__(self, screen, x, y, color, border):
        self.Length = 20
        self.Width = 20
        self.X = x
        self.Y = y
        self.Screen = screen
        self.Color =  color
        self.Border = border
    def getX(self): return self.X

    def getY(self): return self.Y

    def draw(self):
        pygame.draw.rect(self.Screen, (self.Color), [self.X, self.Y, self.Width, self.Length], self.Border)

    def update(self):
        pass

# create a grid class to render cells on the grid
class Grid:
    def __init__(self, screen, color, border):
        self.GridLength = 20
        self.GridWidth = 20
        self.Screen = screen
        self.Border = border
        self.Color = color

        self.cell_list = []

        for row in range(1, self.GridWidth + 1):
            for column in range(1, self.GridLength + 1):
                self.cell_list.append(Cell(self.Screen, row * 20, column * 20, self.Color, self.Border))

    def get(self, x, y):
        for pos in self.cell_list:
            if pos.X == x * 20 and pos.Y == y * 20:
                return pos

        return None

    def draw(self):
        for cells in self.cell_list:
            cells.draw()

    def update(self, x, y, color, border):
        self.current_cell = self.get(x, y)
        self.current_cell.Color = color
        self.current_cell.Border = border

mak = Grid.draw

mak