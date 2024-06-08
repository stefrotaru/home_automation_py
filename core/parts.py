# This module contains the basic parts of an automation subsystem.
# The intention is that the developer uses these as the starting
# point for writing a new subsystem.

class Rule:
    def apply(self, reading, component):
        pass


class Component:
    def __init__(self, room_id):
        self.room_id = room_id
        self.off = True

    def switch_on(self):
        if self.off:
            self.off = False
            print("Switching on component in room ", self.room_id)

    def switch_off(self):
        if not self.off:
            self.off = True
            print("Switching off component in room ", self.room_id)


class Sensor:
    def __init__(self, room_id):
        self.room_id = room_id

    def take_reading(self):
        print("Reading from sensor in room ", self.room_id)
        pass