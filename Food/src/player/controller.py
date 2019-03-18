## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


# Imports
import pygame
import sprite.extractor as se
import projectile.controller as pr

# Constants
PL_SPEED = 3
PR_SPEED = 8
PL_SPRITE = 'Food/assets/Chef.png'
PL_STEP = (64,64)
PL_SIZE = (64,64)
PR_SPRITE = 'Food/assets/knife.png'
PR_STEP = (32,32)
PR_SIZE = (128,32)


# Centers the sprite in the view
OFFSET = (PL_STEP[0]/2) - (PR_STEP[0]/2)

class Player(pygame.sprite.Sprite):

################################################################################
#                                 Initializer                                  #
################################################################################

    def __init__(self):

        # Call parent constructor
        super().__init__()

        # Get sprites
        self.plSprites = se.extractSprites(PL_SPRITE,PL_SIZE,PL_STEP)
        self.prSprites = se.extractSprites(PR_SPRITE,PR_SIZE,PR_STEP)

        self.image = self.plSprites[0]
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

################################################################################
#                                  Movement                                    #
################################################################################

    def moveWest(self):
        self.rect.x -= PL_SPEED

    def moveEast(self):
        self.rect.x += PL_SPEED

    def moveNorth(self):
        self.rect.y -= PL_SPEED

    def moveSouth(self):
        self.rect.y += PL_SPEED

################################################################################
#                               Basic Attacks                                  #
################################################################################

    def attackNorth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x + OFFSET, self.rect.y, 0, -PR_SPEED,
                    self.prSprites[0])

            sc.add(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackSouth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x + OFFSET, self.rect.y +
                    PL_STEP[0], 0, PR_SPEED,
                    self.prSprites[1])

            sc.add(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackWest(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y + OFFSET, -PR_SPEED, 0,
                    self.prSprites[2])

            sc.add(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackEast(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x + PL_STEP[0], self.rect.y +
                    OFFSET, PR_SPEED, 0,
                    self.prSprites[3])

            sc.add(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

################################################################################

    def checkStates(self):

        if self.frame - self.attackCooldownFrame > 20:
            self.attackCooldown = False

    def update(self):
        self.checkStates()
        self.frame += 1
