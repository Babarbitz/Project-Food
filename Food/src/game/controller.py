## @file   controller.py
#  @title  Game Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

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
        self.gameLoop = True
        self.mainMenuLoop = True
        self.menuLoop = True


        # Low level engine modules
        self.inputController      = input.InputController()
        self.spriteController     = sprite.SpriteGroupController()
        self.windowController     = window.Window()

        # game modules
        self.mapController        = map.MapController(self.spriteController)
        self.mainMenu             = menu.MenuController(self.spriteController,
                                                        ['New Game', 'Load Game'])
        self.playerController     = player.PlayerController(self.spriteController.collidableEntities)
        self.projectileController = projectile.ProjectileController(self.spriteController)

    def start(self):

        self.startMenu()
        self.setup()
        self.game()

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


    def game(self):


        while self.gameLoop:

            # Event handling
            self.inputController.gatherInputs('g')

            if self.inputController.exitSignal:
                self.gameLoop = False

            # Update game state
            self.gameStateUpdate(self.inputController.inputs)

            # Update the sprites and render
            self.windowController.update(self.spriteController.renderedEntities)


    def PauseMenu(self):

        self.menuController.render()

        while self.mainMenuLoop:

            # Event handling
            self.inputController.gatherInputs('m')

            if self.inputController.exitSignal:
                self.mainMenuLoop = False

            for event in self.inputController.inputs:
                if event == input.Input.MENUUP:
                    self.menuController.selection = 0
                elif event == input.Input.MENUDOWN:
                    self.menuController.selection = 1
                elif event == input.Input.MENUSELECT:
                    print("enter")
                    if self.menuController.selection == 0:
                        print("new game")
                    else:
                        print("load game")

    def startMenu(self):

        self.mainMenu.render()

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
                    print("enter")
                    if self.mainMenu.selection == 0:
                        print("new game")
                    else:
                        print("load game")

            # Update game state
            self.mainMenu.updateText()

            # Update the sprites and render
            self.windowController.update(self.spriteController.renderedEntities)
