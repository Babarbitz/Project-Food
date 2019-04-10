## @file   identifiers.py
#  @title  Identifier object
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

from enum import Enum

class ID(Enum):
    PLAYER      = 1
    ENEMY       = 2
    STRUCTURE   = 3
    DOOR        = 4
    WALL        = 5
    PROJECTILE  = 6
    BACKGROUND  = 7
    TEXT        = 8
    MENU        = 9
    INVENT      = 10

class Mode(Enum):
    MAINMENU  = 1
    GAME      = 2
    PAUSE     = 3
    INVENTORY = 4
