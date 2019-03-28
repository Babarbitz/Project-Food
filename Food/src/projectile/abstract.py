## @file   abstract.py
#  @title  Projectile
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


import pygame
import game


class Projectile(pygame.sprite.Sprite):


    def __init__(self, x, y, xspeed, yspeed, sprite, cList):

        super().__init__()

        self.image = sprite
        self.rect = self.image.get_rect()

        # Set flags for the spriteController
        self.renderable = True
        self.updatable = True
        self.collidable = True

        # Set position
        self.rect.x = x
        self.rect.y = y

        # Set speeds
        self.xspeed = xspeed
        self.yspeed = yspeed

        self.id = game.ID.PROJECTILE
        #self.source = source
        self.cList = cList

        # TODO
        # Set game attributes like damage
