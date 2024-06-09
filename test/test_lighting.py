import unittest

import subsystems.lighting as light

class TestLightingRule(unittest.TestCase):
    def setUp(self):
        self.light_rule = light.LightingRule()
        self.light = light.Light(1)

    def test_lights_come_on(self):
        # person enters room
        self.light_rule.apply(True, self.light)

        # light should be on
        self.assertFalse(self.light.off)

    def test_lights_stay_on(self):
        # person enters room
        self.light_rule.apply(True, self.light)

        # person leaves room
        self.light_rule.apply(False, self.light)
        
        # light is still on
        self.assertFalse(self.light.off)

    def test_lights_countdown_to_off(self):
        # person enters room
        self.light_rule.apply(True, self.light)

        # person leaves room
        self.light_rule.apply(False, self.light)

        # simulate 5 min countdown (300 seconds)
        for _ in range(1, 300):
            self.light_rule.apply(False, self.light)

        # Light should still be on
        self.assertFalse(self.light.off)

        # One more tick
        self.light_rule.apply(False, self.light)

        # Light should be off
        self.assertTrue(self.light.off)


if __name__ == '__main__':
    unittest.main()