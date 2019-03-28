## @file   room.py
#  @title  Room
#  @author Lucas Zacharewicz
#  @date   March 17, 2019

import pygame
import game
import sprite

BG_SPRITE = 'Food/assets/base.png'
BG_SIZE = (1280, 896)
BG_STEP = (1280, 896)

class Room():

    def __init__(self):

        # Room background Image
        self.background = Background()

        # Room Wall collison
        self.walls = []

        self.walls.append(Wall([0,0],[128,896]))
        self.walls.append(Wall([0,0],[1280,128]))
        self.walls.append(Wall([1152,0],[128,896]))
        self.walls.append(Wall([0,768],[1280,128]))
        #structures
        self.structures = []

        #enemies

        #doors

    def render(self, sc):

        sc.add(self.background)


        for wall in self.walls:
            print(wall)
            sc.add(wall)

        for structure in self.structures:
            sc.add(structure)


class Background(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.bgSprites = sprite.extractSprites(BG_SPRITE, BG_SIZE, BG_STEP)
        self.image = self.bgSprites[0]
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

    def __init__(self,pos,size,sprite):

        super().__init__()

        self.Sprite = sprite.extractSprites(sprite, size, size)
        self.image = self.sSprites[0]

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.id = game.ID.STRUCTURE

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = False
        self.collidable = True
