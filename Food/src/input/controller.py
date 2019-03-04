## @file   controller.py
#  @title  Event Controller
#  @author Lucas Zacharewicz
#  @date   February 21, 2019

import pygame
from .event import *
from .constants import *


class EventController:



    def __init__(self):
        self.exitSignal = False
        self.inputs = []



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

        if e.key == KEYUP:
            self.addInput(InputType.MOVENORTH)
            print("added key up to tape")

        elif e.key == KEYDOWN:
            self.addInput(InputType.MOVESOUTH)
            print("added key down to tape")

        elif e.key == KEYLEFT:
            self.addInput(InputType.MOVEEAST)
            print("added key left to tape")

        elif e.key == KEYRIGHT:
            self.addInput(InputType.MOVEWEST)
            print("added key right to tape")



    # Handles key release events
    def keyRelease(self,e):

        if e.key == KEYUP:
            self.removeInput(InputType.MOVENORTH)
            print("removed key up to tape")

        elif e.key == KEYDOWN:
            self.removeInput(InputType.MOVESOUTH)
            print("removed key down to tape")

        elif e.key == KEYLEFT:
            self.removeInput(InputType.MOVEEAST)
            print("removed key left to tape")

        elif e.key == KEYRIGHT:
            self.removeInput(InputType.MOVEWEST)
            print("removed key right to tape")




    def addInput(self, i):
        if not i in self.inputs:
            self.inputs.append(i)



    def removeInput(self, i):
        if i in self.inputs:
            self.inputs.remove(i)

