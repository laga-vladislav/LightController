import dataclasses
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

from library import Features, Aliases
from config import INSTANCE_BULB_TYPES

class BulbType(Enum):
    TW = "Tunable White"
    """Have Cool White and Warm White LEDs."""
    DW = "Dimmable White"
    """Have only Dimmable white LEDs."""
    RGB = "RGB Tunable"
    """Have RGB LEDs."""
    SOCKET = "Socket"
    """Smart socket with only on/off."""

class BulbTypeDeterminator(ABC):
    def __int__(
            self,
            specific_instance: INSTANCE_BULB_TYPES
    ) -> None:
        self._specific_instance = specific_instance

    @abstractmethod
    def define_type(self) -> BulbType:
        pass

@dataclasses.dataclass
class InstanceOfBulb(ABC):
    """
    Abstract class for instances.
    """
    name: str
    # Name of the bulb model from the specs
    status: bool
    # True means ON, False means OFF
    type: BulbType
    features: Features
    parent_instance: INSTANCE_BULB_TYPES
    """'parent_instance' Contains the class from another package which controls the bulb.
    The specific class is obtained from the BulbFinder module."""

@dataclasses.dataclass
class BulbProfile:
    """
    Contains the information about bulb parameters
    _params keys:
        "brightness": HexCode | None,
        "colortemp": KelvinTemp | None
        "color": RGBColor | None
    """
    brightness: Aliases.HexCode | None
    colortemp: Aliases.KelvinTemp | None
    color: Aliases.RGBColor | None

class BulbProfileDeterminator:
    """
    Define BulbProfile with the BulbType information
    """
    @staticmethod
    def define_profile(bulb_type: BulbType) -> BulbProfile:
        pass


if __name__ == '__main__':
    pass
