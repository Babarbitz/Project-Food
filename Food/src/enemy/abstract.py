## @file   abstract.py
#  @title  Enemy Information
#  @author Alex Lo
#  @date   April 4, 2019

import pygame
import game


class Enemy(pygame.sprite.Sprite):

    def __init__(self, image, data, pos):

        super().__init__()

        self.id = game.ID.ENEMY

        self.renderable = True
        self.updatable  = True
        self.collidable = True

        self.image = image
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # Attributes
        self.hp = data[0]
        self.speed = data[1]
        self.damage = data[2]

        self.oldx = pos[0]
        self.oldy = pos[1]

        self.frame = 0

    @property
    def pos(self):
        return (self.rect.x,self.rect.y)
