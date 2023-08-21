import dataclasses
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

from LightController.core.library import Features, Aliases
from LightController.core.config import INSTANCE_BULB_TYPES

class BulbType(Enum):
    TW = "Tunable White"
    """Have Cool White and Warm White LEDs."""
    DW = "Dimmable White"
    """Have only Dimmable white LEDs."""
    RGB = "RGB Tunable"
    """Have RGB LEDs."""
    SOCKET = "Socket"
    """Smart socket with only on/off."""

class AbstractBulbTypeDeterminator(ABC):
    def __init__(
            self,
            specific_instance: INSTANCE_BULB_TYPES
    ) -> None:
        self._specific_instance = specific_instance

    @abstractmethod
    def define_type(self) -> BulbType:
        pass

@dataclasses.dataclass
class AbstractInstanceOfBulb(ABC):
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
    The specific class is obtained from the finders list."""

@dataclasses.dataclass
class AbstractBulbProfile:
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

class BulbProfileGenerator:
    """
    Define AbstBulbProfile with Features information
    :returns AbstBulbProfile
    """
    def __init__(self, features: Features):
        self._features = features

    def set_parameters(
            self,
            brightness: Optional[Aliases.HexCode],
            colortemp: Optional[Aliases.KelvinTemp],
            color: Optional[Aliases.RGBColor]
    ) -> AbstractBulbProfile:
        """
        :param brightness: HexCode
        :param colortemp: KelvinTemp
        :param color: RGBColor
        :return: BulbProfile
        """
        profile = AbstractBulbProfile(
            brightness=brightness if self._features.brightness else None,
            colortemp=colortemp if self._features.colortemp else None,
            color=color if self._features.color else None
        )
        return profile


if __name__ == '__main__':
    pass
