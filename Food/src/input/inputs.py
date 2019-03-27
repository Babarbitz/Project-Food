## @file   inputs.py
#  @title  Input Information
#  @author Lucas Zacharewicz
#  @date   March 27, 2019

import pygame as p
from enum import Enum

# Constants for keycodes
KEYMOVENORTH   = p.K_e
KEYMOVESOUTH   = p.K_d
KEYMOVEWEST    = p.K_s
KEYMOVEEAST    = p.K_f
KEYATTACKNORTH = p.K_i
KEYATTACKSOUTH = p.K_k
KEYATTACKWEST  = p.K_j
KEYATTACKEAST  = p.K_l

# A simple enumerable type for identifying different player actions.
class Input(Enum):

    MOVENORTH = 1
    MOVESOUTH = 2
    MOVEEAST  = 3
    MOVEWEST  = 4
    ATTACKNORTH = 5
    ATTACKSOUTH = 6
    ATTACKEAST  = 7
    ATTACKWEST  = 8
