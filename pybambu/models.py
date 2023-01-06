from dataclasses import dataclass
import logging

LOGGER = logging.getLogger(__name__)


@dataclass
class Sensors:
    bed_target_temperature: int
    bed_current_temperature: int
    chamber_temperature: int
    nozzle_target_temperature: int
    nozzle_temperature: int
    aux_fan_speed: str
    big_fan2_speed: str
    cooling_fan_speed: str

    @staticmethod
    def from_dict(data):
        return Sensors(
            bed_target_temperature=data["print"].get("bed_target_temper"),
            bed_current_temperature=data["print"].get("bed_temper"),
            chamber_temperature=data["print"].get("chamber_temper"),
            nozzle_target_temperature=data["print"].get("nozzle_target_temper"),
            nozzle_temperature=data["print"].get("nozzle_temper"),
            aux_fan_speed=data["print"].get("big_fan1_speed"),
            big_fan2_speed=data["print"].get("big_fan2_speed"),
            cooling_fan_speed=data["print"].get("cooling_fan_speed"),
        )

    def update_from_dict(self, data):
        self.bed_target_temperature = data["print"].get("bed_target_temper", self.bed_target_temperature)
        self.bed_current_temperature = data["print"].get("bed_temper", self.bed_current_temperature)
        self.chamber_temperature = data["print"].get("chamber_temper", self.chamber_temperature)
        self.nozzle_target_temperature = data["print"].get("nozzle_target_temper", self.nozzle_target_temperature)
        self.nozzle_temperature = data["print"].get("nozzle_temper", self.nozzle_temperature)
        self.aux_fan_speed = data["print"].get("big_fan1_speed", self.aux_fan_speed)
        self.big_fan2_speed = data["print"].get("big_fan2_speed", self.big_fan2_speed)
        self.cooling_fan_speed = data["print"].get("cooling_fan_speed", self.cooling_fan_speed)


class Device:
    def __init__(self, data):
        self.sensors = Sensors.from_dict(data)

    def update_from_dict(self, data):
        if "print" in data:
            self.sensors.update_from_dict(data)
        return self
