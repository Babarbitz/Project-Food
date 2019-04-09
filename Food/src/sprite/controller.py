## @file   controller.py
#  @title  Sprite group controller
#  @author Lucas Zacharewicz
#  @date   March 12, 2019

import pygame
import game

class SpriteGroupController():

    def __init__(self):

        self.collidableEntities = pygame.sprite.Group()

        self.baselayer = pygame.sprite.Group()
        self.textlayer = pygame.sprite.Group()
        self.projectilelayer = pygame.sprite.Group()
        self.playerlayer = pygame.sprite.Group()
        self.menulayer = pygame.sprite.Group()
        self.inventorylayer = pygame.sprite.Group()

    def add(self,entity):

        if entity.renderable:

            if entity.id == game.ID.PLAYER:
                self.playerlayer.add(entity)

            elif entity.id == game.ID.PROJECTILE:
                self.projectilelayer.add(entity)

            elif entity.id == game.ID.TEXT:
                self.textlayer.add(entity)

            elif entity.id == game.ID.MENU:
                self.menulayer.add(entity)

            elif entity.id == game.ID.INVENT:
                self.inventorylayer.add(entity)

            else:
                self.baselayer.add(entity)

        if entity.collidable:
            self.collidableEntities.add(entity)


    def remove(self, entity):

        if entity in self.baselayer:
            self.baselayer.remove(entity)

        elif entity in self.projectilelayer:
            self.projectilelayer.remove(entity)

        elif entity in self.playerlayer:
            self.playerlayer.remove(entity)

        elif entity in self.textlayer:
            self.textlayer.remove(entity)

        elif entity in self.menulayer:
            self.menulayer.remove(entity)

        self.collidableEntities.remove(entity)
