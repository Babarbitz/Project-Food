## @file   controller.py
#  @title  Event Controller
#  @author Lucas Zacharewicz
#  @date   February 21, 2019

import pygame
from .inputs import *


class InputController:

    # Initalizer
    def __init__(self):
        self.exitSignal = False
        self.inputs = []

    # Updates the input list with new keyboard inputs
    def gatherInputs(self, mode):

        for event in pygame.event.get():

            # Check for exit singal
            if event.type == pygame.QUIT:
                self.exitSignal = True

            elif event.type == pygame.KEYDOWN:
                self.keyPress(event,mode)

            elif event.type == pygame.KEYUP:
                self.keyRelease(event)


    # Adds inputs to the input list
    def keyPress(self, e, mode):

        if mode == 'g':

            if e.key == KEYMOVENORTH:
                self.addInput(Input.MOVENORTH)

            elif e.key == KEYMOVESOUTH:
                self.addInput(Input.MOVESOUTH)

            elif e.key == KEYMOVEWEST:
                self.addInput(Input.MOVEWEST)

            elif e.key == KEYMOVEEAST:
                self.addInput(Input.MOVEEAST)

            elif e.key == KEYATTACKNORTH:
                self.addInput(Input.ATTACKNORTH)

            elif e.key == KEYATTACKSOUTH:
                self.addInput(Input.ATTACKSOUTH)

            elif e.key == KEYATTACKWEST:
                self.addInput(Input.ATTACKWEST)

            elif e.key == KEYATTACKEAST:
                self.addInput(Input.ATTACKEAST)

            elif e.key == KEYINVENTORY:
                self.addInput(Input.INVENTORY)

            elif e.key == KEYESCAPE:
                self.addInput(Input.ESCAPE)

        elif mode == 'm':

            if e.key == KEYMOVENORTH:
                self.addInput(Input.MENUUP)

            elif e.key == KEYMOVESOUTH:
                self.addInput(Input.MENUDOWN)

            elif e.key == KEYENTER:
                self.addInput(Input.MENUSELECT)

            elif e.key == KEYINVENTORY:
                self.addInput(Input.INVENTORY)


    # Removes inputs from the input list
    def keyRelease(self, e):

        if e.key == KEYMOVENORTH:
            self.removeInput(Input.MOVENORTH)
            self.removeInput(Input.MENUUP)

        elif e.key == KEYMOVESOUTH:
            self.removeInput(Input.MOVESOUTH)
            self.removeInput(Input.MENUDOWN)

        elif e.key == KEYMOVEWEST:
            self.removeInput(Input.MOVEWEST)

        elif e.key == KEYMOVEEAST:
            self.removeInput(Input.MOVEEAST)

        elif e.key == KEYATTACKNORTH:
            self.removeInput(Input.ATTACKNORTH)

        elif e.key == KEYATTACKSOUTH:
            self.removeInput(Input.ATTACKSOUTH)

        elif e.key == KEYATTACKWEST:
            self.removeInput(Input.ATTACKWEST)

        elif e.key == KEYATTACKEAST:
            self.removeInput(Input.ATTACKEAST)

        elif e.key == KEYINVENTORY:
            self.removeInput(Input.INVENTORY)

        elif e.key == KEYESCAPE:
            self.removeInput(Input.ESCAPE)

        elif e.key == KEYENTER:
            self.removeInput(Input.MENUSELECT)

    # Adds input (i) to the tape iff it is not in the tape
    def addInput(self, i):
        if not i in self.inputs:
            self.inputs.append(i)


    # Removes input (i) from the input list iff it is in the list
    def removeInput(self, i):
        if i in self.inputs:
            self.inputs.remove(i)
