## @file   room.py
#  @title  Room
#  @author Lucas Zacharewicz
#  @date   March 17, 2019

import pygame
import sprite.extractor as se

FL_SPRITE = 'Food/assets/floor.png'
FL_SIZE = (1280, 640)
FL_STEP = (1280, 640)
class Room():

    def __init__(self):

        floor = Floor()

        #structures
        #borders

        #enemies

        #doors


class Floor(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = se.extractSprites(FL_SPRITE, FL_SIZE, FL_STEP)
        self.rect = self.image.get_rect()

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = False


