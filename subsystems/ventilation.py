from core.parts import Component, Rule, Sensor
import datetime
import random

class Ventilator(Component):
    pass


class VentilationRule(Rule):
    # ventilation comes on at 5pm and goes off at 9pm
    ventilation_on = datetime.time(17, 00)
    ventilation_off = datetime.time(21, 00)

    def apply(self, reading, ventilator):
        current_time = datetime.time(datetime.now())
        if reading > 70:
            # ventilation should be on if humidity > 70%
            ventilator.switch_on()
        elif (current_time > ventilation_on and current_time < ventilation_off):
            # even if humidity level is ok, ventilation should be on between 5pm and 9pm
            ventilator.switch_on()
        else:
            ventilator.switch_off()


class MoistureSensor(Sensor):
    def take_reading(self):
        # simulate a humidity reading
        return random.randint(30, 80)
