## @file   text.py
#  @title  Text render
#  @author Lucas Zacharewicz
#  @date   November 8 2018

import pygame
import game

FONT = 'Food/assets/font/gamefont.ttf'

class Text(pygame.sprite.Sprite):

    def __init__(self, pos, string, fontsize, color):

        super().__init__()
        pygame.font.init()

        self.id = game.ID.TEXT

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = False

        self.color = color

        self.string = string

        self.myfont = pygame.font.Font(FONT, fontsize)

        textsurface = self.myfont.render(string, False, color)

        self.image = textsurface
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def updateColor(self, color):
        self.color = color
        self.image = self.myfont.render(self.string, False, self.color)
