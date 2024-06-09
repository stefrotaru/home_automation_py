class Regulator:
    def __init__(self, rule):
        # becomes a specific type depending on the rule (e.g. Ventilator, Radiator, Light)
        self.rule = rule
        self.sensors = dict()
        self.components = dict()

    def add_room(self, room_id, sensor, component):
        self.sensors[room_id] = sensor
        self.components[room_id] = component

    def process_reading(self):
        # go through each sensor belonging to this regulator
        for room_id, sensor in self.sensors.items():
            # for each one, take a reading and pass it to this regulator's rule
            try:
                reading = sensor.take_reading()
            except SensorError:
                # sensor failed to take a reading
                log.error("Sensor in room %s failed to take a reading", room_id, exc_info=True)
                self.rule.apply(reading, self.components[room_id])
