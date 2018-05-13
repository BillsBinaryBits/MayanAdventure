import abc


class Adventurer:
    def __init__(self, name: str):
        self._name = name.strip()

    @property
    def name(self):
        return self._name


class Room(metaclass=abc.ABCMeta):
    def __init__(self, adventurer):
        self._doors = None
        self._adventurer = adventurer

    @property
    def adventurer(self):
        return self._adventurer

    @property
    def description(self):
        raise NotImplementedError

    @property
    def doors(self):
        return self._doors

    def move(self, direction):
        if direction not in self.doors.keys():
            print("\nI don't know what that direction is")
            return None

        room = self.doors[direction]

        if room is None:
            print("\nDon't go that way there is a Crocodile")
            return None

        return room


def get_rooms(north, south, east, west):
    return {
        'N': north,
        'S': south,
        'E': east,
        'W': west
    }


def get_door_directions(doors):
    message = "\nYou can go "
    for key, value in doors.items():
        if value is not None:
            message = message + key.upper()
            message = message + ","
    return message


def get_direction_description(message, doors):
    message = message + "\n"
    message = message + get_door_directions(doors)
    return message


class Bedroom(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(None, WestCorridor, None, DiningHall)

    def description(self):
        message = "Your are standing in a bedroom with blood-stained sheets lying across the floor. " \
                  "To your East is a scary looking door with 'Keep Out!' written on it"
        return get_direction_description(message, self._doors)


class PrayerRoom(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(None, None, DiningHall, None)

    def description(self):
        message = "You are standing in a small prayer room, in the corner you notice a key with gold engravings"
        return get_direction_description(message, self._doors)


class DiningHall(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(None, None, WestCorridor, PrayerRoom)

    def description(self):
        message = "Your standing in a dining hall surrounded by dead bodies"
        return get_direction_description(message, self._doors)


class WestCorridor(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(None, None, EntranceHall, DiningHall)

    def description(self):
        message = "Your are in a long gloomy corridor"
        return get_direction_description(message, self._doors)


class Outside(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(EntranceHall, None, None, None)

    def description(self):
        message = "Welcome {0}! you are standing in front of a mayan temple".format(self.adventurer.name)
        return get_direction_description(message, self._doors)


class EntranceHall(Room):
    def __init__(self, adventurer):
        super().__init__(adventurer)
        self._doors = get_rooms(None, Outside, None, WestCorridor)

    def description(self):
        message = "You are standing in a vast hall"
        return get_direction_description(message, self._doors)


name = input("Hello Adventurer! Tell me your name?:")

adventurer = Adventurer(name)
current_room = Outside(adventurer)

end = False
while end is not True:
    print(current_room.description())
    direction = input("Which way do you want to go {0}?".format(adventurer.name)).upper()
    if direction != "END":
        new_room = current_room.move(direction)
        if new_room is not None:
            current_room = new_room(adventurer)
    else:
        end = True

    print("\n")
