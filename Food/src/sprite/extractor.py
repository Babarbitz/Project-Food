## @file   extractor.py
#  @title  Sprite Extractor
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame

## @brief This function takes a sprite sheet and returns a list of sprites for
#         a renderable object
#
#  @param f  The file that holds the sprites

def extractSprites(fileName, size, step):

    images = []

    # Make a sprite sheet object
    spriteSheet = pygame.image.load(fileName).convert_alpha()

    # Split the sheet into individual sprites

    for x in range(0, size[0] - 1, step[0]):
        for y in range(0, size[1] - 1, step[1]):
            image = pygame.Surface([step[0],step[1]]).convert()
            image.blit(spriteSheet, (0,0), (x,y,step[0],step[1]))
            image.set_colorkey((0,0,0))
            images.append(image)

    return images
