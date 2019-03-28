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

    # Create game window
    windowController = window.Window()

    # Create input controller
    inputController = input.InputController()

    # Create a sprite group controller
    spriteController = sprite.SpriteGroupController()

    # Create Player entity
    playerController = player.PlayerController(spriteController.collidableEntities)

    # Create projectile controller
    projectileController = projectile.ProjectileController(spriteController.collidableEntities)

    # Create Room
    room = map.Room()

    room.render(spriteController)

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
                            projectileController)

        # Update the sprites and render
        windowController.update(spriteController.renderedEntities)
