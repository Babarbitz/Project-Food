
import pygame
import game

from .identifiers import *

class Item(pygame.sprite.Sprite):

    def __init__(self, image, type, x, y):

        super().__init__()

        # Identifiers
        self.type = type
        self.id = game.ID.ITEM

        self.image = image
        self.rect = self.image.get_rect()

        self.renderable = True
        self.updatable = True
        self.collidable = True

        self.rect.x = x
        self.rect.y = y


    def pos(self):
        return (self.rect.x + 30//2, self.rect.y + 36//2)
'''def setImage(id):

    if id == ID.test:
        self.image ='''




