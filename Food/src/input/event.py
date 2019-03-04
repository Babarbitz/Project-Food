
## @file   event.py
#  @title  Event object
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

from enum import Enum

class InputType(Enum):
    MOVENORTH = 1
    MOVESOUTH = 2
    MOVEEAST  = 3
    MOVEWEST  = 4
