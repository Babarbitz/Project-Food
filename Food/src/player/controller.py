## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


# Imports
import pygame
import input
from .abstract import *
import game.identifiers as gi
import sprite.extractor as se
import projectile.controller as pr


# Constants
PR_SPRITE = 'Food/assets/knife.png'
PR_SPEED = 8
PR_STEP = (32,32)
PR_SIZE = (128,32)

PR_LEFT = ()

PL_SPRITE = 'Food/assets/Chef.png'
PL_STEP = (64,64)
PL_SIZE = (64,64)

# Centers the sprite in the view
OFFSET = (PL_STEP[0]/2) - (PR_STEP[0]/2)

class PlayerController(pygame.sprite.Sprite):

################################################################################
#                                 Initializer                                  #
################################################################################

    def __init__(self, cList):

        # Call parent constructor
        super().__init__()

        # Get sprites
        self.plSprites = se.extractSprites(PL_SPRITE,PL_SIZE,PL_STEP)
        self.prSprites = se.extractSprites(PR_SPRITE,PR_SIZE,PR_STEP)

        # Player information
        self.player = Player(self.plSprites[0])

        self.oldx = 0
        self.oldy = 0

        # Set Collision list
        self.cList = cList

        # Create Frame Counter
        self.frame = 0

    def addToController(self, sc):
        sc.add(self.player)

    def setPosition(self, x, y):
        self.player.rect.x = x
        self.player.rect.y = y

################################################################################
#                                  Movement                                    #
################################################################################

    def moveWest(self):
        self.player.rect.x -= PL_SPEED

    def moveEast(self):
        self.player.rect.x += PL_SPEED

    def moveNorth(self):
        self.player.rect.y -= PL_SPEED

    def moveSouth(self):
        self.player.rect.y += PL_SPEED

################################################################################
#                               Basic Attacks                                  #
################################################################################

    def attackNorth(self, sc):

        self.attack(self.player.rect.x + OFFSET,
                    self.player.rect.y,
                    0,
                    -PR_SPEED,
                    self.prSprites[0],
                    sc)

    def attackSouth(self, sc):

        self.attack(self.player.rect.x + OFFSET,
                    self.player.rect.y + PL_STEP[0],
                    0,
                    PR_SPEED,
                    self.prSprites[1],
                    sc)

    def attackWest(self, sc):

        self.attack(self.player.rect.x,
                    self.player.rect.y + OFFSET,
                    -PR_SPEED,
                    0,
                    self.prSprites[2],
                    sc)

    def attackEast(self, sc):

        self.attack(self.player.rect.x + PL_STEP[0],
                    self.player.rect.y + OFFSET,
                    PR_SPEED,
                    0,
                    self.prSprites[3],
                    sc)

    def attack(self, x, y, xs, ys, sprite, sc):

        if not self.player.attackCooldown:
            temp = pr.Projectile(x, y, xs, ys, sprite, self.cList)
            sc.add(temp)
            self.player.attackCooldown = True
            self.player.attackCooldownFrame = self.frame

###############################################################################
#                           Collision Rules                                   #
###############################################################################

    def checkCollision(self):

        collisions = pygame.sprite.spritecollide(self.player,self.cList,False)

        for i in collisions:
            if (i.id == gi.Id.WALL):
                self.collideWall(i)

    def collideWall(self,wall):

        print("hit")

        if(self.oldx + self.player.rect.width <= wall.rect.x):
            print('collide left')
            self.player.rect.x = wall.rect.x - self.player.rect.width
        elif(self.oldx >= wall.rect.x + wall.rect.width):
            print('collide right')
            self.player.rect.x = wall.rect.x + wall.rect.width
        elif(self.oldy + self.player.rect.height <= wall.rect.y):
            print('collide top')
            self.player.rect.y = wall.rect.y - self.player.rect.height
        elif(self.oldy >= wall.rect.y + wall.rect.height):
            print('collide bottom')
            self.player.rect.y = wall.rect.y + wall.rect.height

    def checkStates(self):

        if self.frame - self.player.attackCooldownFrame > 20: #<- attack cool down
            self.player.attackCooldown = False


    def handleInputs(self, inputs, sc):

        for event in inputs:

            if event == input.Input.MOVENORTH:
                self.moveNorth()

            elif event == input.Input.MOVESOUTH:
                self.moveSouth()

            elif event == input.Input.MOVEEAST:
                self.moveEast()

            elif event == input.Input.MOVEWEST:
                self.moveWest()

            elif event == input.Input.ATTACKNORTH:
                self.attackNorth(sc)

            elif event == input.Input.ATTACKSOUTH:
                self.attackSouth(sc)

            elif event == input.Input.ATTACKEAST:
                self.attackEast(sc)

            elif event == input.Input.ATTACKWEST:
                self.attackWest(sc)


    def update(self, sc, inputs):

        self.oldx = self.player.rect.x
        self.oldy = self.player.rect.y

        self.handleInputs(sc, inputs)

        self.checkStates()
        self.checkCollision()

        self.frame += 1
