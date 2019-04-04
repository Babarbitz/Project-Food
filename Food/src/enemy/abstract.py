## @file   abstract.py
#  @title  Enemy Information
#  @author Alex Lo
#  @date   April 4, 2019

import pygame
import game


class Enemy(pygame.sprite.Sprite):

    def __init__(self, image, health):

        super().__init__()

        
        self.id = game.ID.ENEMY

        
        self.renderable = True
        self.updatable  = True
        self.collidable = True

        
        self.image = image
        self.rect = self.image.get_rect()

        
        self.attackCooldown = False
        self.attackCooldownFrame = 0

        
        self.hp = health


    @property
    def pos(self):
        return (self.rect.x,self.rect.y)
