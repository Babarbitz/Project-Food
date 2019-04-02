## @file   controller.py
#  @title  Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019


def gameStateController(inputs, sc, player, projectile, map):

    # Update Controllers


    player.update(inputs, sc, projectile)

    projectile.update()

    map.update(player)
