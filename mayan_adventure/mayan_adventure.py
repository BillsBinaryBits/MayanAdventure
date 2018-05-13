import abc


class Adventurer:
    def __init__(self, name: str):
        self._name = name.strip()

    @property
    def name(self):
        return self._name


class Room(metaclass=abc.ABCMeta):
    def __init__(self,adventurer):
        self._adventurer=adventurer

    @property
    def adventurer(self):
        return self._adventurer

    @property
    def description(self):
        raise NotImplementedError

    @property
    def doors(self):
        return self._doors

    def move(self,direction):
        if direction not in self.doors.keys():
            print("I don't know what that direction is")
            return None

        room=self.doors[direction]

        if room is None:
            print("Don't go that way there is a Crocodile")
            return None

        return room

def get_rooms(north, south, east, west):
    return {
            'n' : north,
            's' : south,
            'e' : east,
            'w' : west
        }

def get_door_directions(doors):
    message = "You can go "
    for key, value in doors.items():
        if value is not None:
            message = message + key
            message = message + ","
    return message


class Outside(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors=get_rooms(EntranceHall,None,None,None)

    def description(self):
        message = "Welcome {0}! you are standing in front of a mayan temple".format(self.adventurer.name)
        message = message + "\n"
        message = message + get_door_directions(self._doors)
        return message

class EntranceHall(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors=get_rooms(None,Outside,None,None)

    def description(self):
        message="You are standing in a vast hall"
        message = message + "\n"
        message = message + get_door_directions(self._doors)
        return message



name = input("Hello Adventurer! Tell me your name?:")

adventurer = Adventurer(name)
current_room=Outside(adventurer)

end = False
while end is not True:
    print(current_room.description())
    direction=input("Which way do you want to go {0}?".format(adventurer.name))
    if direction != "end":
        new_room = current_room.move(direction)
        if new_room is not None:
            current_room = new_room(adventurer)
    else:
        end = True

    print("\n")

