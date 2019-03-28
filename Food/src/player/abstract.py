## @file   abstract.py
#  @title  Player Information
#  @author Lucas Zacharewicz
#  @date   March 23, 2019


import pygame
import game


PL_SPEED = 3
PL_MAXHP = 4


class Player(pygame.sprite.Sprite):

    def __init__(self, image):

        super().__init__()

        # Give player Identifier
        self.id = game.ID.PLAYER

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = True
        self.collidable = True

        # Set default Sprite, Make rectangle
        self.image = image
        self.rect = self.image.get_rect()

        # Establish player states
        self.attackCooldown = False
        self.attackCooldownFrame = 0

        # Player stats
        self.hp = PL_SPEED
        self.maxHP = PL_MAXHP


    @property
    def pos(self):
        return (self.rect.x,self.rect.y)
