import unittest

import core.regulator as regulator
import subsystems.heating as heat


def temp_low(self):
    return 17

def temp_ok(self):
    return 21

def temp_high(self):
    return 25


class TestHeatingSubsystem(unittest.TestCase):
    def setUp(self):
        # fully simulate a regulator
        room_id = 1
        self.temperature_sensor = heat.TemperatureSensor(room_id)
        self.radiator = heat.Radiator(room_id)
        self.heat_regulator = regulator.Regulator(heat.TemperatureRule())
        self.heat_regulator.add_room(room_id, self.temperature_sensor, self.radiator)

    def test_heating_off(self):
        # should simulate sensor outputs at different temperatures
        # the following line replaces the take_reading method that a Radiator has and replaces it with the temp_ok function
        heat.TemperatureSensor.take_reading = temp_ok

        # therefore, the temperature sensor returns 21
        self.heat_regulator.process_reading()

        # radiator is off
        self.assertTrue(self.radiator.off)

    def test_heating_comes_on_and_stays_on(self):
        # the temperature sensor returns 17 now
        heat.TemperatureSensor.take_reading = temp_low
        self.heat_regulator.process_reading()

        # radiator is on
        self.assertFalse(self.radiator.off)

        # the temperature sensor will return 21 now
        heat.TemperatureSensor.take_reading = temp_ok
        self.heat_regulator.process_reading()

        # radiator is still on
        self.assertFalse(self.radiator.off)
    
    def test_heating_on_then_off(self):
        heat.TemperatureSensor.take_reading = temp_low
        self.heat_regulator.process_reading()

        # radiator is on
        self.assertFalse(self.radiator.off)

        # now the temperature is too high
        heat.TemperatureSensor.take_reading = temp_high
        self.heat_regulator.process_reading()

        # radiator is now off
        self.assertTrue(self.radiator.off)


if __name__ == '__main__':
    unittest.main()