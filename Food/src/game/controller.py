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
import music
import inventory

#Constants
MUSIC_FP = "Food/assets/sound/Game_Music/"
M_MENU_SOUNDS_FP = "Food/assets/sound/Main_Menu_Sounds/"
P_MENU_SOUNDS_FP = "Food/assets/sound/Pause Menu Sounds/"

class GameController():

    def __init__(self):

        # Game loop control variables
        self.isRunning = False
        self.gameLoop = False
        self.mainMenuLoop = True
        self.pauseMenuLoop = False
        self.inventoryLoop = False


        # Low level engine modules
        self.inputController      = input.InputController()
        self.spriteController     = sprite.SpriteGroupController()
        self.windowController     = window.Window()

        # music/sound module
        self.mixer                = music.MixerController()

        # game modules
        self.mapController        = map.MapController(self.spriteController)
        self.mainMenu             = menu.MenuController(self.spriteController,
                                                        ['Press Enter To Start Game'])
        self.pauseMenu            = menu.MenuController(self.spriteController,
                                                        ['Resume', 'Save and Quit'])
        self.playerController     = player.PlayerController(self.spriteController.collidableEntities, self.mixer)
        self.projectileController = projectile.ProjectileController(self.spriteController)
        self.enemyController      = enemy.EnemyController(self.spriteController.collidableEntities)
        self.inventoryController  = inventory.InventoryController()

    def start(self):
        self.startMenu()

    def setup(self):

        # Music
        self.mixer.stopMusic()
        self.mixer.loadMusic(MUSIC_FP + "Game_Music.ogg")
        self.mixer.playMusic()

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
                elif event == input.Input.INVENTORY:
                    print("bring up inventory")
                    self.inventoryLoop = True
                    self.InventoryMenu()

            # Update game state
            self.gameStateUpdate(self.inputController.inputs)

    def PauseMenu(self):

        self.mixer.playSoundEffect(P_MENU_SOUNDS_FP + "PauseMenu_Select_Option.1.ogg")
        self.mixer.pauseMusic()

        self.pauseMenu.renderText(self.spriteController, "pause")

        while self.pauseMenuLoop:

            self.pauseMenu.animateBackground(self.spriteController)

            self.inputController.gatherInputs('m')

            for event in self.inputController.inputs:

                if event == input.Input.MENUUP:
                    self.mixer.playSoundEffect(P_MENU_SOUNDS_FP + "PauseMenu_Switch_Option.1.ogg")
                    self.pauseMenu.selection = 0

                elif event == input.Input.MENUDOWN:
                    self.mixer.playSoundEffect(P_MENU_SOUNDS_FP + "PauseMenu_Switch_Option.1.ogg")
                    self.pauseMenu.selection = 1

                elif event == input.Input.MENUSELECT:

                    self.mixer.playSoundEffect(P_MENU_SOUNDS_FP + "PauseMenu_Select_Option.1.ogg")

                    self.pauseMenu.clear(self.spriteController)
                    self.pauseMenuLoop = False

                    if self.pauseMenu.selection == 0:
                        self.mixer.playSoundEffect(P_MENU_SOUNDS_FP + "PauseAndUnPauseGame.ogg")
                        self.mixer.resumeMusic()
                        self.gameLoop = True
                    else:
                        self.gameLoop = False
                        self.isRunning = False

            # Update game state
            self.pauseMenu.updateText()
            # Update the sprites and render
            self.windowController.update(self.spriteController)


    def startMenu(self):

        self.mainMenu.renderText(self.spriteController, "main")
        self.mainMenu.render(self.spriteController)

        #play main menu music
        self.mixer.stopMusic()
        self.mixer.loadMusic(MUSIC_FP + "Main_Menu_Song.ogg")
        self.mixer.playMusic()

        while self.mainMenuLoop:

            self.mainMenu.animateBackground(self.spriteController)
            # Event handling
            self.inputController.gatherInputs('m')

            if self.inputController.exitSignal:
                self.mainMenuLoop = False

            for event in self.inputController.inputs:

                '''
                if event == input.Input.MENUUP:
                    self.mixer.playSoundEffect(M_MENU_SOUNDS_FP + "Menu_Switch_Option.ogg")
                    self.mainMenu.selection = 0

                elif event == input.Input.MENUDOWN:
                    self.mixer.playSoundEffect(M_MENU_SOUNDS_FP + "Menu_Switch_Option.ogg")
                    self.mainMenu.selection = 1
                '''

                if event == input.Input.MENUSELECT:
                    self.mixer.playSoundEffect(M_MENU_SOUNDS_FP + "Menu_Select_Option.ogg")

                    self.mainMenuLoop = False
                    self.mainMenu.clear(self.spriteController)

                    if self.mainMenu.selection == 0:
                        self.setup()
                    else:
                        print("load game")

            # Update game state
            #self.mainMenu.updateText()

            # Update the sprites and render
            self.windowController.update(self.spriteController)


    def InventoryMenu(self):

        self.inventoryController.render(self.spriteController)
