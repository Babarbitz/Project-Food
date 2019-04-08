## @file   controller.py
#  @title  Sprite group controller
#  @author Lucas Zacharewicz
#  @date   March 12, 2019

import pygame
import game

class SpriteGroupController():

    def __init__(self):

        self.renderedEntities = pygame.sprite.Group()
        self.collidableEntities = pygame.sprite.Group()

        self.baselayer = []
        self.projectilelayer = []
        self.playerlayer = []
        self.textlayer = []

    def add(self,entity):

        if entity.renderable:

            if entity.id == game.ID.PLAYER:
                self.playerlayer.append(entity)

            elif entity.id == game.ID.PROJECTILE:
                self.projectilelayer.append(entity)

            elif entity.id == game.ID.TEXT:
                self.textlayer.append(entity)

            else:
                self.baselayer.append(entity)

            self.updateRender()

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

        self.collidableEntities.remove(entity)

        self.updateRender()

    def updateRender(self):

        self.renderedEntities.empty()
        self.renderedEntities.add(self.baselayer)
        self.renderedEntities.add(self.projectilelayer)
        self.renderedEntities.add(self.playerlayer)
        self.renderedEntities.add(self.textlayer)
