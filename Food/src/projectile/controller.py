## @file   controller.py
#  @title  Projectile
#  @author Lucas Zacharewicz
#  @date   March 08, 2019

import pygame
import sprite.extractor as se

class Projectile(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.sprites = se.extractSprites("Food/assets/knife.png",64,16)
