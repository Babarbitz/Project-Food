## @file   controller.py
#  @title  Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

import game

def gameStateController(inputs, sc, player, projectile, map, mode):

    # Update Controllers
    if mode == game.Mode.MAINMENU:

    elif mode == game.Mode.GAME:

        player.update(inputs, sc, projectile)

        projectile.update()

        map.update(player)
