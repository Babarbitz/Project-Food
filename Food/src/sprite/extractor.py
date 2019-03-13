## @file   extractor.py
#  @title  Sprite Extractor
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame

## @brief This function takes a sprite sheet and returns a list of sprites for
#         a renderable object
#
#  @param f  The file that holds the sprites

def extractSprites(fileName, width, height, size):

    images = []

    # Make a sprite sheet object
    spriteSheet = pygame.image.load(fileName).convert_alpha()

    # Split the sheet into individual sprites

    for x in range(0, width-1, size):
        for y in range(0, height-1, size):
            image = pygame.Surface([size,size]).convert()
            image.blit(spriteSheet, (0,0), (x,y,size,size))
            image.set_colorkey((0,0,0))
            images.append(image)

    return images
