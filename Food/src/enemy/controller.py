## @file   controller.py
#  @title  Enemy
#  @author Alex Lo
#  @date   April 06, 2019


# Imports
import pygame
import input
import projectile
import game
import sprite
import map
from random import randint

from .abstract import *
# image, hp, speed, damage
#ENEMYDATA = [image, 3, 3, 0]

IT_SPRITE = 'Food/assets/test.png'
IT_SIZE = (32,32)
IT_STEP = (32,32)

class EnemyController():

    # pass enemy sprite info and attack info as a list.
    def __init__(self, cList):

        self.enemies = []

        self.sprites = sprite.extractSprites(IT_SPRITE, IT_SIZE, IT_STEP)

        self.data = [[self.sprites[0], 3, 3, 1]]

        #set collision list
        self.cList = cList


    def spawnEnemies(self, sc):

       # for i in range(randint(0, 5)):
        self.enemies.append(Enemy(self.data[0], (200, 200)))
        self.enemies.append(Enemy(self.data[0], (600, 200)))
        self.enemies.append(Enemy(self.data[0], (400, 800)))
        self.renderEnemies(sc)


    def renderEnemies(self,sc):
        for enemy in self.enemies:
            sc.add(enemy)

    def setEnemyPosition(self, Enemy, x, y):
        enemy.rect.x = x
        enemy.rect.y = y


################################################################################
#                                  Movement                                    #
################################################################################


    def moveX(self, enemy, speedX):
        enemy.rect.x += speedX


    def moveY(self, enemy, speedY):
        enemy.rect.y += speedY



###############################################################################
#                           Collision Rules                                   #
###############################################################################

    def checkCollision(self, enemy):

        collisions = pygame.sprite.spritecollide(enemy, self.cList, False)

        for i in collisions:

            if (i.id == game.ID.WALL or i.id == game.ID.STRUCTURE):
                self.collideWall(enemy,i)


    def collideWall(self, enemy, wall):

        if (enemy.oldx + enemy.rect.width <= wall.rect.x):
            enemy.rect.x = wall.rect.x - enemy.rect.width

        elif (enemy.oldx >= wall.rect.x + wall.rect.width):
            enemy.rect.x = wall.rect.x + wall.rect.width

        elif (enemy.oldy + enemy.rect.height <= wall.rect.y):
            enemy.rect.y = wall.rect.y - enemy.rect.height

        elif (enemy.oldy >= wall.rect.y + wall.rect.height):
            enemy.rect.y = wall.rect.y + wall.rect.height


    def moveToPlayer(self, player, enemy):

        xDiff = player.pos[0] - enemy.rect.x
        yDiff = player.pos[1] - enemy.rect.y
        enSpeed = enemy.speed

        if (xDiff > enSpeed):
            self.moveX(enemy,enSpeed)

        elif (xDiff < -enSpeed):
            self.moveX(enemy,-enSpeed)

        elif (abs(xDiff) <= enSpeed):
            self.moveX(enemy,xDiff)

        if (yDiff > enSpeed):
            self.moveY(enemy,enSpeed)

        elif (yDiff < -enSpeed):
            self.moveY(enemy,-enSpeed)

        elif (abs(yDiff) <= enSpeed):
            self.moveY(enemy,yDiff)

    def update(self, player):

        for enemy in self.enemies:

            enemy.oldx = enemy.rect.x
            enemy.oldy = enemy.rect.y

            self.moveToPlayer(player, enemy)

            self.checkCollision(enemy)

            if enemy.hp <= 0:
                enemy.kill()

            enemy.frame += 1
