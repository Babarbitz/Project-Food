
## @file   event.py
#  @title  Event object
#  @author Lucas Zacharewicz
#  @date   March 03, 2019

###########
# Imports #
###########

from enum import Enum


class Event(Enum):
    MOVENORTH = 1
    MOVESOUTH = 2
    MOVEEAST  = 3
    MOVEWEST  = 4
