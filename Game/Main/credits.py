import pygame, globals, text, menu, webbrowser

def show():

    credits = True

    while credits:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                globals.quitgame()

        mouse = pygame.mouse.get_pos()
        globals.gameDisplay.blit(globals.BackgroundBlur, (0,0))

        #Title
        TextSurf, TextRect = text.text_objects("Credits", globals.largeText, globals.bright_grey)
        TextRect.center = ((400),(55)) 
        globals.gameDisplay.blit(TextSurf, TextRect)

        #Little story
        TextSurf, TextRect = text.text_objects("The Development team of this game is very proud to present!", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(120))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("Battleport", globals.mediumText, globals.bright_black)
        TextRect.center = ((400),(155))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("We have put a lot of work into this project.", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(200))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("It has taken bloodshed, tears & a lot of sweat!", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(225))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("This all is made possible by the gifted programmers,", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(250))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("whose portfolio websites have been linked down below.", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(275))
        globals.gameDisplay.blit(TextSurf, TextRect)
        TextSurf, TextRect = text.text_objects("If you click on a name their website will pop-up.", globals.smallText, globals.bright_black)
        TextRect.center = ((400),(300))
        globals.gameDisplay.blit(TextSurf, TextRect)

        #Buttons to portfolio websites
        text.button("Fabian !",95,475,100,50,globals.purple,globals.bright_grey,openweb)
        text.button("Tim !",275,475,75,50,globals.green2,globals.bright_grey,openweb1)
        text.button("Bob !",440,475,75,50,globals.red2,globals.bright_grey,openweb2)
        text.button("Damian !",605,475,100,50,globals.blue2,globals.bright_grey,openweb3)
        text.button("Back!",690,10,100,50,globals.grey,globals.bright_red,menu.game_intro)
        
        globals.clock.tick(60)
        pygame.display.update()

#Portfolio websites functions
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