
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

'''def setImage(id):

    if id == ID.test:
        self.image ='''




