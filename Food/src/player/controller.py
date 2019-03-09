## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame
import sprite.extractor as se


class Player(pygame.sprite.Sprite):

    def __init__(self):

        # Call parent constructor
        super().__init__()

        self.sprites = se.extractSprites("Food/assets/Chef.png",64,64)
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

        self.xpos = 0.0
        self.ypos = 0.0
