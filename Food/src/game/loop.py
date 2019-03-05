## @file   loop.py
#  @title  Loop
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import window.window as win
import input.controller as ic
from .controller import *


def gameloop():

    isRunning = True

    window = win.Window()
    inputController = ic.EventController()



    while isRunning:

        # Event handling
        inputController.handleEvents()

        if inputController.exitSignal:
            isRunning = False

        # Update game state
        gameStateController(inputController.inputs)

        # Update the sprites and render
        window.update([])


