from dataclasses import dataclass
import logging

LOGGER = logging.getLogger(__name__)


@dataclass
class Bed:
    bed_target_temperature: int
    bed_current_temperature: int

    @staticmethod
    def from_dict(data):
        return Bed(
            bed_target_temperature=data["print"].get("bed_target_temper"),
            bed_current_temperature=data["print"].get("bed_temper")
        )

    def update_from_dict(self, data):
        self.bed_target_temperature = data["print"].get("bed_target_temper", self.bed_target_temperature)
        self.bed_current_temperature = data["print"].get("bed_temper", self.bed_current_temperature)


class Device:
    def __init__(self, data):
        self.bed = Bed.from_dict(data)

    def update_from_dict(self, data):
        if "print" in data:
            self.bed.update_from_dict(data)
        return self
