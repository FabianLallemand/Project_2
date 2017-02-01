import pygame, globals, text , game, webbrowser, credits, highscores, settings

pygame.mixer.init()
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
        globals.gameDisplay.blit(globals.Background, (0,0))
        
 

        #Title        
        TextSurf, TextRect = text.text_objects("Battleport", globals.largeText, globals.bright_grey)
        TextRect.center = ((280),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos()

        text.button("Start Game!",75,450,100,50,globals.green,globals.bright_green,game.program)
        text.button("Highscores",125,525,100,50,globals.grey,globals.bright_orange,highscores.show)
        text.button("Game Rules",350,525,100,50,globals.grey,globals.bright_blue,globals.openrules)
        text.button("Settings",575,525,100,50,globals.grey,globals.bright_grey,settings.settings)
        text.button("Quit Game!",625,450,100,50,globals.red,globals.bright_red,globals.quitgame)
        text.button("Credits",690,10,100,50,globals.grey,globals.bright_grey,credits.show)

        pygame.display.update()
        globals.clock.tick(60)

