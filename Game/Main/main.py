"""
PyGame Battleport
Fabian Lallemand, Tim van Leeuwen, Bob Verkaik & Damian van Vuuren
"""

import pygame, menu, globals, settings



pygame.init()
pygame.display.set_caption('Battleport')
pygame.display.set_icon(globals.gameIcon)

pygame.mixer.init()
settings.music("start")


menu.game_intro()
pygame.quit()
quit()
