import pygame
import random
import sprite

from .room import *

BG_SPRITES = ['Food/assets/Backgrounds/dungeon.png',
              'Food/assets/Backgrounds/restaurant.png',
              'Food/assets/Backgrounds/woods.png']

DR_SPRITES = ['Food/assets/DoorSprites/DungeonDoor.png',
              'Food/assets/DoorSprites/RestaurantDoor.png',
              'Food/assets/DoorSprites/WoodsDoor.png']

BG_SIZE = (1280,896)
DR_SIZE = (2048,2304)

class MapController():

    def __init__(self, sc):

        self.map = []
        self.level = 0

        self.currentRoom = None
        self.sc = sc

        self.gameEnd = False

        self.BGSPRITES = []
        self.DOORSPRITES = []

        # Sprites
        for sheet in BG_SPRITES:
            temp = sprite.extractSprites(sheet, BG_SIZE, BG_SIZE)
            self.BGSPRITES.append(temp[0])

        for sheet in DR_SPRITES:
            temp = sprite.extractSprites(sheet, DR_SIZE, DR_SIZE)
            temp = pygame.transform.scale(temp[0],(128,128))
            north = temp
            south = pygame.transform.rotate(temp, -180)
            east = pygame.transform.rotate(temp, -90)
            west = pygame.transform.rotate(temp, -270)
            self.DOORSPRITES.append([north,south,east,west])


    def checkRoomTransition(self, pc, ec):

        for door in self.currentRoom.doors:
            collisions = pygame.sprite.spritecollide(door,
                                                     self.sc.collidableEntities,
                                                     False)

            for i in collisions:
                if (i.id == game.ID.PLAYER):
                    pc.collideDoor(door)
                    self.transition(door.type, ec)

    def checkLevelTransition(self, pc):
        for s in self.currentRoom.structures:
            collisions = pygame.sprite.spritecollide(s,
                                                     self.sc.collidableEntities,
                                                     False)
            for i in collisions:
                if (i.id == game.ID.PLAYER):
                    pc.setPosition(400,400)
                    self.currentRoom.clearRoom(self.sc)
                    self.level += 1
                    if self.level > 2:
                        self.gameEnd = True
                    else:
                        self.generateMap()


    def transition(self, direction, ec):

        position = self.currentRoom.position
        self.currentRoom.clearRoom(self.sc)

        i = position[0]
        j = position[1]

        if direction == ID.NORTH:
            self.currentRoom = self.map[i + 5 * (j - 1)]

        if direction == ID.SOUTH:
            self.currentRoom = self.map[i + 5 * (j + 1)]

        if direction == ID.EAST:
            self.currentRoom = self.map[(i + 1) + 5 * j]

        if direction == ID.WEST:
            self.currentRoom = self.map[(i - 1) + 5 * j]

        ec.killall(self.sc)
        ec.spawnEnemies(self.sc, self.level)
        self.currentRoom.render(self.sc)
        print(self.currentRoom.position)

    def generateMap(self):

        # Pick a layout

        self.map = []

        layout = self.generateLayout()


        # Place rooms based on layout

        count = 0
        for room in layout:

            i = count  % 5
            j = count // 5

            pos = (i, j)

            doors = []


            # Check North room
            try:
                if layout[i + 5 * (j - 1)] != 'n':
                    doors.append(True)
                else:
                    doors.append(False)
            except IndexError:
                doors.append(False)

            # Check South room
            try:
                if layout[i + 5 * (j + 1)] != 'n':
                    doors.append(True)
                else:
                    doors.append(False)
            except IndexError:
                doors.append(False)

            # Check East room
            try:
                if layout[(i + 1)+ 5 * j] != 'n':
                    doors.append(True)
                else:
                    doors.append(False)
            except IndexError:
                doors.append(False)

            # Check West room
            try:
                if layout[(i - 1)+ 5 * j] != 'n':
                    doors.append(True)
                else:
                    doors.append(False)
            except IndexError:
                doors.append(False)


            # Place Room
            if room == 'n':
                self.map.append(Room(pos,
                                     [False, False, False, False],
                                     self.BGSPRITES[self.level],
                                     self.DOORSPRITES[self.level],
                                     False))


            elif room == 'r':
                self.map.append(Room(pos, doors, self.BGSPRITES[self.level],
                                     self.DOORSPRITES[self.level], False))

            elif room == 's':
                self.map.append(Room(pos, doors, self.BGSPRITES[self.level],
                                     self.DOORSPRITES[self.level], True))
                start = count

            elif room == 'b':
                self.map.append(Room(pos, doors, self.BGSPRITES[self.level],
                                     self.DOORSPRITES[self.level], True))

            count += 1

        self.currentRoom = self.map[start]
        self.currentRoom.render(self.sc)

    def generateLayout(self):

        layouts = [['s','n','n','n','n',
                    'r','r','r','r','n',
                    'r','r','n','n','n',
                    'n','r','r','n','n',
                    'n','n','b','n','n'],
                   ['n','n','n','n','n',
                    'n','n','r','r','r',
                    'n','b','s','n','r',
                    'n','r','r','r','n',
                    'n','r'r'r','n','n'],
                   ['n','n','n','n','n',
                    'n','n','b','n','n',
                    'n','r','r','n','n',
                    'n','r','r','r','n',
                    's','r','n','n','n'],
                   ['n','n','n','n','n',
                    'n','r','r','r','b',
                    'n','r','n','r','n',
                    's','r','r','r','n',
                    'n','n','n','n','n'],
                   ['n','n','n','n','n',
                    's','r','r','r','n',
                    'n','n','n','r','n',
                    'n','b','r','r','n',
                    'n','n','n','n','n'],
                   ['n','n','n','n','n',
                    'n','r','r','r','n',
                    'n','r','n','r','n',
                    'b','r','r','r','r',
                    'n','n','n','n','s']]

        return random.choice(layouts)

    def update(self, pc, ec):
        self.checkRoomTransition(pc,ec)
        self.checkLevelTransition(pc)
