## @file   controller.py
#  @title  Enemy
#  @author Alex Lo
#  @date   April 06, 2019


# Imports
import pygame
import input
import projectile

from .abstract import *

import game
import sprite
import map

class EnemyController(pygame.sprite.Sprite):

	# pass enemy sprite info and attack info as a list.
	def __init__(self, cList, enSpriteList, attkSpriteList, HP, MAXSPEED):

		super().__init__()

		#sprite constants
		EN_SPRITE = enSpriteList[0]
		EN_SIZE = enSpriteList[1]
		EN_STEP = enSpriteList[2]

		ATTK_SPRITE = attkSpriteList[0]
		ATTK_SIZE = attkSpriteList[1]
		ATTK_STEP = attkSpriteList[2]

		# get enemy sprites. idk if this is valid
		self.enSprites = sprite.extractSprites(EN_SPRITE,EN_SIZE,EN_STEP)
        self.attkSprites = sprite.extractSprites(ATTK_SPRITE,ATTK_SIZE,ATTK_STEP)

        #enemy information
        self.enemy = Enemy(self.enSprites[0], HP, MAXSPEED)

        self.oldx = 0
        self.oldy = 0

        #set ollision list
        self.cList = cList

        #create frame counter
        self.frame = 0

    def addToController(self, sc):
    	sc.add(self.enemy)

    def setPosition(self, x, y):
    	self.enemy.rect.x = x
    	self.enemy.rect.y = y


################################################################################
#                                  Movement                                    #
################################################################################


    def moveX(self, speedX):
        self.enemy.rect.x += speedX


    def moveY(self, speedY):
        self.enemy.rect.y += speedY



###############################################################################
#                           Collision Rules                                   #
###############################################################################
	
	def checkCollision(self):

		collisions = pygame.sprite.spritecollide(self.enemy, self.cList, False)

		for i in collisions:

			if (i.id == game.ID.WALL):
				self.collideWall(i)

			elif (i.id == game.ID.PLAYER):
				self.collidePlayer(i)


	def collideWall(self, wall):

		if (self.oldx + self.enemy.rect.width <= wall.rect.x):
			self.enemy.rect.x = wall.rect.x - self.enemy.rect.width

		elif(self.oldx >= wall.rect.x + wall.rect.width):
            self.enemy.rect.x = wall.rect.x + wall.rect.width

        elif(self.oldy + self.enemy.rect.height <= wall.rect.y):
            self.enemy.rect.y = wall.rect.y - self.enemy.rect.height

        elif(self.oldy >= wall.rect.y + wall.rect.height):
            self.enemy.rect.y = wall.rect.y + wall.rect.height


    #similar to collideWall. Need to check if works. 
    def collidePlayer(self, player):

    	playerX = player.pos()[0]
    	playerY = player.pos()[1]

    	if (self.oldx + self.enemy.rect.width <= playerX):
    		self.enemy.rect.x = playerX - self.enemy.rect.width

    	elif(self.oldx >= playerX + player.rect.width):
    		self.enemy.rect.x = playerX + player.rect.width  #should use getter for player width


    	if(self.oldy + self.enemy.rect.height <= playerY):
    		self.enemy.rect.y = playerY - self.enemy.rect.height

    	elif(self.oldy >= playerY + player.rect.height):
    		self.enemy.rect.y = playerY + player.rect.height


    def checkStates(self):

        if self.frame - self.enemy.attackCooldownFrame > 20: #<- attack cool down
            self.enemy.attackCooldown = False


   	def moveToPlayer(self, player):

   		xDiff = player.pos[0] - self.enemy.rect.x
    	yDiff = player.pos[1] - self.enemy.rect.y
    	enSpeed = self.enemy.speed

    	if (xDiff > enSpeed):
    		moveX(enSpeed)
    	elif (xDiff < -enSpeed):
    		moveX(-enSpeed)
    	elif (abs(xDiff) <= enSpeed):
    		moveX(xDiff)

    	if (yDiff > enSpeed):
    		moveY(enSpeed)
    	elif (yDiff < -enSpeed):
    		moveY(-enSpeed)
    	elif (abs(yDiff) <= enSpeed):
    		moveY(yDiff)


    def update(self, inputs, sc, pc):

    	self.oldx = self.enemy.rect.x
    	self.oldy = self.enemy.rect.y

    	self.moveToPlayer(player)

    	self.checkStates()
    	self.checkCollision()

    	self.frame += 1


