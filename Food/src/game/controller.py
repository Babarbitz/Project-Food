## @file   controller.py
#  @title  Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019


import input


def gameStateController(inputs, sc, player):

    # Update Controllers

    player.update(inputs, sc)

