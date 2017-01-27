import pygame, globals, text, ships, time, playboard, players

pygame.init()

class Game:
    def __init__(self):

        self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
        self.ship1 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,4,3)
        self.ship2 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,4,3)
        self.ship3 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,4,3)
        self.ship4 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,4,3)
        self.ship5 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,4,3)
        self.ship6 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,4,3)
        self.ship7 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,4,3)
        self.ship8 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,4,3)
        self.shiplist = [self.ship1,self.ship2,self.ship3,self.ship4,self.ship5,self.ship6,self.ship7,self.ship8]
        self.player1 = players.Player("Player1",globals.green,globals.bright_green)
        self.player2 = players.Player("Player2",globals.red,globals.bright_red)
        self.shipxylist1 = []

   
    def game_loop(self):
        self.player1.Turn = True

        pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
        RUNNING, PAUSE = 0, 1
        state = RUNNING


        globals.gameDisplay.fill(globals.black)
        self.board.draw()
        pygame.display.update()
        shipcnt = 0

        shiplength = 0

        while self.player1.shipsplaced <4:
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                click = pygame.mouse.get_pressed()
            
                if click[0] == 1:
                    time.sleep(0.2)
                    mouse = pygame.mouse.get_pos()

                    if self.player1.shipsplaced == 0:
                        shiplength = 2
                    elif self.player1.shipsplaced == 1 or self.player1.shipsplaced == 2:
                        shiplength = 3
                    else:
                        shiplength = 4
                    
                    mousex1 = int(mouse[0]/20)
                    if mousex1 == self.shiplist[0].PosX or mousex1 == self.shiplist[1].PosX or mousex1 == self.shiplist[2].PosX or mousex1 == self.shiplist[3].PosX or mousex1 >= 20:
                        break
                    self.shiplist[self.player1.shipsplaced].PosX = mousex1
                    self.shiplist[self.player1.shipsplaced].ShipLength = shiplength
                    self.shiplist[self.player1.shipsplaced].PosY = 21 - shiplength
                    self.shiplist[self.player1.shipsplaced].draw()
                    self.player1.shipsplaced +=1
           
                

            self.board.draw()
            pygame.display.update()
            globals.clock.tick(60)
        while self.player2.shipsplaced <4:
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                click = pygame.mouse.get_pressed()
            
                if click[0] == 1:
                    time.sleep(0.2)
                    mouse = pygame.mouse.get_pos()

                    if self.player2.shipsplaced == 0:
                        shiplength = 2
                    elif self.player2.shipsplaced == 1 or self.player2.shipsplaced == 2:
                        shiplength = 3
                    else:
                        shiplength = 4
                    
                    mousex1 = int(mouse[0]/20)
                    if mousex1 == self.shiplist[4].PosX or mousex1 == self.shiplist[5].PosX or mousex1 == self.shiplist[6].PosX or mousex1 == self.shiplist[7].PosX or mousex1 >= 20:
                        break
                    self.shiplist[4+self.player2.shipsplaced].PosX = mousex1
                    self.shiplist[4+self.player2.shipsplaced].ShipLength = shiplength
                    self.shiplist[4+self.player2.shipsplaced].PosY = 1
                    self.shiplist[4+self.player2.shipsplaced].draw()


                    self.player2.shipsplaced +=1
                    
                

            self.board.draw()
            pygame.display.update()
            
            globals.clock.tick(60)    

        while self.player1.shipsplaced == 4 and self.player2.shipsplaced == 4:
            self.shipxylist1 =[]
            curshiplist = []

            for i in range(4):
                for c in range(self.shiplist[i].ShipLength):
                    self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                    self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
            if self.player1.Turn:
                self.shiplist[shipcnt].Color = self.player1.aColor
            else:
                self.shiplist[shipcnt].Color = self.player2.aColor
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if shipcnt < 3 and self.player1.Turn:
                            self.shiplist[shipcnt].Color = self.player1.iColor
                            shipcnt += 1
                            self.shiplist[shipcnt].Color = self.player1.aColor
                        elif shipcnt == 3 and self.player1.Turn:
                            self.shiplist[shipcnt].Color = self.player1.iColor
                            shipcnt = 0
                            self.shiplist[shipcnt].Color = self.player1.aColor
                        elif shipcnt <7 and self.player2.Turn:
                            self.shiplist[shipcnt].Color = self.player2.iColor
                            shipcnt += 1
                            self.shiplist[shipcnt].Color = self.player2.aColor
                        elif shipcnt == 7 and self.player2.Turn:
                            self.shiplist[shipcnt].Color = self.player2.iColor
                            shipcnt = 4
                            self.shiplist[shipcnt].Color = self.player2.aColor

                        
                    if event.key == pygame.K_p:
                        state = PAUSE
                    if event.key == pygame.K_u:
                        state = RUNNING
                    if event.key == pygame.K_t:
                        if self.player1.Turn:
                            self.player1.Turn = False
                            self.player2.Turn = True
                            self.shiplist[shipcnt].Color = self.player1.iColor
                            shipcnt = 4

                            print(self.player1.Turn, self.player2.Turn)    
                        else:
                            self.player1.Turn = True
                            self.player2.Turn = False
                            self.shiplist[shipcnt].Color = self.player2.iColor
                            shipcnt = 0
                            print(self.player1.Turn, self.player2.Turn)


                        
                    if event.key == pygame.K_LEFT:
                        self.shiplist[shipcnt].PosX += -1
                        for i in range(self.shiplist[shipcnt].ShipLength):
                            curshiplist = curshiplist + [(self.shiplist[shipcnt].PosX, self.shiplist[shipcnt].PosY +i)]
                        self.shiplist[shipcnt].PosX += 1

                        
                        if self.shiplist[shipcnt].PosX == 1: 
                            self.shiplist[shipcnt].PosX += 0
                        elif set(self.shipxylist1) & set(curshiplist) != set():
                            self.shiplist[shipcnt].PosX += 0
                        else:
                            self.shiplist[shipcnt].PosX += -1
                    if event.key == pygame.K_RIGHT:
                        self.shiplist[shipcnt].PosX += 1
                        for i in range(self.shiplist[shipcnt].ShipLength):
                            curshiplist = curshiplist + [(self.shiplist[shipcnt].PosX, self.shiplist[shipcnt].PosY +i)]
                        self.shiplist[shipcnt].PosX -= 1

                        if self.shiplist[shipcnt].PosX == 20:
                            self.shiplist[shipcnt].PosX += 0
                        elif set(self.shipxylist1) & set(curshiplist) != set():
                            self.shiplist[shipcnt].PosX += 0
                        else:
                            self.shiplist[shipcnt].PosX += 1
                    if event.key == pygame.K_UP:
                        self.shiplist[shipcnt].PosY += -1
                        curshiplist = [(self.shiplist[shipcnt].PosX, self.shiplist[shipcnt].PosY)]
                        self.shiplist[shipcnt].PosY += 1                      
                        if self.shiplist[shipcnt].PosY == 1: 
                            self.shiplist[shipcnt].PosY += 0
                        elif set(self.shipxylist1) & set(curshiplist) != set():
                            self.shiplist[shipcnt].PosY += 0
                        else:
                            self.shiplist[shipcnt].PosY += -1
                    if event.key == pygame.K_DOWN:
                        self.shiplist[shipcnt].PosY += 1
                        curshiplist = [(self.shiplist[shipcnt].PosX, (self.shiplist[shipcnt].PosY) + self.shiplist[shipcnt].ShipLength -1)]
                        self.shiplist[shipcnt].PosY += -1 

                        if self.shiplist[shipcnt].PosY == (21 - self.shiplist[shipcnt].ShipLength):
                            self.shiplist[shipcnt].PosY += 0
                        elif set(self.shipxylist1) & set(curshiplist) != set():
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
            text.button("Press >T< to end turn",575,25,200,50,globals.blue,globals.bright_blue,None)
            for x in range(0,8):
                self.shiplist[x].Board = self.board

                

            self.ship1 = self.shiplist[0]
            self.ship2 = self.shiplist[1]
            self.ship3 = self.shiplist[2]
            self.ship4 = self.shiplist[3]
            self.ship5 = self.shiplist[4]
            self.ship6 = self.shiplist[5]
            self.ship7 = self.shiplist[6]
            self.ship8 = self.shiplist[7]

            self.ship1.draw()
            self.ship2.draw()
            self.ship3.draw()
            self.ship4.draw()
            self.ship5.draw()
            self.ship6.draw()
            self.ship7.draw()
            self.ship8.draw()
            self.board.draw()

           
            pygame.display.update()
            globals.clock.tick(60)

def program():
    game = Game()
    game.game_loop()
