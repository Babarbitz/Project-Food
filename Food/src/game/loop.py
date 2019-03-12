## @file   loop.py
#  @title  Loop
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import pygame
import window.window as win
import input.controller as ic
from .controller import *
import player.controller as pc

def gameloop():

    isRunning = True

    window = win.Window()
    inputController = ic.EventController()
    player = pc.Player()
    spriteList = pygame.sprite.Group()

    spriteList.add(player)

    while isRunning:

        # Event handling
        inputController.handleEvents()

        if inputController.exitSignal:
            isRunning = False

        # Update game state
        gameStateController(inputController.inputs, player)

        # Update the sprites and render
        window.update(spriteList)


