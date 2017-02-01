import pygame, globals, text, ships, time, playboard, players, random, cards, cardfunctions, mysql


pygame.init()

class Game:
    def __init__(self):

        self.board = playboard.Grid(globals.gameDisplay, globals.white,1)
        self.ship1 = ships.Ship(globals.white, 4, -1,1,0,3,self.board,2,2,[],"Furgo Saltire",True)
        self.ship2 = ships.Ship(globals.white, 4, -1,1,1,2,self.board,3,3,[],"Silver Whisper",True)
        self.ship3 = ships.Ship(globals.white, 4, -1,1,1,2,self.board,3,3,[],"Windsurf",True)
        self.ship4 = ships.Ship(globals.white, 4, -1,1,1,1,self.board,4,4,[],"Merapi",True)
        self.ship5 = ships.Ship(globals.white, 4, -1,1,0,3,self.board,2,2,[],"Santa Bettina",True)
        self.ship6 = ships.Ship(globals.white, 4, -1,1,1,2,self.board,3,3,[],"Sea Spirit",True)
        self.ship7 = ships.Ship(globals.white, 4, -1,1,1,2,self.board,3,3,[],"Intensity",True)
        self.ship8 = ships.Ship(globals.white, 4, -1,1,1,1,self.board,4,4,[],"Amadea",True)


        self.shiplist = [self.ship1,self.ship2,self.ship3,self.ship4,self.ship5,self.ship6,self.ship7,self.ship8]
        self.player1 = players.Player("Player1",globals.white,globals.white)
        self.player2 = players.Player("Player2",globals.white,globals.white)
        
        self.shipxylist1 = [] 
        self.curshiplist = []
        self.shipcnt = 0    
        self.shipsinrange = []
        self.firecnt = 0
        self.damageship = 0 
        self.deadships = []
        self.GameStopped = False
        self.attackcnt = 0

        self.index = 0


        #offensieve kaarten
        self.card1 = cards.Cards("FMJ Upgrade",self.FMJ)
        self.card2 = cards.Cards("Rifling",self.Rifling)
        self.card3 = cards.Cards("Adv Rifling",self.advRifling)
        self.card4 = cards.Cards("Naval Mine",self.FMJ)
        self.card5 = cards.Cards("EMP Upgrade",self.FMJ)

        #defensieve cards
        self.card6 = cards.Cards("Hull",self.Hull)
        self.card7 = cards.Cards("Sonar",self.FMJ)
        self.card8 = cards.Cards("Smokescreen",self.FMJ)
        self.card9 = cards.Cards("Sabotage",self.FMJ)

        #Helpende cards
        self.card10 = cards.Cards("Backup",self.Backup)
        self.card11 = cards.Cards("Extrafuel2",self.Extrafuel2)
        self.card12 = cards.Cards("Extrafuel",self.Extrafuel)
        self.card13 = cards.Cards("Rally",self.Rally)
        self.card14 = cards.Cards("Adr. Rush",self.Adrenaline)

        #speciale cards
        self.card15 = cards.Cards("Repair",self.FMJ)
        self.card16 = cards.Cards("Flak Armor",self.FMJ)
        self.card17 = cards.Cards("Hack Intel",self.FMJ)
        self.card18 = cards.Cards("Far Sight",self.FMJ)
        self.card19 = cards.Cards("Allu. Hull",self.FMJ)
        self.card20 = cards.Cards("J. Sparrow",self.FMJ)

        self.cardlist2 = [self.card1] * 2 + [self.card2] * 2 + [self.card3] * 2 + [self.card4] * 6 + [self.card5] * 4 + [self.card6] * 2 + [self.card7] * 4 + [self.card8] * 2 + [self.card9] * 2 + [self.card10] * 2 + [self.card11] * 4 + [self.card12] * 6 + [self.card13] * 1 + [self.card14] * 4
        self.cardlist = [self.card1] * 2 + [self.card2] * 2 + [self.card3] * 2 + [self.card6] * 2 + [self.card10] * 2 + [self.card11] * 4 + [self.card12] * 6 + [self.card13] * 1 + [self.card14] * 4
        
        self.cardimglist2 = [globals.fmjupgrade] * 2 + [globals.rifling] * 2 + [globals.advancedrifling] * 2 + [globals.navalmine] * 6 + [globals.emp] * 4 + [globals.hull] * 2 + [globals.sonar] * 4 + [globals.smokescreen] * 2 + [globals.sabotage] * 2 + [globals.backup] * 2 + [globals.extrafuel2] * 4 + [globals.extrafuel] * 6 + [globals.rally] * 1 + [globals.adrenalinerush] * 4
        self.cardimglist = [globals.fmjupgrade] * 2 + [globals.rifling] * 2 + [globals.advancedrifling] * 2 + [globals.hull] * 2 + [globals.backup] * 2 + [globals.extrafuel2] * 4 + [globals.extrafuel] * 6 + [globals.rally] * 1 + [globals.adrenalinerush] * 4
        
        self.cardused = False


    def shiprotate(self):
        if self.firecnt == 0 and self.shiplist[self.shipcnt].Steps > 0:
            if self.shiplist[self.shipcnt].Offensive:
                self.shiplist[self.shipcnt].PosX -= self.shiplist[self.shipcnt].Middle
                self.shiplist[self.shipcnt].PosY += self.shiplist[self.shipcnt].Middle

                if self.shiplist[self.shipcnt].PosX + self.shiplist[self.shipcnt].ShipLength <= 21 and self.shiplist[self.shipcnt].PosX > 0:
                    for i in range(self.shiplist[self.shipcnt].ShipLength):
                        self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX + i, self.shiplist[self.shipcnt].PosY)]
                    self.shiplist[self.shipcnt].PosX += self.shiplist[self.shipcnt].Middle
                    self.shiplist[self.shipcnt].PosY -= self.shiplist[self.shipcnt].Middle
                    if set(self.shipxylist1) & set(self.curshiplist) == set():
                        self.shiplist[self.shipcnt].Offensive = False
                        self.shiplist[self.shipcnt].Range += 1
                        self.shiplist[self.shipcnt].Steps -= 1
                        self.shiplist[self.shipcnt].PosX -= self.shiplist[self.shipcnt].Middle
                        self.shiplist[self.shipcnt].PosY += self.shiplist[self.shipcnt].Middle
                else:
                    self.shiplist[self.shipcnt].PosX += self.shiplist[self.shipcnt].Middle
                    self.shiplist[self.shipcnt].PosY -= self.shiplist[self.shipcnt].Middle

            else:
                self.shiplist[self.shipcnt].PosX += self.shiplist[self.shipcnt].Middle
                self.shiplist[self.shipcnt].PosY -= self.shiplist[self.shipcnt].Middle
                for i in range(self.shiplist[self.shipcnt].ShipLength):
                    self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY + i)]
                self.shiplist[self.shipcnt].PosX -= self.shiplist[self.shipcnt].Middle
                self.shiplist[self.shipcnt].PosY += self.shiplist[self.shipcnt].Middle
                if set(self.shipxylist1) & set(self.curshiplist) == set():
                    self.shiplist[self.shipcnt].Offensive = True
                    self.shiplist[self.shipcnt].Range -= 1
                    self.shiplist[self.shipcnt].Steps -= 1
                    self.shiplist[self.shipcnt].PosX += self.shiplist[self.shipcnt].Middle
                    self.shiplist[self.shipcnt].PosY -= self.shiplist[self.shipcnt].Middle

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
        if self.firecnt == 0:
            for x in range(0,8):
                self.shiplist[x].Shots = 1
                self.shiplist[x].Damage = 1
            
        
            if self.player1.Turn:
                self.player1.Turn = False
                self.player2.Turn = True
                self.shiplist[self.shipcnt].Color = self.player1.iColor
                self.shipcnt = 4
                self.ship1.Steps = 3
                self.ship2.Steps = 2
                self.ship3.Steps = 2
                self.ship4.Steps = 1
                self.ship1.Range = 2
                self.ship2.Range = 3
                self.ship3.Range = 3
                self.ship4.Range = 4
                for i in range(4,8):
                    if not self.shiplist[i].Offensive:
                        self.shiplist[i].Range += 1
                self.player1.Shots = 2
                if self.shipcnt in self.deadships:
                    self.shipswitch()
            
                if len(self.cardlist) != 0:
                    if len(self.player2.Cards)+ 1 < 7:
                        index = random.randint(0,len(self.cardlist)-1)
                        card = self.cardlist[index]
                        cardimg = self.cardimglist[index]
                        self.player2.Cards.append(card)
                        self.player2.Cardimg.append(cardimg)
                        self.cardlist.pop(index)
                        self.cardimglist.pop(index)
            




  
            else:
                self.player1.Turn = True
                self.player2.Turn = False
                self.shiplist[self.shipcnt].Color = self.player2.iColor
                self.shipcnt = 0
                self.ship5.Steps = 3
                self.ship6.Steps = 2
                self.ship7.Steps = 2
                self.ship8.Steps = 1
                self.ship5.Range = 2
                self.ship6.Range = 3
                self.ship7.Range = 3
                self.ship8.Range = 4
                for i in range(0,4):
                    if not self.shiplist[i].Offensive:
                        self.shiplist[i].Range += 1
                self.player2.Shots = 2

                if len(self.cardlist) != 0:
                    if len(self.player1.Cards)+ 1 < 7:
                        index = random.randint(0,len(self.cardlist)-1)
                        card = self.cardlist[index]
                        cardimg = self.cardimglist[index]
                        self.player1.Cards.append(card)
                        self.player1.Cardimg.append(cardimg)
                        self.cardlist.pop(index)
                        self.cardimglist.pop(index)


                if self.shipcnt in self.deadships:
                    self.shipswitch()
                
    def fire(self):
        if self.attackcnt == 0:
            if ((self.player1.Turn and self.player1.Shots != 0) or (self.player2.Turn and self.player2.Shots != 0)) and self.shiplist[self.shipcnt].Shots != 0:
                self.curshiplist = []
                self.firecnt = 0
                if self.shiplist[self.shipcnt].Offensive:
                    for i in range(self.shiplist[self.shipcnt].ShipLength):
                        for x in range(1, 1 + self.shiplist[self.shipcnt].Range):
                            self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX + x, self.shiplist[self.shipcnt].PosY +i)] + [(self.shiplist[self.shipcnt].PosX - x, self.shiplist[self.shipcnt].PosY +i)]
                        self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY + self.shiplist[self.shipcnt].ShipLength+i)] + [(self.shiplist[self.shipcnt].PosX, self.shiplist[self.shipcnt].PosY -1 - i)]
            
                else:
                    for i in range(self.shiplist[self.shipcnt].ShipLength):
                        for x in range(1, 1 + self.shiplist[self.shipcnt].Range):
                            self.curshiplist = self.curshiplist + [(self.shiplist[self.shipcnt].PosX + i, self.shiplist[self.shipcnt].PosY +x)] + [(self.shiplist[self.shipcnt].PosX + i, self.shiplist[self.shipcnt].PosY -x)]
                  
                        
                if self.player1.Turn:
                    self.firecnt += 4
                if set(self.shiplist[self.firecnt].XYlist +self.shiplist[self.firecnt+1].XYlist +self.shiplist[self.firecnt+2].XYlist +self.shiplist[self.firecnt+3].XYlist) & set(self.curshiplist) != set():
                    if set(self.shiplist[self.firecnt].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt].Health > 0:
                        self.shipsinrange = self.shipsinrange + [self.firecnt]
                        self.attackcnt += 1
                    if set(self.shiplist[self.firecnt+1].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+1].Health > 0:
                        self.shipsinrange = self.shipsinrange + [self.firecnt + 1]
                        self.attackcnt += 1
                    if set(self.shiplist[self.firecnt+2].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+2].Health > 0:
                        self.shipsinrange = self.shipsinrange + [self.firecnt + 2]
                        self.attackcnt += 1
                    if set(self.shiplist[self.firecnt+3].XYlist) & set(self.curshiplist) != set() and self.shiplist[self.firecnt+3].Health > 0:
                        self.shipsinrange = self.shipsinrange + [self.firecnt + 3]
                        self.attackcnt += 1
                if self.attackcnt == 0:
                    self.firecnt = 0
                pygame.display.update()
                self.curshiplist = []
        
    def damage(self):
        self.shipsinrange = []
        self.shiplist[self.damageship].Health -= self.shiplist[self.shipcnt].Damage
        if self.player1.Turn:
            self.player1.Shots -= 1
        if self.player2.Turn:
            self.player2.Shots -= 1
        self.shiplist[self.shipcnt].Shots -= 1
        self.firecnt = 0
        self.attackcnt = 0
        self.damageship = 0
        self.shiplist[self.shipcnt].Damage = 1
        (globals.Explosionfx).play()
        
        
        
    def FMJ(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Damage += 1
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)

    def Rifling(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Range += 1
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
        
    def advRifling(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Range += 2
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
        
    def Hull(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Health += 1
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
           
    def Backup(self):
        self.cardused = True

        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)
            for i in range(0,2):
                if len(self.cardlist) != 0:
                    if len(self.player1.Cards)+ 1 < 7:
                        index = random.randint(0,len(self.cardlist)-1)
                        card = self.cardlist[index]
                        cardimg = self.cardimglist[index]
                        self.player1.Cards.append(card)
                        self.player1.Cardimg.append(cardimg)
                        self.cardlist.pop(index)
                        self.cardimglist.pop(index) 
        if self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
            for i in range(0,2):
                if len(self.cardlist) != 0:
                    if len(self.player2.Cards)+ 1 < 7:
                        index = random.randint(0,len(self.cardlist)-1)
                        card = self.cardlist[index]
                        cardimg = self.cardimglist[index]
                        self.player2.Cards.append(card)
                        self.player2.Cardimg.append(cardimg)
                        self.cardlist.pop(index)
                        self.cardimglist.pop(index)

    def Extrafuel2(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Steps += 2
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)

    def Extrafuel(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Steps += 1
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
    
    def Rally(self):
        self.cardused = True
        
        if self.player1.Turn:
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)
            for i in range(0,4):
                self.shiplist[i].Steps += 1

        elif self.player2.Turn:
            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
            for i in range(4,8):
                self.shiplist[i].Steps += 1

    def Adrenaline(self):
        self.cardused = True
        self.shiplist[self.shipcnt].Steps += 1
        if self.player1.Turn:
            if self.shipcnt == 0:
                self.shiplist[self.shipcnt].Steps = 3
            if self.shipcnt == 1:
                self.shiplist[self.shipcnt].Steps = 2
            if self.shipcnt == 2:
                self.shiplist[self.shipcnt].Steps = 2
            if self.shipcnt == 3:
                self.shiplist[self.shipcnt].Steps = 1
            
            self.player1.Cards.pop(self.index)
            self.player1.Cardimg.pop(self.index)

        elif self.player2.Turn:
            if self.shipcnt == 4:
                self.shiplist[self.shipcnt].Steps = 3
            if self.shipcnt == 5:
                self.shiplist[self.shipcnt].Steps = 2
            if self.shipcnt == 6:
                self.shiplist[self.shipcnt].Steps = 2
            if self.shipcnt == 7:
                self.shiplist[self.shipcnt].Steps = 1

            self.player2.Cards.pop(self.index)
            self.player2.Cardimg.pop(self.index)
   
    def game_loop(self):
        
        for x in range(0,2):
            index = random.randint(0,len(self.cardlist)-1)
            card = self.cardlist[index]
            cardimg = self.cardimglist[index]
            self.player1.Cards.append(card)
            self.player1.Cardimg.append(cardimg)
            self.cardlist.pop(index)
            self.cardimglist.pop(index)

            index = random.randint(0,len(self.cardlist)-1)
            card = self.cardlist[index]
            cardimg = self.cardimglist[index]
            self.player2.Cards.append(card)
            self.player2.Cardimg.append(cardimg)
            self.cardlist.pop(index)
            self.cardimglist.pop(index)



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
                    #(globals.Blopfx).play()

                    if self.player1.shipsplaced == 0:
                        shiplength = 2
                    elif self.player1.shipsplaced == 1 or self.player1.shipsplaced == 2:
                        shiplength = 3
                    else:
                        shiplength = 4
                    
                    mousex = int(mouse[0]/20)
                    if mousex == self.shiplist[0].PosX or mousex == self.shiplist[1].PosX or mousex == self.shiplist[2].PosX or mousex == self.shiplist[3].PosX or mousex >= 21:
                        break
                    self.shiplist[self.player1.shipsplaced].PosX = mousex
                    self.shiplist[self.player1.shipsplaced].ShipLength = shiplength
                    self.shiplist[self.player1.shipsplaced].PosY = 21 - shiplength
                    self.shiplist[self.player1.shipsplaced].draw()
                    self.player1.shipsplaced +=1
                    
                    
                    
            self.board.draw()

            globals.gameDisplay.blit(globals.boot1off, (self.ship1.PosX * 20,self.ship1.PosY * 20))

            globals.gameDisplay.blit(globals.boot3off, (self.ship2.PosX * 20,self.ship2.PosY * 20))

            globals.gameDisplay.blit(globals.boot3off, (self.ship3.PosX * 20,self.ship3.PosY * 20))
 
            globals.gameDisplay.blit(globals.boot4off, (self.ship4.PosX * 20,self.ship4.PosY * 20))

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
                    
                    mousex = int(mouse[0]/20)
                    if mousex == self.shiplist[4].PosX or mousex == self.shiplist[5].PosX or mousex == self.shiplist[6].PosX or mousex == self.shiplist[7].PosX or mousex >= 21:
                        break
                    self.shiplist[4+self.player2.shipsplaced].PosX = mousex
                    self.shiplist[4+self.player2.shipsplaced].ShipLength = shiplength
                    self.shiplist[4+self.player2.shipsplaced].PosY = 1
                    self.shiplist[4+self.player2.shipsplaced].draw()

                    self.player2.shipsplaced +=1
                                    
            self.board.draw()
            globals.gameDisplay.blit(globals.boot1off, (self.ship1.PosX * 20,self.ship1.PosY * 20))

            globals.gameDisplay.blit(globals.boot3off, (self.ship2.PosX * 20,self.ship2.PosY * 20))

            globals.gameDisplay.blit(globals.boot3off, (self.ship3.PosX * 20,self.ship3.PosY * 20))
 
            globals.gameDisplay.blit(globals.boot4off, (self.ship4.PosX * 20,self.ship4.PosY * 20))

            globals.gameDisplay.blit(globals.boot5off, (self.ship5.PosX * 20,self.ship5.PosY * 20))
            
            globals.gameDisplay.blit(globals.boot7off, (self.ship6.PosX * 20,self.ship6.PosY * 20))
            
            globals.gameDisplay.blit(globals.boot7off, (self.ship7.PosX * 20,self.ship7.PosY * 20))
                      
            globals.gameDisplay.blit(globals.boot8off, (self.ship8.PosX * 20,self.ship8.PosY * 20))
            
            pygame.display.update()
            
            globals.clock.tick(60)
            if self.player1.shipsplaced == 4 and self.player2.shipsplaced == 4:
                self.turn()    
            
        while self.player1.shipsplaced == 4 and self.player2.shipsplaced == 4 and not(self.GameStopped):
            self.shipxylist1 =[]
            self.curshiplist = []
            
            for x in range(0,8):
                self.shiplist[x].XYlist = []

            for i in range(4):                 
                for c in range(self.shiplist[i].ShipLength):
                    if (self.player1.Turn and i != self.shipcnt):
                        if self.shiplist[i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX + c, self.shiplist[i].PosY)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX +c, self.shiplist[i].PosY)]

                        if self.shiplist[4+i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]

                    elif self.player1.Turn:
                        if self.shiplist[4+i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]

                    if (self.player2.Turn and i+4 != self.shipcnt):
                        if self.shiplist[i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX + c, self.shiplist[i].PosY)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX +c, self.shiplist[i].PosY)]
                        
                        if self.shiplist[4+i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX, self.shiplist[4+i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]
                            self.shiplist[4+i].XYlist = self.shiplist[4+i].XYlist + [(self.shiplist[4+i].PosX +c, self.shiplist[4+i].PosY)]

                    elif self.player2.Turn:
                        if self.shiplist[i].Offensive:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX, self.shiplist[i].PosY +c)]
                        else:
                            self.shipxylist1 = self.shipxylist1 + [(self.shiplist[i].PosX + c, self.shiplist[i].PosY)]
                            self.shiplist[i].XYlist = self.shiplist[i].XYlist + [(self.shiplist[i].PosX +c, self.shiplist[i].PosY)]


            if self.player1.Turn:
                self.shiplist[self.shipcnt].Color = self.player1.aColor
            else:
                self.shiplist[self.shipcnt].Color = self.player2.aColor
            for event in pygame.event.get():
                if self.firecnt == 0:
                    click = pygame.mouse.get_pressed()
            
                    if click[0] == 1:
                        time.sleep(0.2)
                        mouse = pygame.mouse.get_pos()
                    
                        mousex = int(mouse[0]/20)
                        mousey = int(mouse[1]/20)
                        mousexy = (mousex, mousey)

                        if self.player1.Turn:
                            if mousexy in self.shiplist[0].XYlist:
                                if 0 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player1.iColor
                                self.shipcnt = 0
                                self.shiplist[self.shipcnt].Color = self.player1.aColor
                            if mousexy in self.shiplist[1].XYlist:
                                if 1 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player1.iColor
                                self.shipcnt = 1
                                self.shiplist[self.shipcnt].Color = self.player1.aColor
                            if mousexy in self.shiplist[2].XYlist:
                                if 2 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player1.iColor
                                self.shipcnt = 2
                                self.shiplist[self.shipcnt].Color = self.player1.aColor
                            if mousexy in self.shiplist[3].XYlist:
                                if 3 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player1.iColor
                                self.shipcnt = 3
                                self.shiplist[self.shipcnt].Color = self.player1.aColor

                        if self.player2.Turn:
                            if mousexy in self.shiplist[4].XYlist:
                                if 4 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player2.iColor
                                self.shipcnt = 4
                                self.shiplist[self.shipcnt].Color = self.player2.aColor
                            if mousexy in self.shiplist[5].XYlist:
                                if 5 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player2.iColor
                                self.shipcnt = 5
                                self.shiplist[self.shipcnt].Color = self.player2.aColor
                            if mousexy in self.shiplist[6].XYlist:
                                if 6 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player2.iColor
                                self.shipcnt = 6
                                self.shiplist[self.shipcnt].Color = self.player2.aColor
                            if mousexy in self.shiplist[7].XYlist:
                                if 7 in self.deadships:
                                    break
                                self.shiplist[self.shipcnt].Color = self.player2.iColor
                                self.shipcnt = 7
                                self.shiplist[self.shipcnt].Color = self.player2.aColor

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                #Pause key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.firecnt ==0:
                        self.shiprotate()
                    if event.key == pygame.K_f:
                        self.fire()
                    if event.key == pygame.K_p:
                        state = PAUSE
                    if event.key == pygame.K_u:
                        state = RUNNING
                    if event.key == pygame.K_t:
                        self.turn()
                    if event.key == pygame.K_1:
                        for i in range(0,4):
                            self.shiplist[i].Health = 0
                    if event.key == pygame.K_2:
                        for i in range(4,8):
                            self.shiplist[i].Health = 0

                        
                    if event.key == pygame.K_LEFT:
                        if self.shiplist[self.shipcnt].Steps == 0 or self.attackcnt != 0 or not self.shiplist[self.shipcnt].Offensive:
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
                        if self.shiplist[self.shipcnt].Steps == 0 or self.attackcnt != 0 or not self.shiplist[self.shipcnt].Offensive:
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
                        if self.shiplist[self.shipcnt].Steps == 0 or self.attackcnt != 0 or not self.shiplist[self.shipcnt].Offensive:
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
                        if self.shiplist[self.shipcnt].Steps == 0 or self.attackcnt != 0 or not self.shiplist[self.shipcnt].Offensive:
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
            text.button("End turn",650,25,140,50,globals.blue,globals.bright_blue,self.turn)
            text.button("Fire",650,100,140,50,globals.red,globals.bright_red,self.fire)
            fbuty = 180
            
            if self.firecnt in self.shipsinrange:
                self.damageship = 0 + self.firecnt
                text.button("",650,fbuty,140,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60
                
            if self.firecnt+1 in self.shipsinrange:
                self.damageship = 1 + self.firecnt
                text.button("",650,fbuty,140,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60

            if self.firecnt+2 in self.shipsinrange:
                self.damageship = 2 + self.firecnt
                text.button("",650,fbuty,140,50,globals.blue,globals.bright_blue,self.damage)
                fbuty += 60
                
            if self.firecnt +3 in self.shipsinrange:
                self.damageship = 3 + self.firecnt  
                text.button("",650,fbuty,140,50,globals.blue,globals.bright_blue,self.damage)
                

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


            if self.ship1.Health <= 0 and self.ship2.Health <= 0 and self.ship3.Health <= 0 and self.ship4.Health <= 0:
                print("Player2 wins")
                mysql_con = mysql.mysql()
                update = mysql_con.update("UPDATE score SET points = points + 1 WHERE name = 'Player2'")
                self.GameStopped = True
            elif self.ship5.Health <= 0 and self.ship6.Health <= 0 and self.ship7.Health <= 0 and self.ship8.Health <= 0:
                print("Player1 wins")
                mysql_con = mysql.mysql()
                update = mysql_con.update("UPDATE score SET points = points + 1 WHERE name = 'Player1'")
                self.GameStopped = True



            statsx = 500
            statsy = 25

            currentshipname = globals.smallText.render("Current ship: ", True, globals.white)
            shipname = globals.infoText.render("Name: " + str(self.shiplist[self.shipcnt].Name), True, globals.white)
            currentshiphp = globals.infoText.render("HP: " + str(self.shiplist[self.shipcnt].Health), True, globals.white)
            currentshiprange = globals.infoText.render("Range: " + str(self.shiplist[self.shipcnt].Range), True, globals.white)
            currentshipdamage = globals.infoText.render("Damage: " + str(self.shiplist[self.shipcnt].Damage), True, globals.white)
            currentshipshots = globals.infoText.render("Shots left: " + str(self.shiplist[self.shipcnt].Shots), True, globals.white)
            currentshipsteps = globals.infoText.render("Steps left: " + str(self.shiplist[self.shipcnt].Steps), True, globals.white)
            fbuty = 180
            for i in range(0,self.attackcnt):

                
                attshipname = globals.infoText.render("Name: " + str(self.shiplist[self.shipsinrange[i]].Name), True, globals.white)
                attshiphp = globals.infoText.render("HP: " + str(self.shiplist[self.shipsinrange[i]].Health), True, globals.white)
                attshipxy = globals.infoText.render("Position: (" + str(self.shiplist[self.shipsinrange[i]].PosX) + " , " + str(self.shiplist[self.shipsinrange[i]].PosY) + ")", True, globals.white)


                globals.gameDisplay.blit(attshipname, (655 , fbuty+2))
                globals.gameDisplay.blit(attshiphp,(655, fbuty+18))
                globals.gameDisplay.blit(attshipxy, (655, fbuty + 34))
                fbuty += 60

            pygame.draw.rect(globals.gameDisplay, globals.white, (statsx, statsy , 140 , 140), 1)
            globals.gameDisplay.blit(currentshipname, (statsx +5 , statsy+10))
            globals.gameDisplay.blit(shipname, (statsx +5 , statsy+28))
            globals.gameDisplay.blit(currentshiphp, (statsx +5 , statsy+46))
            globals.gameDisplay.blit(currentshiprange, (statsx +5 , statsy+64))
            globals.gameDisplay.blit(currentshipdamage, (statsx +5 , statsy+82))
            globals.gameDisplay.blit(currentshipshots, (statsx +5 , statsy+100))
            globals.gameDisplay.blit(currentshipsteps, (statsx +5 , statsy+118))
            cardsy = 20
            self.cardused = False
            
            if self.player1.Turn:
                for i in range(len(self.player1.Cards)):
                    self.index = i
                    globals.gameDisplay.blit(self.player1.Cardimg[i], (cardsy,450))
                    text.button("",cardsy,450,100,125,globals.black,globals.black,self.player1.Cards[i].Action)
                    if self.cardused:
                        break
                    cardsy += 120
            else:
                for i in range(len(self.player2.Cards)):
                    self.index = i
                    globals.gameDisplay.blit(self.player2.Cardimg[i], (cardsy,450))
                    text.button("",cardsy,450,100,125,globals.black,globals.black,self.player2.Cards[i].Action)
                    if self.cardused:
                        break
                    cardsy += 120

            self.ship1.draw()
            self.ship2.draw()
            self.ship3.draw()
            self.ship4.draw()
            self.ship5.draw()
            self.ship6.draw()
            self.ship7.draw()
            self.ship8.draw()

            self.board.draw()
            if self.ship1.Offensive:
                globals.gameDisplay.blit(globals.boot1off, (self.ship1.PosX * 20,self.ship1.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot1def, (self.ship1.PosX * 20,self.ship1.PosY * 20))
            
            if self.ship2.Offensive:
                globals.gameDisplay.blit(globals.boot3off, (self.ship2.PosX * 20,self.ship2.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot3def, (self.ship2.PosX * 20,self.ship2.PosY * 20))
            
            if self.ship3.Offensive:
                globals.gameDisplay.blit(globals.boot3off, (self.ship3.PosX * 20,self.ship3.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot3def, (self.ship3.PosX * 20,self.ship3.PosY * 20))
            
            if self.ship4.Offensive:
                if self.ship4.Health > 0:
                    globals.gameDisplay.blit(globals.boot4off, (self.ship4.PosX * 20,self.ship4.PosY * 20))
                else:
                    globals.gameDisplay.blit(globals.boot4offdead, (self.ship4.PosX * 20,self.ship4.PosY * 20))
            else:
                if self.ship4.Health > 0:
                    globals.gameDisplay.blit(globals.boot4def, (self.ship4.PosX * 20,self.ship4.PosY * 20))
                else:
                    globals.gameDisplay.blit(globals.boot4defdead, (self.ship4.PosX * 20,self.ship4.PosY * 20))
            if self.ship5.Offensive:
                globals.gameDisplay.blit(globals.boot5off, (self.ship5.PosX * 20,self.ship5.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot5def, (self.ship5.PosX * 20,self.ship5.PosY * 20))
            
            if self.ship6.Offensive:
                globals.gameDisplay.blit(globals.boot7off, (self.ship6.PosX * 20,self.ship6.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot7def, (self.ship6.PosX * 20,self.ship6.PosY * 20))
            
            if self.ship7.Offensive:
                globals.gameDisplay.blit(globals.boot7off, (self.ship7.PosX * 20,self.ship7.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot7def, (self.ship7.PosX * 20,self.ship7.PosY * 20))
            
            if self.ship8.Offensive:
                globals.gameDisplay.blit(globals.boot8off, (self.ship8.PosX * 20,self.ship8.PosY * 20))
            else:
                globals.gameDisplay.blit(globals.boot8def, (self.ship8.PosX * 20,self.ship8.PosY * 20))
 
            pygame.display.update()
            globals.clock.tick(60)


def program():
    game = Game()
    game.game_loop()
