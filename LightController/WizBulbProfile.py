from typing import NamedTuple
from typing import Optional
from typing import Dict
from typing import Any
from LightController.exceptions._exceptions import *

class Aliases(NamedTuple):
    HexCode = int  # Hex 25-255 values
    KelvinTemperature = int  # from 1000 to 10000
    RGBColor = tuple[int, int, int]  # every int from 0 to 255

MIN_BRIGHTNESS_VALUE: Aliases.HexCode = 25
MAX_BRIGHTNESS_VALUE: Aliases.HexCode = 255

class WizBulbProfile:
    """
    Contains the information about bulb parameters
    _params keys:
        "brightness": HexCode,
        "light_temperature": KelvinTemperature
        "rgb_color": RGBColor
    """
    def __init__(
            self,
            brightness: Optional[Aliases.HexCode] = None,
            light_temperature: Optional[Aliases.KelvinTemperature] = None,
            rgb_color: Optional[Aliases.RGBColor] = None
    ) -> None:
        # dictionary with all parameters
        self._params: Dict[str, Any] = {}
        # setters
        if brightness is not None:
            self._set_brightness(brightness)
        if light_temperature is not None:
            self._set_light_temperature(light_temperature)
        if rgb_color is not None:
            self._set_rgb_color(rgb_color)

    def _set_brightness(self, brightness: Aliases.HexCode) -> None:
        try:
            if not (MIN_BRIGHTNESS_VALUE <= brightness <= MAX_BRIGHTNESS_VALUE):
                raise BrightnessValueError(f"Value must be between {MIN_BRIGHTNESS_VALUE} and {MAX_BRIGHTNESS_VALUE}")
        except TypeError:
            raise BrightnessTypeError(f"Value must be '{Aliases.HexCode.__name__}'")
        self._params["brightness"] = Aliases.HexCode(brightness)

    def _set_light_temperature(self, light_temperature: Aliases.KelvinTemperature) -> None:
        try:
            if not (1000 <= light_temperature <= 10000):
                raise LightTemperatureValueError("Value must be between 1000 and 10000")
        except TypeError:
            raise LightTemperatureTypeError(f"Value must be '{Aliases.KelvinTemperature.__name__}'")
        self._params["light_temperature"] = Aliases.KelvinTemperature(light_temperature)

    def _set_rgb_color(self, rgb_color: Aliases.RGBColor) -> None:
        try:
            if not all(0 <= color <= 255 for color in rgb_color):
                raise RGBValueError("Every value must be between 0 and 255")
        except TypeError:
            raise RGBTypeError(f"Value must be '{Aliases.RGBColor.__name__}'")
        self._params["rgb_color"] = Aliases.RGBColor(rgb_color)

    def set_new_brightness(self, new_brightness: Aliases.HexCode) -> None:
        self._set_brightness(new_brightness)

    def set_new_light_temperature(self, new_light_temperature: Aliases.KelvinTemperature) -> None:
        self._set_light_temperature(new_light_temperature)

    def set_new_rgb_color(self, new_rgb_color: Aliases.RGBColor) -> None:
        self._set_rgb_color(new_rgb_color)

    def get_params(self) -> Dict[str, Any]:
        return self._params


if __name__ == "__main__":
    profile = WizBulbProfile(
        brightness=144,
        light_temperature=4500
    )
    try:
        f = WizBulbProfile(
            brightness="10"
        )
        print(f.get_params())
    except BrightnessTypeError as e:
        print(e)
