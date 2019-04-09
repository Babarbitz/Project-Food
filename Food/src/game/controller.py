## @file   controller.py
#  @title  Game Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

import enemy
import input
import map
import menu
import projectile
import player
import sprite
import window

class GameController():

    def __init__(self):

        # Game loop control variables
        self.isRunning = False
        self.gameLoop = False
        self.mainMenuLoop = True
        self.pauseMenuLoop = False


        # Low level engine modules
        self.inputController      = input.InputController()
        self.spriteController     = sprite.SpriteGroupController()
        self.windowController     = window.Window()

        # game modules
        self.mapController        = map.MapController(self.spriteController)
        self.mainMenu             = menu.MenuController(self.spriteController,
                                                        ['New Game', 'Load Game'])
        self.pauseMenu            = menu.MenuController(self.spriteController,
                                                        ['Resume', 'Save and Quit'])
        self.playerController     = player.PlayerController(self.spriteController.collidableEntities)
        self.projectileController = projectile.ProjectileController(self.spriteController)
        self.enemyController      = enemy.EnemyController(self.spriteController.collidableEntities)

    def start(self):
        self.startMenu()

    def setup(self):

        # Map
        self.mapController.generateMap()
        self.mapController.currentRoom.render(self.spriteController)
        self.enemyController.spawnEnemies(self.spriteController)

        # Player
        self.playerController.addToController(self.spriteController)
        self.playerController.setPosition(400,400)

        self.game()

    def gameStateUpdate(self, inputs):

        # Update Controllers

        self.playerController.update(inputs,
                                     self.spriteController,
                                     self.projectileController)

        self.projectileController.update()

        self.mapController.update(self.playerController)
        self.enemyController.update(self.playerController.player)

    def game(self):

        self.isRunning = True
        self.gameLoop = True

        while self.isRunning:

            if self.inputController.exitSignal:
                isRunning = False

            self.gameloop()

            # Update the sprites and render
            self.windowController.update(self.spriteController)

    def gameloop(self):

        if self.gameLoop:

            # Event handling
            self.inputController.gatherInputs('g')

            for event in self.inputController.inputs:
                if event == input.Input.ESCAPE:
                    print("shouldpause")
                    self.pauseMenuLoop = True
                    self.gameLoop = False
                    self.PauseMenu()

            # Update game state
            self.gameStateUpdate(self.inputController.inputs)

    def PauseMenu(self):

        self.pauseMenu.render(self.spriteController)

        while self.pauseMenuLoop:

            self.inputController.gatherInputs('m')

            for event in self.inputController.inputs:

                if event == input.Input.MENUUP:
                    self.pauseMenu.selection = 0

                elif event == input.Input.MENUDOWN:
                    self.pauseMenu.selection = 1

                elif event == input.Input.MENUSELECT:

                    self.pauseMenu.clear(self.spriteController)
                    self.pauseMenuLoop = False

                    if self.pauseMenu.selection == 0:
                        self.gameLoop = True
                    else:
                        self.gameLoop = False
                        self.isRunning = False

            # Update game state
            self.pauseMenu.updateText()
            # Update the sprites and render
            self.windowController.update(self.spriteController)


    def startMenu(self):

        self.mainMenu.render(self.spriteController)

        while self.mainMenuLoop:

            # Event handling
            self.inputController.gatherInputs('m')

            if self.inputController.exitSignal:
                self.mainMenuLoop = False

            for event in self.inputController.inputs:

                if event == input.Input.MENUUP:
                    self.mainMenu.selection = 0

                elif event == input.Input.MENUDOWN:
                    self.mainMenu.selection = 1

                elif event == input.Input.MENUSELECT:

                    self.mainMenuLoop = False
                    self.mainMenu.clear(self.spriteController)

                    if self.mainMenu.selection == 0:
                        self.setup()
                    else:
                        print("load game")

            # Update game state
            self.mainMenu.updateText()

            # Update the sprites and render
            self.windowController.update(self.spriteController)
