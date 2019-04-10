## @file   controller.py
#  @title  Player
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


# Imports
import pygame
import input
import projectile
import random

from .abstract import *

import game
import sprite
import map


# Constants
PR_SPRITE = 'Food/assets/knife.png'
PR_SPEED = 8
PR_STEP = (32,32)
PR_SIZE = (128,32)


PL_SPRITE = 'Food/assets/Chef.png'
PL_STEP = (64,64)
PL_SIZE = (64,64)

PL_SOUNDS = 'Food/assets/sound/Player Sounds/'

# Centers the sprite in the view
OFFSET = (PL_STEP[0]/2) - (PR_STEP[0]/2)


class PlayerController(pygame.sprite.Sprite):

################################################################################
#                                 Initializer                                  #
################################################################################


    def __init__(self, cList, mixer):

        # Call parent constructor
        super().__init__()

        # Get sprites
        self.plSprites = sprite.extractSprites(PL_SPRITE,PL_SIZE,PL_STEP)
        self.prSprites = sprite.extractSprites(PR_SPRITE,PR_SIZE,PR_STEP)

        # Player information
        self.player = Player(self.plSprites[0])

        self.oldx = 0
        self.oldy = 0

        # Set Collision list
        self.cList = cList

        # Create Frame Counter
        self.frame = 0

        # sound mixer
        self.mixer = mixer
        self.invincbleFrame = 0

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


    def attackNorth(self, sc, pc):

        self.attack(self.player.rect.x + OFFSET,
                    self.player.rect.y,
                    0,
                    -PR_SPEED,
                    self.prSprites[0],
                    sc,
                    pc)


    def attackSouth(self, sc, pc):

        self.attack(self.player.rect.x + OFFSET,
                    self.player.rect.y + PL_STEP[0],
                    0,
                    PR_SPEED,
                    self.prSprites[1],
                    sc,
                    pc)


    def attackWest(self, sc, pc):

        self.attack(self.player.rect.x,
                    self.player.rect.y + OFFSET,
                    -PR_SPEED,
                    0,
                    self.prSprites[2],
                    sc,
                    pc)


    def attackEast(self, sc, pc):

        self.attack(self.player.rect.x + PL_STEP[0],
                    self.player.rect.y + OFFSET,
                    PR_SPEED,
                    0,
                    self.prSprites[3],
                    sc,
                    pc)


    def attack(self, x, y, xs, ys, sprite, sc, pc):

        if not self.player.attackCooldown:
            self.attackSound()
            temp = projectile.Projectile(x, y, xs, ys, sprite, self.cList,
                    self.player.attack)
            sc.add(temp)
            pc.addProjectile(temp)
            self.player.attackCooldown = True
            self.player.attackCooldownFrame = self.frame


    def attackSound(self):

        rand_sound = random.randint(1, 3)

        if (rand_sound == 1):
            self.mixer.playSoundEffect(PL_SOUNDS + "Knife_Throw_2.1.ogg")

        elif (rand_sound == 2):
            self.mixer.playSoundEffect(PL_SOUNDS + "Knife_Throw_3.1.ogg")

        else:
            self.mixer.playSoundEffect(PL_SOUNDS + "Knife_Throw_4.1.ogg")


###############################################################################
#                           Collision Rules                                   #
###############################################################################

    def checkItems(self, sc, it_c, in_c):

        for item in it_c.itemList:
            #print(abs(self.player.rect.x - item.pos()[0]) < 5, "and", abs(self.player.rect.y - item.pos()[1]) < 5)

            if (abs(self.player.rect.x + OFFSET - item.pos()[0]) < 15 and abs(self.player.rect.y + PL_STEP[0] - item.pos()[1]) < 15):
                print("pickup")
                it_c.pickUpItem(sc, item)

                type = item.type
                in_c.addItem(type)

    def checkCollision(self):

        collisions = pygame.sprite.spritecollide(self.player,self.cList,False)

        for i in collisions:

            if (i.id == game.ID.WALL or i.id == game.ID.STRUCTURE):
                self.collideWall(i)

            elif (i.id == game.ID.ENEMY):
                self.player.hp -= i.damage


    def collideWall(self,wall):

        if(self.oldx + self.player.rect.width <= wall.rect.x):
            self.player.rect.x = wall.rect.x - self.player.rect.width

        elif(self.oldx >= wall.rect.x + wall.rect.width):
            self.player.rect.x = wall.rect.x + wall.rect.width

        elif(self.oldy + self.player.rect.height <= wall.rect.y):
            self.player.rect.y = wall.rect.y - self.player.rect.height

        elif(self.oldy >= wall.rect.y + wall.rect.height):
            self.player.rect.y = wall.rect.y + wall.rect.height


    def collideDoor(self, door):

        if door.type == map.ID.NORTH:
            self.setPosition(  map.BG_SIZE[0]/2
                             - PL_SIZE[0]/2 ,
                               map.BG_SIZE[1]
                             - 150
                             - PL_SIZE[1])

        elif door.type == map.ID.SOUTH:
            self.setPosition(  map.BG_SIZE[0]/2
                             - PL_SIZE[0]/2 ,
                               150)

        elif door.type == map.ID.EAST:
            self.setPosition(  150,
                               map.BG_SIZE[1]/2
                             - PL_SIZE[1]/2)

        elif door.type == map.ID.WEST:
             self.setPosition( map.BG_SIZE[0]
                             - 150
                             - PL_SIZE[0],
                               map.BG_SIZE[1]/2
                             - PL_SIZE[1]/2)
    def checkStates(self):

        if self.frame - self.player.attackCooldownFrame > 20: #<- attack cool down
            self.player.attackCooldown = False


    def handleInputs(self, inputs, sc, pc):

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
                self.attackNorth(sc, pc)

            elif event == input.Input.ATTACKSOUTH:
                self.attackSouth(sc, pc)

            elif event == input.Input.ATTACKEAST:
                self.attackEast(sc, pc)

            elif event == input.Input.ATTACKWEST:
                self.attackWest(sc, pc)

    def upgradeAttack(self):
        self.player.attack += 1

    def upgradeHP(self):
        self.player.maxHp+= 1

    def upgradeSpeed(self):
        self.player.speed += 1

    def update(self, inputs, sc, pc, it_c, in_c):

        self.oldx = self.player.rect.x
        self.oldy = self.player.rect.y

        self.handleInputs(inputs, sc, pc)

        self.checkStates()
        self.checkCollision()
        self.checkItems(sc, it_c, in_c)

        if self.player.hp <= 0:
            self.player.kill()

        self.frame += 1
