import pygame, globals, text , game, webbrowser

#game intro and button's
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            click = pygame.mouse.get_pressed()


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Background code
        BackGround = pygame.image.load('assets/background.jpg')
        globals.gameDisplay.blit(BackGround, (0,0))
        
 

        #Title        
        TextSurf, TextRect = text.text_objects("Battleport", globals.largeText)
        TextRect.center = ((280),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos()

        text.button("Start Game!",75,450,100,50,globals.green,globals.bright_green,game.program)
        text.button("Highscore",125,525,100,50,globals.grey,globals.bright_orange,highscores)
        text.button("Game Rules",350,525,100,50,globals.grey,globals.bright_blue,openrules)
        text.button("Settings",575,525,100,50,globals.grey,globals.bright_grey,None)
        text.button("Quit Game!",625,450,100,50,globals.red,globals.bright_red,globals.quitgame)
        text.button("Credits",690,10,100,50,globals.grey,globals.bright_grey,None)

        pygame.display.update()
        globals.clock.tick(60)

def highscores():
    hscore = True


    while hscore:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        globals.gameDisplay.fill(globals.white)


        text.button("Back!",650,50,100,50,globals.orange,globals.bright_red,game_intro)
        
        globals.clock.tick(60)
        pygame.display.update()


def openrules():
    url = "https://www.dropbox.com/sh/fqanfbkw8l5y0b6/AAA8PrSl17eJWV_1DkiRGvVoa?dl=0"
    webbrowser.open_new(url)