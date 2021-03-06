import pygame, globals, time

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    #titleSurface = font.render(text, True, globals.white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(globals.gameDisplay, ac,(x,y,w,h),1)

        if click[0] == 1 and action != None:
            time.sleep(0.5)
            action()
                    
    else:
        pygame.draw.rect(globals.gameDisplay, ic,(x,y,w,h),1)       
    #button text    
    textSurf, textRect = text_objects(msg, globals.smallText, globals.bright_grey)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    globals.gameDisplay.blit(textSurf, textRect)