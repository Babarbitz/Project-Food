## @file   window.py
#  @title  Window object for game output
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import pygame
from window.constants import *

## @brief The class wraps pygame functionallity related to window sprite lists,
#         clock speed, and rendering to a form that is easier to use for the
#         project.
class Window:
   
    ## @brief Set the clock and window
    def __init__(self):
        
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(DEFAULT_RES)

    ## @brief Render to screen and maintain 60fps clock rate
    def update(self):
        
        pygame.display.flip()
        self.clock.tick(60)
