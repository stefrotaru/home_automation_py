from core.parts import Component, Rule, Sensor
import random

class Radiator(Component):
    pass


class TemperatureRule(Rule):
    def apply(self, reading, radiator):
        if reading < 18:
            radiator.switch_on()
        elif reading > 22:
            radiator.switch_off()


class TemperatureSensor(Sensor):
    def take_reading(self):
        # simulate a temperature reading
        return random.randint(16, 25)