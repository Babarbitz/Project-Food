## @file   controller.py
#  @title  Event Controller
#  @author Lucas Zacharewicz
#  @date   February 21, 2019

import pygame
from .event import *
from .constants import *


class EventController:



    def __init__(self):
        self._exitSignal = False
        self._inputs = []



    def handleEvents(self):

        for event in pygame.event.get():

            # Check for exit singal
            if event.type == pygame.QUIT:
                self.exitSignal = True

            elif event.type == pygame.KEYDOWN:
                self.keyPress(event)

            elif event.type == pygame.KEYUP:
                self.keyRelease(event)



    # Handles key press events
    def keyPress(self,e):

        if e.key == KEYMOVENORTH:
            self.addInput(InputType.MOVENORTH)
            print("added move up to tape")

        elif e.key == KEYMOVESOUTH:
            self.addInput(InputType.MOVESOUTH)
            print("added move down to tape")

        elif e.key == KEYMOVEWEST:
            self.addInput(InputType.MOVEWEST)
            print("added move left to tape")

        elif e.key == KEYMOVEEAST:
            self.addInput(InputType.MOVEEAST)
            print("added move right to tape")

        elif e.key == KEYATTACKNORTH:
            self.addInput(InputType.ATTACKNORTH)
            print("added attack right to tape")

        elif e.key == KEYATTACKSOUTH:
            self.addInput(InputType.ATTACKSOUTH)
            print("added attack right to tape")

        elif e.key == KEYATTACKWEST:
            self.addInput(InputType.ATTACKWEST)
            print("added attack right to tape")

        elif e.key == KEYATTACKEAST:
            self.addInput(InputType.ATTACKEAST)
            print("added attack right to tape")

    # Handles key release events
    def keyRelease(self,e):

        if e.key == KEYMOVENORTH:
            self.removeInput(InputType.MOVENORTH)
            print("removed move up to tape")

        elif e.key == KEYMOVESOUTH:
            self.removeInput(InputType.MOVESOUTH)
            print("removed move down to tape")

        elif e.key == KEYMOVEWEST:
            self.removeInput(InputType.MOVEWEST)
            print("removed move left to tape")

        elif e.key == KEYMOVEEAST:
            self.removeInput(InputType.MOVEEAST)
            print("removed move right to tape")

        elif e.key == KEYATTACKNORTH:
            self.removeInput(InputType.ATTACKNORTH)
            print("removed attack up to tape")

        elif e.key == KEYATTACKSOUTH:
            self.removeInput(InputType.ATTACKSOUTH)
            print("removed attack down to tape")

        elif e.key == KEYATTACKWEST:
            self.removeInput(InputType.ATTACKWEST)
            print("removed attack left to tape")

        elif e.key == KEYATTACKEAST:
            self.removeInput(InputType.ATTACKEAST)
            print("removed attack right to tape")



    def addInput(self, i):
        if not i in self.inputs:
            self.inputs.append(i)



    def removeInput(self, i):
        if i in self.inputs:
            self.inputs.remove(i)


    @property
    def inputs(self):
        return self._inputs


    @property
    def exitSignal(self):
        return self._exitSignal

    @exitSignal.setter
    def exitSignal(self, val):
        self._exitSignal = val
