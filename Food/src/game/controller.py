## @file   controller.py
#  @title  Game Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

import window
import input
import projectile
import player
import sprite
import map

class GameController():

    def __init__(self):

        # Game loop control variable
        self.isRunning = True

        # Low level engine modules
        self.inputController      = input.InputController()
        self.spriteController     = sprite.SpriteGroupController()
        self.windowController     = window.Window()

        # game modules
        self.mapController        = map.MapController(self.spriteController)
        self.playerController     = player.PlayerController(self.spriteController.collidableEntities)
        self.projectileController = projectile.ProjectileController(self.spriteController)

    def start(self):

        self.setup()
        self.gameLoop()

    def setup(self):

        # Map
        self.mapController.currentRoom.render(self.spriteController)

        # Player
        self.playerController.addToController(self.spriteController)
        self.playerController.setPosition(400,400)

    def gameStateUpdate(self, inputs):

        # Update Controllers

        self.playerController.update(inputs,
                                     self.spriteController,
                                     self.projectileController)

        self.projectileController.update()

        self.mapController.update(self.playerController)


    def gameLoop(self):


        while self.isRunning:

            # Event handling
            self.inputController.gatherInputs()

            if self.inputController.exitSignal:
                self.isRunning = False

            # Update game state
            self.gameStateUpdate(self.inputController.inputs)

            # Update the sprites and render
            self.windowController.update(self.spriteController.renderedEntities)


