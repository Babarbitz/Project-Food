import pygame
import game

class Background(pygame.sprite.Sprite):

    def __init__(self, image):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.id = game.ID.MENU

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = False
