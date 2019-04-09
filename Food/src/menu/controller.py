import pygame
import game
import sprite

from .background import *

MU_SPRITE_FP = 'Food/assets/screen/'
MU_SIZE = (1280,960)
MU_STEP = (1280,960)

WHITE = (255,255,255)

class MenuController():

    def __init__(self, sc, messages):

        self.BG_ANIM = [Background(sprite.extractSprites(MU_SPRITE_FP + "splash1.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash2.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash3.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash4.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash5.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash6.png", MU_SIZE, MU_STEP)[0]),
                    Background(sprite.extractSprites(MU_SPRITE_FP + "splash7.png", MU_SIZE, MU_STEP)[0])]

        self.bg_index = 0

        self.selection = 0

        self.sc = sc

        #self.background = Background(BG_ANIM[self.bg_index][0])

        self.text = []

        i = 0

        '''for message in messages:
            self.text.append(game.Text((MU_SIZE[0]/2-150,700 + i), message, 50, WHITE))
            i += 50
        '''

    def render(self, sc):

        sc.add(self.BG_ANIM[self.bg_index//2])

    def clear(self, sc):

        sc.remove(self.BG_ANIM[self.bg_index//2])

        for text in self.text:
            sc.remove(text)

    def renderText(self, sc, mode):

        if mode == "main":
            self.text.append(game.Text((MU_SIZE[0]/2-200,700), "Press Enter To", 50, WHITE))
            self.text.append(game.Text((MU_SIZE[0]/2-150,750), "Start Game", 50, WHITE))

        elif mode == "pause":
            self.text.append(game.Text((MU_SIZE[0]/2-140,700), "Resume", 50, WHITE))
            self.text.append(game.Text((MU_SIZE[0]/2-170,750), "Quit Game", 50, WHITE))

        for text in self.text:
            sc.add(text)

    def animateBackground(self, sc):

        sc.remove(self.BG_ANIM[self.bg_index//2])

        self.bg_index += 1
        if self.bg_index > 13:
            self.bg_index = 0

        sc.add(self.BG_ANIM[self.bg_index//2])


    def updateText(self):

        i = 0

        for text in self.text:

            if i == self.selection:
                text.updateColor((100,100,100))
            else:
                text.updateColor(WHITE)

            i += 1
