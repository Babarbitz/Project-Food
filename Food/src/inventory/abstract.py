
import pygame
import game

class Inventory(pygame.sprite.Sprite):

	def __init__(self, image):

		super().__init__()

		self.image = image
		self.rect = self.image.get_rect()

		self.id = game.ID.INVENT

		self.renderable = True
		self.updatable = False
		self.collidable = False

		self.inventList = [0, 0, 10]

		self.rect.x = 350
		self.rect.y = 200

	def getInventory(self):

		return self.inventList

	def addItem(self, type):

		self.inventList[type] += 1

	def spendItems(self, type):

		self.inventList[type] = 0

	