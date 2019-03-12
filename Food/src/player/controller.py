## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame
import sprite.extractor as se

PLAYERSPEED = 3


class Player(pygame.sprite.Sprite):

    def __init__(self):

        # Call parent constructor
        super().__init__()

        self.sprites = se.extractSprites("Food/assets/Chef.png",64,64)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()


    def moveWest(self):
        self.rect.x -= PLAYERSPEED

    def moveEast(self):
        self.rect.x += PLAYERSPEED

    def moveNorth(self):
        self.rect.y -= PLAYERSPEED

    def moveSouth(self):
        self.rect.y += PLAYERSPEED

    def attackNorth(self):
        pass
