"""
PyGame Battleport
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""

import pygame, menu, globals



pygame.init()
pygame.display.set_caption('Battleport')

pygame.mixer.init()
globals.MenuSoundfx.play().set_volume(0.2)
    
menu.game_intro()
pygame.quit()
quit()
