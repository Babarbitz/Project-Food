import pygame
import game
import sprite

BG_SPRITE = 'Food/assets/base.png'
BG_SIZE = (1280, 896)
BG_STEP = (1280, 896)


class Background(pygame.sprite.Sprite):

    def __init__(self, image):

        super().__init__()

        self.id = None

        self.image = image
        self.rect = self.image.get_rect()

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = False

class Structure(pygame.sprite.Sprite):

    def __init__(self,pos,size,sprite):

        super().__init__()

        #self.Sprite = se.extractSprites(sprite, size, size)
        self.image = self.sSprites[0]

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.id = game.ID.STRUCTURE

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = True

class Wall(pygame.sprite.Sprite):

    def __init__(self,pos,size):

        super().__init__()

        self.image = pygame.Surface(size)

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.id = game.ID.WALL

        # Set flags for the spriteController
        self.renderable = False
        self.updatable  = False
        self.collidable = True

class Door(pygame.sprite.Sprite):

    def __init__(self, sprite, pos, direction):

        super().__init__()

        self.image = sprite

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.id = game.ID.DOOR
        self.type = direction

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = True
