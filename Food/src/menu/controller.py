import pygame
import game
import sprite

from .background import *

MU_SPRITE = 'Food/assets/menu.png'
MU_SIZE = (1280,960)
MU_STEP = (1280,960)

WHITE = (255,255,255)

class MenuController():

    def __init__(self, sc, messages):

        BG = sprite.extractSprites(MU_SPRITE, MU_SIZE, MU_STEP)

        self.selection = 0

        self.sc = sc

        self.background = Background(BG[0])

        self.text = []

        i = 0

        for message in messages:
            self.text.append(game.Text((MU_SIZE[0]/2,100 + i), message, 30, WHITE))
            i += 50


    def render(self, sc):

        sc.add(self.background)

        for text in self.text:
            sc.add(text)

    def clear(self, sc):

        sc.remove(self.background)

        for text in self.text:
            sc.remove(text)

    def updateText(self):

        i = 0

        for text in self.text:

            if i == self.selection:
                text.updateColor((100,100,100))
            else:
                text.updateColor(WHITE)

            i += 1
