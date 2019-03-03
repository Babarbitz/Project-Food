## @file   eventcontroller.py
#  @title  Event Controller
#  @author Lucas Zacharewicz
#  @date   February 21, 2019

import pygame

class eventcontroller:

    def __init__(self):
        self.exitSignal = False

    def handleEvents(self):

        for event in pygame.event.get():

            # Check for exit singal
            if event.type == pygame.QUIT:
                self.exitSignal = True

            elif event.type == pygame.KEYDOWN:
                self.keypress(event)

            elif event.type == pygame.KEYUP:
                self.keyrelease(event)


    # Handles key press events
    def keypress(self,e):
        pass

    # Handles key release events
    def keyrelease(self,e):
        pass
