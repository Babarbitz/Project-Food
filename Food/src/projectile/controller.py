## @file   controller.py
#  @title  Projectile Controller
#  @author Lucas Zacharewicz
#  @date   March 08, 2019


import pygame
import game

from .abstract import *

class ProjectileController():


    def __init__(self, cList):

        self.projectiles = []
        self.cList = cList

    def addProjectile(self, p):

        self.projectiles.append(p)

    def remove(self, p):

        self.projectiles.remove(p)

    def moveProjectiles(self):

        for p in self.projectiles:
            p.rect.x += p.xspeed
            p.rect.y += p.yspeed


    def checkCollision(self):

        for p in self.projectiles:

            collisions = pygame.sprite.spritecollide(p, self.cList, False)

            for c in collisions:
                if (c.id == game.ID.WALL):
                    self.remove(p)
                    p.kill()


    def update(self):

        self.moveProjectiles()
        self.checkCollision()
