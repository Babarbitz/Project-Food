## @file   window.py
#  @title  Window object for game output
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import pygame
from .constants import *

## @brief The class wraps pygame functionallity related to window sprite lists,
#         clock speed, and rendering to a form that is easier to use for the
#         project.

class Window:

    ## @brief Set the clock and window
    def __init__(self):

        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(DEFAULT_RES)

    ## @brief Render to screen and maintain 60fps clock rate
    def update(self, sc):

        self.window.fill((0,0,0))
        sc.baselayer.draw(self.window)
        sc.projectilelayer.draw(self.window)
        sc.playerlayer.draw(self.window)
        sc.enemylayer.draw(self.window)
        sc.inventorylayer.draw(self.window)
        sc.menulayer.draw(self.window)
        sc.textlayer.draw(self.window)
        pygame.display.flip()
        self.clock.tick(60)
