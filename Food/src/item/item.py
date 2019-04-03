
import pygame

from .identifiers import *

class item(pygame.sprite.Sprite):

    def __init__(self, origin, type, id, hasUse):

        # Identifiers
        self.origin = origin
        self.type = type
        self.id = id
        self.usable = hasUse

        self.image = setImage()
        self.rect - self.image.get_rect()

def setImage(id):

    if id == ID.test:
        self.image =




