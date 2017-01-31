import pygame, globals, text, menu, webbrowser

def show():
    credits = True
    while credits:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        globals.gameDisplay.fill(globals.black)

        TextSurf, TextRect = text.text_objects("Credits", globals.largeText)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(120))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(145))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(170))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(195))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(220))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(245))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText)
        TextRect.center = ((400),(270))
        globals.gameDisplay.blit(TextSurf, TextRect)

        text.button("Fabian !",95,475,100,50,globals.purple,globals.bright_grey,openweb)
        text.button("Tim !",275,475,75,50,globals.green2,globals.bright_grey,openweb1)
        text.button("Bob !",440,475,75,50,globals.red2,globals.bright_grey,openweb2)
        text.button("Damian !",605,475,100,50,globals.blue2,globals.bright_grey,openweb3)
        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        
        globals.clock.tick(60)
        pygame.display.update()

def openweb():
    url = "www.fabianlallemand.nl"
    webbrowser.open_new(url)

def openweb1():
    url = "www.timvanleeuwen.jimdo.com"
    webbrowser.open_new(url)

def openweb2():
    url = "www.bobportfolio.wordpress.com"
    webbrowser.open_new(url)

def openweb3():
    url = "www.damianvanvuuren.jimdo.com"
    webbrowser.open_new(url)