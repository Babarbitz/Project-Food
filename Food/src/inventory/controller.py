import pygame
import game
import sprite

from .abstract import *

IN_SPRITE_FP = "Food/assets/Inventory/"
IN_SIZE = (580, 448)
IN_STEP = (580, 448)

WHITE = (255,255,255)

class InventoryController():

	def __init__(self):

		self.inSprites = sprite.extractSprites(IN_SPRITE_FP + "inventory.1.png", IN_SIZE, IN_STEP)

		self.inventory = Inventory(self.inSprites[0])

		self.inSpriteSelectList =  [Inventory(sprite.extractSprites(IN_SPRITE_FP + "swordselect.png", IN_SIZE, IN_STEP)[0]),
									Inventory(sprite.extractSprites(IN_SPRITE_FP + "bootselect.png", IN_SIZE, IN_STEP)[0]),
									Inventory(sprite.extractSprites(IN_SPRITE_FP + "heartselect.png", IN_SIZE, IN_STEP)[0])]

		self.selection = 0

		self.requiredpts = 10

		self.values = []


	def render(self, sc):

		self.addValues()

		sc.add(self.inSpriteSelectList[self.selection])

		for value in self.values:
			sc.add(value)

	def clear(self, sc):

		sc.remove(self.inSpriteSelectList[self.selection])

		for value in self.values:
			sc.remove(value)

		self.values = []


	def updateSelection(self, sc, direction):

		self.clear(sc)

		self.selection += -direction

		if self.selection > 2:
			self.selection = 0
		elif self.selection < 0:
			self.selection = 2

		self.render(sc)

	def getInventory(self):

		return self.inventory.inventList

	def addItem(self, type):

		self.inventory.inventList[type] += 1

	def addValues(self):

		i = 0
		for value in self.getInventory():
			self.values.append(game.Text((780,260 + i), str(value)+'/'+str(self.requiredpts), 50, WHITE))
			i += 140


	def spendItems(self, pc):

		if self.getInventory()[self.selection] >= self.requiredpts:

			self.inventory.inventList[self.selection] -= self.requiredpts

			if type == 0:
				pc.upgradeAttack()
			elif type == 1:
				pc.upgradeSpeed()
			elif type == 2:
				pc.upgradeHealth()


			#self.updateValues()

