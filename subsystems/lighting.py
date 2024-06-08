from core.parts import Component, Rule, Sensor

class Light(Component):
    def dim_off():
        # @TODO: implement dimming off instead of switching off
        print("Dimming off light in room ", self.room_id)
        pass


class LightingRule(Rule):
    # countdown limit in seconds
    time_limit = 300

    def __init__(self):
        # when the light is switched on, reset the countdown
        self._resetCountdown()

    def apply(self, reading, light):
        if reading == True:
            # True means room is occupied
            light.switch_on()
            self._resetCountdown()
        else:
            # Room is not occupied
            if self.countdown == 0:
                light.switch_off()
            else:
                # decrement the countdown
                self._tick()

    def _resetCountdown(self):
        self.countdown = self.time_limit

    def _tick(self):
        if self.countdown > 0:
            self.countdown -= 1


class LightSensor(Sensor):
    def take_reading(self):
        # simulate a reading
        return random.choice([True, False])
