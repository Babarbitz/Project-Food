from .item import *

import sprite

IT_SPRITE = 'Food/src/assets/test.png'
IT_SIZE = (32,32)
IT_STEP = (32,32)

class itemController():

    def __init__(self):

        self.sprites = sprite.extractor(IT_SPRITE, IT_SIZE, IT_STEP)

    def makeItem(self, origin, type, id, hasUse):

        if id == ID.test:
            return Item(origin, type, id, False, self.sprites[0])



