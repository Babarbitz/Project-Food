## @file   __main__.py
#  @title  Main game file
#  @author Lucas Zacharewicz
#  @date   February 19, 2019

###########
# Imports #
###########

import pygame
import game.loop as gl


## @brief  Entering point of the game.
#  @detail Creates game window object and handles pygame.quit
def main():

    # Initialize pygame
    pygame.init()

    # Run game
    gl.gameloop()

    # IO output
    print("Exited game successfully")

    # Quit pygame
    pygame.quit()

if __name__=="__main__":
    main()
