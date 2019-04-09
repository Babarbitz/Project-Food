import pygame
import game
import sprite

from .abstract import *

IN_SPRITE_FP = "Food/assets/"
IN_SIZE = (270, 270)
IN_STEP = (270, 270)

class InventoryController():

	def __init__(self):

		self.inSprites = sprite.extractSprites(IN_SPRITE_FP, IN_SIZE, IN_STEP)

		self.inventory = Inventory(self.inSprite[0])

		self.selection = 0

		self.requiredpts = 10

		self.values = []


	def render(self, sc, select):

		sc.add(self.inventory)

	def clear(self, sc):

		sc.remove(self.inventory)


	def updateSelection(self, sc, select):

		if not select = self.selection:

			self.remove(sc)
			self.add(select)

	def getInventory(self):

		return self.inventory.inventList

	def addItem(self, type):

		self.inventory.inventList[type] += 1

	def renderValues(self):


		for value in getInventory():
			self.values.append(game.Text((MU_SIZE[0]/2,100 + i), message, 30, WHITE))
            i += 50

	def spendItems(self, type, pc):

		if self.getInventory()[type] >= self.requiredpts:

			self.inventory.inventList[type] -= self.requiredpts

			if type == 0:
				pc.upgradeAttack()
			elif type == 1:
				pc.upgradeSpeed()
			elif type == 2:
				pc.upgradeHealth()


			self.updateValues()

