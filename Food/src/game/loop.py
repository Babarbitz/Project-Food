## @file   loop.py
#  @title  Loop
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import pygame
import window.window as win
import input.controller as ic
import player.controller as pc
import sprite.controller as sc
import map.room as mr

from .controller import *

def gameloop():

    # Game loop control variable, game exits on false
    isRunning = True

    # Create game window
    window = win.Window()

    # Create input controller
    inputController = ic.EventController()

    # Create a sprite group controller
    spriteController = sc.SpriteGroupController()

    # Create Player entity
    player = pc.Player(spriteController.collidableEntities)

    # Create Room
    room = mr.Room()

    room.addToController(spriteController)

    spriteController.add(player)

    while isRunning:

        # Event handling
        inputController.handleEvents()

        if inputController.exitSignal:
            isRunning = False

        # Update game state
        gameStateController(inputController.inputs, spriteController,player)

        # Update the sprites and render
        window.update(spriteController.renderedEntities)


