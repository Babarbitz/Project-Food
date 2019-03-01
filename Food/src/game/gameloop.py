## @file   gameloop.py
#  @title  GameLoop
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

import window.window as win
import game.eventcontroller as ec
from .gamestate import *
from .render import *


def gameloop():

    isRunning = True

    window = win.Window()
    inputController = ec.eventcontroller()



    while isRunning:

        # Event handling
        inputController.handleEvents()

        # Update game state


        # Update the sprites and render
        window.update()
