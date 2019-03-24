## @file   controller.py
#  @title  Contoller
#  @author Lucas Zacharewicz
#  @date   March 03, 2019


import input.event as ie


def gameStateController(inputs, sc, player):

    # perform inputs

    handleInputs(inputs, sc, player)

    # Update Controllers

    player.update()

    # Update enemy state

    sc.updatedEntities.update()

def handleInputs(inputs, sc, player):

    for event in inputs:

        if event == ie.InputType.MOVENORTH:
            player.moveNorth()

        elif event == ie.InputType.MOVESOUTH:
            player.moveSouth()

        elif event == ie.InputType.MOVEEAST:
            player.moveEast()

        elif event == ie.InputType.MOVEWEST:
            player.moveWest()

        elif event == ie.InputType.ATTACKNORTH:
            player.attackNorth(sc)

        elif event == ie.InputType.ATTACKSOUTH:
            player.attackSouth(sc)

        elif event == ie.InputType.ATTACKEAST:
            player.attackEast(sc)

        elif event == ie.InputType.ATTACKWEST:
            player.attackWest(sc)
