## @file   room.py
#  @title  Room
#  @author Lucas Zacharewicz
#  @date   March 17, 2019

from .entities import *
from .identifiers import *

DOOR_SPRITE = 'Food/assets/door.png'
DOOR_SIZE = (512,128)
DOOR_STEP = (128,128)


class Room():

    def __init__(self, pos, doors):

        # Position in map
        self.position = pos

        BG = sprite.extractSprites(BG_SPRITE, BG_SIZE, BG_STEP)

        # Room background Image
        self.background = Background(BG[0])

        # TODO: Refactor to make not hardcoded
        # Room Wall collison
        self.walls = []
        self.walls.append(Wall([0,0],[128,896]))
        self.walls.append(Wall([0,0],[1280,128]))
        self.walls.append(Wall([1152,0],[128,896]))
        self.walls.append(Wall([0,768],[1280,128]))


        # structures
        self.structures = []

        # enemies

        # doors
        self.doors = addDoors(doors)


    def render(self, sc):

        sc.add(self.background)


        for wall in self.walls:
            sc.add(wall)

        for structure in self.structures:
            sc.add(structure)

        for door in self.doors:
            sc.add(door)

    def clearRoom(self, sc):

        sc.remove(self.background)

        for wall in self.walls:
            sc.remove(wall)

        for structure in self.structures:
            sc.remove(structure)

        for door in self.doors:
            sc.remove(door)



def addDoors(doors):


    Sprites = sprite.extractSprites(DOOR_SPRITE, DOOR_SIZE, DOOR_STEP)

    doorList = []

    # North door
    if doors[0]:
        doorList.append(Door(Sprites[0],(BG_SIZE[0]/2 - DOOR_STEP[0] / 2,11), ID.NORTH))

    # South door
    if doors[1]:
        doorList.append(Door(Sprites[1],(BG_SIZE[0]/2 -
            DOOR_STEP[0]/2,BG_SIZE[1] - 13 - DOOR_STEP[0]), ID.SOUTH))

    # East door
    if doors[2]:
        doorList.append(Door(Sprites[2],(BG_SIZE[0] - 12 - DOOR_STEP[0],BG_SIZE[1]/2 - DOOR_STEP[1]/2), ID.EAST))

    # West door
    if doors[3]:
        doorList.append(Door(Sprites[3],(11,BG_SIZE[1]/2 - DOOR_STEP[1]/2), ID.WEST))

    return doorList
