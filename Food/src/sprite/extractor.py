## @file   extractor.py
#  @title  Sprite Extractor
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame

SPRITESIZE = 64

## @brief This function takes a sprite sheet and returns a list of sprites for
#         a renderable object
#
#  @param f  The file that holds the sprites

def extractSprites(fileName, width, height):

    images = []

    # Make a sprite sheet object
    spriteSheet = pygame.image.load(fileName).convert_alpha()

    # Split the sheet into individual sprites

    for i in range(0, width-1, SPRITESIZE):
        for j in range(0, height-1, SPRITESIZE):
            image = pygame.Surface([SPRITESIZE,SPRITESIZE]).convert()
            image.blit(spriteSheet, (0,0), (i,j,SPRITESIZE,SPRITESIZE))
            image.set_colorkey((0,0,0))
            images.append(image)

    return images
