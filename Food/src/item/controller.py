from .item import *

import sprite
import random

IT_SPRITE = 'Food/assets/Coin Sprites/'
IT_SIZE = (30,36)
IT_STEP = (30,36)

class ItemController():

    def __init__(self):

        self.spritesList = [sprite.extractSprites(IT_SPRITE + "Attack up Coin.1.png", IT_SIZE, IT_STEP)[0],
        					sprite.extractSprites(IT_SPRITE + "Speed Up Coin.1.png", IT_SIZE, IT_STEP)[0],
        					sprite.extractSprites(IT_SPRITE + "Health Up Coin.1.png", IT_SIZE, IT_STEP)[0]]


        self.itemList = []

    def makeItem(self, origin, type, id, hasUse):

        if id == ID.test:
            return Item(origin, type, id, False, self.sprites[0])

    def spawnItem(self, sc, x, y):

    	type = random.randint(0,2)
    	item = Item(self.spritesList[type], type, x, y)

    	self.itemList.append(item)

    	sc.add(item)

    def pickUpItem(self, sc, item):

    	self.itemList.remove(item)

    	sc.remove(item)
    	








