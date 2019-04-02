## @file   loop.py
#  @title  Loop
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import pygame
import window
import input
import projectile
import player
import sprite
import map

from .controller import *

def gameloop():

    # Game loop control variable, game exits on false
    isRunning = True

    # Create controllers

    inputController      = input.InputController()
    spriteController     = sprite.SpriteGroupController()
    windowController     = window.Window()

    mapController        = map.MapController(spriteController)
    playerController     = player.PlayerController(spriteController.collidableEntities)
    projectileController = projectile.ProjectileController(spriteController)



    # Do pregame setup

    mapController.currentRoom.render(spriteController)

    playerController.addToController(spriteController)
    playerController.setPosition(400,400)


    while isRunning:

        # Event handling
        inputController.gatherInputs()

        if inputController.exitSignal:
            isRunning = False

        # Update game state
        gameStateController(inputController.inputs,
                            spriteController,
                            playerController,
                            projectileController,
                            mapController)

        # Update the sprites and render
        windowController.update(spriteController.renderedEntities)
