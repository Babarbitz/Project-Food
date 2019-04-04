
MU_SPRITE = 'Food/assets/menu.png'
MU_SIZE = (1280,960)
MU_STEP = (1280,960)

import pygame
import game
import map
import sprite

class MainMenuController():

    def __init__(self):

        BG = sprite.extractSprites(MU_SPRITE, MU_SIZE, MU_STEP)

        self.background = map.Background(BG[0])

        self.text = []

        self.text.append(game.Text((100,100), 'test', 18, (0,0,0)))

    def render(self, sc):

        sc.add()

