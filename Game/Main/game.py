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
        

    def game_loop(self):
        time.sleep(0.1)
        s1 = True
        s2 = False
        pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
        RUNNING, PAUSE = 0, 1
        state = RUNNING

        gameExit = False
        gameExit2 = False
        globals.gameDisplay.fill(globals.black)
        self.board.draw()
        pygame.display.update()
        shiplength1 = 5
        shiplength2 = 3
        while not gameExit and self.shipsplaced <2:
        

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
                    #print("schip plaatsen")
                    mouse = pygame.mouse.get_pos()
                    
                    #print(mousex)
                    if self.shipsplaced == 0:
                        mousex1 = int(mouse[0]/20)
                        shipy1 = 21 - shiplength1
                        self.ship1  = ships.Ship(globals.green, shiplength1, mousex1,shipy1, 2, 1, self.board, 1,3)
                        self.ship1.draw()
                    if self.shipsplaced == 1:
                        mousex2 = int(mouse[0]/20)
                        shipy2 = 21 - shiplength2
                        self.ship2  = ships.Ship(globals.green, shiplength2, mousex2,shipy2, 2, 1, self.board, 1,3)
                        self.ship2.draw()
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


        while self.shipsplaced == 2:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if s1 and not s2:
                            s1 = False
                            s2 = True
                        elif not s1 and s2:
                            s1 = True
                            s2 = False
                        
                    if event.key == pygame.K_p:
                        state = PAUSE
                    if event.key == pygame.K_u:
                        state = RUNNING

                    if s1 == True:
                        if event.key == pygame.K_LEFT:
                            if mousex1 == 1: 
                                mousex1 += 0
                            else:
                                mousex1 += -1
                        if event.key == pygame.K_RIGHT:
                            if mousex1 == 20:
                                mousex1 += 0
                            else:
                                mousex1 += 1
                        if event.key == pygame.K_UP:
                            if shipy1 == 1:
                                shipy1 += 0
                            else:
                               shipy1 += -1
                        if event.key == pygame.K_DOWN:
                            if shipy1 == (21 -shiplength1):
                                shipy1 += 0
                            else:
                                shipy1 += 1
                    if s2 == True:
                        if event.key == pygame.K_LEFT:
                            if mousex2 == 1: 
                                mousex2 += 0
                            else:
                                mousex2 += -1
                        if event.key == pygame.K_RIGHT:
                            if mousex2 == 20:
                                mousex2 += 0
                            else:
                                mousex2 += 1
                        if event.key == pygame.K_UP:
                            if shipy2 == 1:
                                shipy2 += 0
                            else:
                               shipy2 += -1
                        if event.key == pygame.K_DOWN:
                            if shipy2 == (21 -shiplength2):
                                shipy2 += 0
                            else:
                                shipy2 += 1                            

                while state == PAUSE:
                    globals.gameDisplay.blit(pause_text,(300,300))
                    pygame.display.flip()
                    globals.clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_u: state = RUNNING
                 

            globals.gameDisplay.fill(globals.black)
            self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
            self.ship1  = ships.Ship(globals.green, shiplength1, mousex1,shipy1, 2, 1, self.board, 1,3)
            self.ship2  = ships.Ship(globals.green, shiplength2, mousex2,shipy2, 2, 1, self.board, 1,3)
            self.ship1.draw()
            self.ship2.draw()
            self.board.draw()
        
            pygame.display.update()
            globals.clock.tick(60)

def program():
    game = Game()
    game.game_loop()
