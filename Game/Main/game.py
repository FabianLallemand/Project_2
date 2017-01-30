import pygame, globals, text, ships, time, playboard, players


pygame.init()

class Game:
    def __init__(self):

        self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
        self.ship1 = ships.Ship(globals.green, 4, 0,1,2,3,self.board,2,2,[])
        self.ship2 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,3,3,[])
        self.ship3 = ships.Ship(globals.green, 4, 0,1,2,2,self.board,3,3,[])
        self.ship4 = ships.Ship(globals.green, 4, 0,1,2,1,self.board,4,4,[])
        self.ship5 = ships.Ship(globals.red, 4, 0,1,2,3,self.board,2,2,[])
        self.ship6 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,3,3,[])
        self.ship7 = ships.Ship(globals.red, 4, 0,1,2,2,self.board,3,3,[])
        self.ship8 = ships.Ship(globals.red, 4, 0,1,2,1,self.board,4,4,[])
        self.shiplist = [self.ship1,self.ship2,self.ship3,self.ship4,self.ship5,self.ship6,self.ship7,self.ship8]
        self.player1 = players.Player("Player1",globals.green,globals.bright_green)
        self.player2 = players.Player("Player2",globals.red,globals.bright_red)
        self.shipxylist1 = []
        self.curshiplist = []
        self.shipcnt = 0    
        self.shipsinrange = []
        self.firecnt = 0
        self.damageship = 0
        self.deadships = []
        self.GameStopped = False

        #Database connections opzetten
       # self.db = mysql.connect(user='battleport', password='ditiseengeheim', database='highscores')
        #self.cursor = db.cursor()

    def shipswitch(self):
        if self.shipcnt < 3 and self.player1.Turn:
            self.shiplist[self.shipcnt].Color = self.player1.iColor
            self.shipcnt += 1
            self.shiplist[self.shipcnt].Color = self.player1.aColor
        elif self.shipcnt == 3 and self.player1.Turn:
            self.shiplist[self.shipcnt].Color = self.player1.iColor
            self.shipcnt = 0
            self.shiplist[self.shipcnt].Color = self.player1.aColor
        elif self.shipcnt <7 and self.player2.Turn:
            self.shiplist[self.shipcnt].Color = self.player2.iColor
            self.shipcnt += 1
            self.shiplist[self.shipcnt].Color = self.player2.aColor
        elif self.shipcnt == 7 and self.player2.Turn:
            self.shiplist[self.shipcnt].Color = self.player2.iColor
            self.shipcnt = 4
            self.shiplist[self.shipcnt].Color = self.player2.aColor

        if self.shipcnt in self.deadships:
            self.shipswitch()

    def turn(self):
        for x in range(0,8):
            self.shiplist[x].Shots = 1
        if self.player1.Turn:
            self.player1.Turn = False
            self.player2.Turn = True
            self.shiplist[self.shipcnt].Color = self.player1.iColor
            self.shipcnt = 4
            self.ship1.Steps = 3
            self.ship2.Steps = 2
            self.ship3.Steps = 2
            self.ship4.Steps = 1
            self.player1.Shots = 2
            if self.shipcnt in self.deadships:
                self.shipswitch()

  
        else:
            self.player1.Turn = True
            self.player2.Turn = False
            self.shiplist[self.shipcnt].Color = self.player2.iColor
            self.shipcnt = 0
            self.ship5.Steps = 3
            self.ship6.Steps = 2
            self.ship7.Steps = 2
            self.ship8.Steps = 1
            self.player2.Shots = 2
            if self.shipcnt in self.deadships:
                self.shipswitch()


    def fire(self):
        if ((self.player1.Turn and self.player1.Shots != 0) or (self.player2.Turn and self.player2.Shots != 0)) and self.shiplist[self.shipcnt].Shots != 0:

            self.firecnt = 0
            fbuty = 100
            for i in range(self.shiplist[self.shipcnt].ShipLength):
                for x in range(1, 1 + self.shiplist[self.shipcnt].ShipLength):
                    self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX + x, self.shiplist[self.shipcnt].PosY +i)] + [(self.shiplist[self.shipcnt].PosX - x, self.shiplist[self.shipcnt].PosY +i)]

                self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY + self.shiplist[self.shipcnt].ShipLength+i)] + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY -1 - i)]
            if self.player1.Turn:
                self.firecnt += 4
            if set(self.shiplist[self.firecnt].XYlist +self.shiplist[self.firecnt+1].XYlist +self.shiplist[self.firecnt+2].XYlist +self.shiplist[self.firecnt+3].XYlist) & set(self.curshiplist) != set():
                if set(self.shiplist[self.firecnt].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt].Health > 0:
                    self.shipsinrange = self.shipsinrange + [self.firecnt]
                    fbuty += 60
                if set(self.shiplist[self.firecnt+1].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+1].Health > 0:
                    self.shipsinrange = self.shipsinrange + [self.firecnt + 1]

                    fbuty += 60
                if set(self.shiplist[self.firecnt+2].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+2].Health > 0:
                    self.shipsinrange = self.shipsinrange + [self.firecnt + 2]

                    fbuty += 60
                if set(self.shiplist[self.firecnt+3].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+3].Health > 0:
                    self.shipsinrange = self.shipsinrange + [self.firecnt + 3]

            pygame.display.update()
            self.curshiplist = []
        
    def damage(self):
        self.shipsinrange = []
        self.shiplist[self.damageship].Health -= 1
        if self.player1.Turn:
            self.player1.Shots -= 1
        if self.player2.Turn:
            self.player2.Shots -= 1
        self.shiplist[self.shipcnt].Shots -= 1


    def game_loop(self):
        self.player1.Turn = True

        pause_text = pygame.font.SysFont('freesansbold.ttf', 50).render('Paused', True, globals.white)
        RUNNING, PAUSE = 0, 1
        state = RUNNING


        globals.gameDisplay.fill(globals.black)
        self.board.draw()
        pygame.display.update()
        self.shipcnt = 0

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
                    if mousex1 == self.shiplist[0].PosX or mousex1 == self.shiplist[1].PosX or mousex1 == self.shiplist[2].PosX or mousex1 == self.shiplist[3].PosX or mousex1 >= 21:
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
                    if mousex1 == self.shiplist[4].PosX or mousex1 == self.shiplist[5].PosX or mousex1 == self.shiplist[6].PosX or mousex1 == self.shiplist[7].PosX or mousex1 >= 21:
                        break
                    self.shiplist[4+self.player2.shipsplaced].PosX = mousex1
                    self.shiplist[4+self.player2.shipsplaced].ShipLength = shiplength
                    self.shiplist[4+self.player2.shipsplaced].PosY = 1
                    self.shiplist[4+self.player2.shipsplaced].draw()


                    self.player2.shipsplaced +=1
                    
                

            self.board.draw()
            pygame.display.update()
            
            globals.clock.tick(60)    
            
        while self.player1.shipsplaced == 4 and self.player2.shipsplaced == 4 and not(self.GameStopped):
            #self.deadships = []
            self.shipxylist1 =[]
            self.curshiplist = []
            for x in range(0,8):
                self.shiplist[x].XYlist = []
            for i in range(4):
                for c in range(self.shiplist[i].ShipLength):
                    self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                    self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                    self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                    self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]

            if self.player1.Turn:
                self.shiplist[self.shipcnt].Color = self.player1.aColor
            else:
                self.shiplist[self.shipcnt].Color = self.player2.aColor
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.shipswitch()


                    if event.key == pygame.K_f:
                        self.fire()
                    if event.key == pygame.K_p:
                        state = PAUSE
                    if event.key == pygame.K_u:
                        state = RUNNING
                    if event.key == pygame.K_t:
                        self.turn()

                        
                    if event.key == pygame.K_LEFT:
                        if self.shiplist[self.shipcnt].Steps == 0:
                            break
                        self.shiplist[self.shipcnt].PosX += -1
                        for i in range(self.shiplist[self.shipcnt].ShipLength):
                            self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY +i)]
                        self.shiplist[self.shipcnt].PosX += 1

                        
                        if self.shiplist[self.shipcnt].PosX == 1: 
                            self.shiplist[self.shipcnt].PosX += 0
                        elif set(self.shipxylist1) & set(self.curshiplist) != set():
                            self.shiplist[self.shipcnt].PosX += 0
                        else:
                            self.shiplist[self.shipcnt].PosX += -1
                            self.shiplist[self.shipcnt].Steps -=1
                    if event.key == pygame.K_RIGHT:
                        if self.shiplist[self.shipcnt].Steps == 0:
                            break
                        self.shiplist[self.shipcnt].PosX += 1
                        
                        for i in range(self.shiplist[self.shipcnt].ShipLength):
                            self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY +i)]
                        self.shiplist[self.shipcnt].PosX -= 1

                        if self.shiplist[self.shipcnt].PosX == 20:
                            self.shiplist[self.shipcnt].PosX += 0
                        elif set(self.shipxylist1) & set(self.curshiplist) != set():
                            self.shiplist[self.shipcnt].PosX += 0
                        else:
                            self.shiplist[self.shipcnt].PosX += 1
                            self.shiplist[self.shipcnt].Steps -=1
                    if event.key == pygame.K_UP:
                        if self.shiplist[self.shipcnt].Steps == 0:
                            break
                        self.shiplist[self.shipcnt].PosY += -1
                        self.curshiplist = [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY)]
                        self.shiplist[self.shipcnt].PosY += 1                      
                        if self.shiplist[self.shipcnt].PosY == 1: 
                            self.shiplist[self.shipcnt].PosY += 0
                        elif set(self.shipxylist1) & set(self.curshiplist) != set():
                            self.shiplist[self.shipcnt].PosY += 0
                        else:
                            self.shiplist[self.shipcnt].PosY += -1
                            self.shiplist[self.shipcnt].Steps -=1
                    if event.key == pygame.K_DOWN:
                        if self.shiplist[self.shipcnt].Steps == 0:
                            break
                        self.shiplist[self.shipcnt].PosY += 1
                        self.curshiplist = [(self.shiplist[self.shipcnt].PosX, (self.shiplist[self.shipcnt].PosY) + self.shiplist[self.shipcnt].ShipLength -1)]
                        self.shiplist[self.shipcnt].PosY += -1 

                        if self.shiplist[self.shipcnt].PosY == (21 - self.shiplist[self.shipcnt].ShipLength):
                            self.shiplist[self.shipcnt].PosY += 0
                        elif set(self.shipxylist1) & set(self.curshiplist) != set():
                            self.shiplist[self.shipcnt].PosY += 0
                        else:
                            self.shiplist[self.shipcnt].PosY += 1
                            self.shiplist[self.shipcnt].Steps -=1
                          
                while state == PAUSE:
                    globals.gameDisplay.blit(pause_text,(300,300))
                    pygame.display.flip()
                    globals.clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_u: state = RUNNING
                  
            
            globals.gameDisplay.fill(globals.black)
            self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
            text.button("Press >T< to end turn",575,25,200,50,globals.blue,globals.bright_blue,self.turn)
            fbuty = 100
            if self.firecnt in self.shipsinrange:
                self.damageship = 0 + self.firecnt
                text.button("Ship 1",575,fbuty,100,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60
            if self.firecnt+1 in self.shipsinrange:
                self.damageship = 1 + self.firecnt
                text.button("Ship 2",575,fbuty,100,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60
            if self.firecnt+2 in self.shipsinrange:
                self.damageship = 2 + self.firecnt
                text.button("Ship 3",575,fbuty,100,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60
            if self.firecnt +3 in self.shipsinrange:
                self.damageship = 3 + self.firecnt  
                text.button("Ship 4",575,fbuty,100,50,globals.blue,globals.bright_blue,self.damage)
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

            self.deadships = []

            if self.ship1.Health <= 0:
                self.ship1.Color = globals.brown
                self.deadships = self.deadships + [0]

            if self.ship2.Health <= 0:
                self.ship2.Color = globals.brown
                self.deadships = self.deadships + [1]

            if self.ship3.Health <= 0:
                self.ship3.Color = globals.brown
                self.deadships = self.deadships + [2]

            if self.ship4.Health <= 0:
                self.ship4.Color = globals.brown
                self.deadships = self.deadships + [3]

            if self.ship5.Health <= 0:
                self.ship5.Color = globals.brown
                self.deadships = self.deadships + [4]

            if self.ship6.Health <= 0:
                self.ship6.Color = globals.brown
                self.deadships = self.deadships + [5]

            if self.ship7.Health <= 0:
                self.ship7.Color = globals.brown
                self.deadships = self.deadships + [6]

            if self.ship8.Health <= 0:
                self.ship8.Color = globals.brown
                self.deadships = self.deadships + [7]


            if self.ship1.Health == 0 and self.ship2.Health == 0 and self.ship3.Health == 0 and self.ship4.Health == 0:
                print("Player2 wins")
                self.GameStopped = True
            elif self.ship5.Health == 0 and self.ship6.Health == 0 and self.ship7.Health == 0 and self.ship8.Health == 0:
                print("Player1 wins")
                self.GameStopped = True






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
