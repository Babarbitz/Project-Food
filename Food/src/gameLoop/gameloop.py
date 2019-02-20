## @file   gameloop.py
#  @title  GameLoop object for running the game
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

from window.window import *


## @brief Runs the main gameloop, handles events, updates state, and
#         renders scenes.

class GameLoop:

    def __init__(self):
        
        # Game window
        self.window = Window()

    def run(self):
        
        isRunning = True

        while isRunning:
            # Event handling

            # Update game state

            # Update the sprites and render

            self.window.update()
