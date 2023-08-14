from typing import NamedTuple

import pytest

from LightController.WizBulbProfile import WizBulbProfile, Aliases
from LightController.exceptions._exceptions import *


class BrightnessValues(NamedTuple):
    CORRECT_BRIGHTNESS_VALUES: list[Aliases.HexCode]
    NEGATIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE: Aliases.HexCode
    POSITIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE: Aliases.HexCode
    STR_BRIGHTNESS_VALUE: str
    FLOAT_BRIGHTNESS_VALUE: float
    INT_BRIGHTNESS_VALUE: int

class Test_Brightness:
    profile = WizBulbProfile()
    values = BrightnessValues(
        CORRECT_BRIGHTNESS_VALUES=[0, 144, 11, 1, 255],
        NEGATIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE=-1,
        POSITIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE=256,
        STR_BRIGHTNESS_VALUE="144",
        FLOAT_BRIGHTNESS_VALUE=144.0,
        INT_BRIGHTNESS_VALUE=144
    )

    def test_init_brightness(self):
        assert self.profile.get_params() == {}
        assert len(self.profile.get_params()) == 0

    def test_str_brightness(self):
        with pytest.raises(BrightnessTypeError):
            self.profile.set_new_brightness(self.values.STR_BRIGHTNESS_VALUE)

    def test_wrong_value_brightness(self):
        with pytest.raises(BrightnessValueError):
            self.profile.set_new_brightness(self.values.NEGATIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE)
        with pytest.raises(BrightnessValueError):
            self.profile.set_new_brightness(self.values.POSITIVE_OUT_OF_RANGE_BRIGHTNESS_VALUE)

    def test_correct_values_brightness(self):
        for value in self.values.CORRECT_BRIGHTNESS_VALUES:
            self.profile.set_new_brightness(value)
            assert type(self.profile.get_params()['brightness']) is Aliases.HexCode
        self.profile.set_new_brightness(self.values.FLOAT_BRIGHTNESS_VALUE)
        assert type(self.profile.get_params()['brightness']) is Aliases.HexCode
        self.profile.set_new_brightness(self.values.INT_BRIGHTNESS_VALUE)
        assert type(self.profile.get_params()['brightness']) is Aliases.HexCode
