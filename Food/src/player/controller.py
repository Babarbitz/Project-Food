## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


# Imports
import pygame
import sprite.extractor as se
import projectile.controller as pr

# Constants
PLAYERSPEED = 3
PROJECTILESPEED = 4
SPRITE = 'Food/assets/Chef.png'
PROJECTILESPRITE = 'Food/assets/knife.png'

class Player(pygame.sprite.Sprite):

################################################################################
# Initializer #
################################################################################

    def __init__(self):

        # Call parent constructor
        super().__init__()

        # Get sprites
        self.sprites = se.extractSprites(SPRITE,64,64,64)
        self.projectileSprites = se.extractSprites(PROJECTILESPRITE,64,16,16)

        self.image = self.sprites[0]
        self.rect = self.image.get_rect()

        # Set flags for the spriteController
        self.renderable = True
        self.updatable  = True
        self.collidable = True

        # Etablish player states
        self.attackCooldown = False
        self.attackCooldownFrame = 0

        # Create Frame Counter
        self.frame = 0

        # Create empty list of projectiles
        self.projectiles = []

################################################################################
# Movement #
################################################################################

    def moveWest(self):
        self.rect.x -= PLAYERSPEED

    def moveEast(self):
        self.rect.x += PLAYERSPEED

    def moveNorth(self):
        self.rect.y -= PLAYERSPEED

    def moveSouth(self):
        self.rect.y += PLAYERSPEED

################################################################################
# Basic Attacks #
################################################################################

    def attackNorth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, 0, -PROJECTILESPEED,
                    self.projectileSprites[0])

            sc.add(temp)
            self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame


    def attackSouth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, 0, PROJECTILESPEED,
                    self.projectileSprites[1])

            sc.add(temp)
            self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackWest(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, -PROJECTILESPEED, 0,
                    self.projectileSprites[2])

            sc.add(temp)
            self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackEast(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, PROJECTILESPEED, 0,
                    self.projectileSprites[3])

            sc.add(temp)
            self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

################################################################################

    def checkStates(self):

        if self.frame - self.attackCooldownFrame > 20:
            self.attackCooldown = False

    def update(self):
        self.checkStates()
        self.frame += 1
