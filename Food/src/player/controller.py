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
PR_SPEED = 4
PL_SPRITE = 'Food/assets/Chef.png'
PL_SPRITESIZE = 64
PL_SPRITESHEET = (64,64)
PR_SPRITE = 'Food/assets/knife.png'
PR_SPRITESIZE = 16
PR_SPRITESHEET = (16,16)

# ATTACK SPAWNS

# Centers the sprite in the view
OFFSET = (PL_SPRITESIZE/2) - (PR_SPRITESIZE/2)

class Player(pygame.sprite.Sprite):

################################################################################
# Initializer #
################################################################################

    def __init__(self):

        # Call parent constructor
        super().__init__()

        # Get sprites
        self.sprites = se.extractSprites(PL_SPRITE,64,64,64)
        self.projectileSprites = se.extractSprites(PR_SPRITE,64,16,16)

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

################################################################################
# Movement #
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
# Basic Attacks #
################################################################################

    def attackNorth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x + OFFSET, self.rect.y, 0, -PR_SPEED,
                    self.projectileSprites[0])

            sc.add(temp)
            #self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackSouth(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x + OFFSET, self.rect.y + 64, 0, PR_SPEED,
                    self.projectileSprites[1])

            sc.add(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackWest(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, -PR_SPEED, 0,
                    self.projectileSprites[2])

            sc.add(temp)
            self.projectiles.append(temp)

            self.attackCooldown = True
            self.attackCooldownFrame = self.frame

    def attackEast(self, sc):

        if not self.attackCooldown:
            temp = pr.Projectile(self.rect.x, self.rect.y, PR_SPEED, 0,
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
