import random
from .room import *


class MapController():

    def __init__(self, sc):

        self.currentLevel = 1
        self.map = []

        self.currentRoom = None
        self.sc = sc

    def checkRoomTransition(self, pc):

        for door in self.currentRoom.doors:
            collisions = pygame.sprite.spritecollide(door,
                                                     self.sc.collidableEntities,
                                                     False)

            for i in collisions:
                if (i.id == game.ID.PLAYER):
                    pc.collideDoor(door)
                    self.transition(door.type)


    def transition(self, direction):

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
                self.map.append(Room(pos, [False, False, False, False]))

            elif room == 'r':
                self.map.append(Room(pos, doors))

            elif room == 's':
                self.map.append(Room(pos, doors))
                start = count

            elif room == 'b':
                self.map.append(Room(pos, doors))


            # figure out if the room has doors.



            count += 1

        self.currentRoom = self.map[start]

    def generateLayout(self):


        # s = starting room
        # n = no room
        # k = room with a key reward at the end.


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

    def update(self, pc):
        self.checkRoomTransition(pc)
