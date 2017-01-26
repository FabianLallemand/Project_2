import pygame, globals, text, ships, time, playboard

pygame.init()

class Game:
    def __init__(self):
        self.shipsplaced = 0
        self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
        self.ship1 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship2 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship3 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship4 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship5 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship6 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship7 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.ship8 = ships.Ship(globals.green, 4, 2,1,2,2,self.board,4,3)
        self.shiplist = [self.ship1,self.ship2,self.ship3,self.ship4,self.ship5,self.ship6,self.ship7,self.ship8]

    def game_loop(self):
        time.sleep(0.1)

        pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
        RUNNING, PAUSE = 0, 1
        state = RUNNING

        gameExit = False

        globals.gameDisplay.fill(globals.black)
        self.board.draw()
        pygame.display.update()
        shipcnt = 0

        shiplength = 0

        while not gameExit and self.shipsplaced <4:
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: state = PAUSE
                    if event.key == pygame.K_u: state = RUNNING

                click = pygame.mouse.get_pressed()
            
                if click[0] == 1:
                    time.sleep(0.2)
                    mouse = pygame.mouse.get_pos()
                    if self.shipsplaced == 0:
                        shiplength = 2
                    elif self.shipsplaced == 1 or self.shipsplaced == 2:
                        shiplength = 3
                    else:
                        shiplength = 4

                    mousex1 = int(mouse[0]/20)
                    self.shiplist[self.shipsplaced].PosX = mousex1
                    self.shiplist[self.shipsplaced].ShipLength = shiplength
                    self.shiplist[self.shipsplaced].PosY = 21 - shiplength
                    self.shiplist[self.shipsplaced].draw()


                    self.shipsplaced +=1
                    time.sleep(0.2)              
                

                while state == PAUSE:
                    globals.gameDisplay.blit(pause_text,(300,300))
                    pygame.display.flip()
                    globals.clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_u: state = RUNNING

            self.board.draw()
            pygame.display.update()
            globals.clock.tick(60)
            

        while self.shipsplaced == 4:

            self.shiplist[shipcnt].Color = globals.bright_green
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if shipcnt < 3:
                            self.shiplist[shipcnt].Color = globals.green
                            shipcnt += 1
                            self.shiplist[shipcnt].Color = globals.bright_green
                        else:
                            self.shiplist[shipcnt].Color = globals.green
                            shipcnt = 0
                            self.shiplist[shipcnt].Color = globals.bright_green

                        
                    if event.key == pygame.K_p:
                        state = PAUSE
                    if event.key == pygame.K_u:
                        state = RUNNING

                    
                    if event.key == pygame.K_LEFT:
                        if self.shiplist[shipcnt].PosX == 1: 
                            self.shiplist[shipcnt].PosX += 0
                        else:
                            self.shiplist[shipcnt].PosX += -1
                    if event.key == pygame.K_RIGHT:
                        if self.shiplist[shipcnt].PosX == 20:
                            self.shiplist[shipcnt].PosX += 0
                        else:
                            self.shiplist[shipcnt].PosX += 1
                    if event.key == pygame.K_UP:
                        if self.shiplist[shipcnt].PosY == 1:
                            self.shiplist[shipcnt].PosY += 0
                        else:
                            self.shiplist[shipcnt].PosY += -1
                    if event.key == pygame.K_DOWN:
                        if self.shiplist[shipcnt].PosY == (21 - self.shiplist[shipcnt].ShipLength):
                            self.shiplist[shipcnt].PosY += 0
                        else:
                            self.shiplist[shipcnt].PosY += 1
                          
                while state == PAUSE:
                    globals.gameDisplay.blit(pause_text,(300,300))
                    pygame.display.flip()
                    globals.clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_u: state = RUNNING
                  

            globals.gameDisplay.fill(globals.black)
            self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
            for x in range(0,8):
                self.shiplist[x].Board = self.board

            self.ship1 = self.shiplist[0]
            self.ship2 = self.shiplist[1]
            self.ship3 = self.shiplist[2]
            self.ship4 = self.shiplist[3]

            self.ship1.draw()
            self.ship2.draw()
            self.ship3.draw()
            self.ship4.draw()
            self.board.draw()
        
            pygame.display.update()
            globals.clock.tick(60)

def program():
    game = Game()
    game.game_loop()
