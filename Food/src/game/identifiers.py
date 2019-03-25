## @file   identifiers.py
#  @title  Identifier object
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

from enum import Enum

class Id(Enum):
    PLAYER      = 1
    ENEMY       = 2
    STRUCTURE   = 3
    WALL        = 4
    PROJECTILE  = 5

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST  = 3
    WEST  = 4
