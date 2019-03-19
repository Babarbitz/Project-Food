## @file   controller.py
#  @title  Sprite group controller
#  @author Lucas Zacharewicz
#  @date   March 12, 2019

import pygame

class SpriteGroupController():

    def __init__(self):

        self.renderedEntities = pygame.sprite.Group()
        self.updatedEntities = pygame.sprite.Group()
        self.collidableEntities = pygame.sprite.Group()

    def add(self,entity):

        if entity.renderable:
           self.renderedEntities.add(entity)
        if entity.updatable:
           self.updatedEntities.add(entity)
        if entity.collidable:
           self.collidableEntities.add(entity)

    # Runs updates for all sprite group
    def update(self):

        self.updatedEntities.update()


