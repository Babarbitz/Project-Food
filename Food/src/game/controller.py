## @file   controller.py
#  @title  Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019


import input.event as ie


def gameStateController(inputs, player):

    # perform inputs

    handleInputs(inputs, player)

    # Update player state


    # Update enemy state



def handleInputs(inputs, player):

    for event in inputs:

        if event == ie.InputType.MOVENORTH:
            player.moveNorth()

        elif event == ie.InputType.MOVESOUTH:
            player.moveSouth()

        elif event == ie.InputType.MOVEEAST:
            player.moveEast()

        elif event == ie.InputType.MOVEWEST:
            player.moveWest()

