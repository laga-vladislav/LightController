from typing import NamedTuple

import pytest

from LightController.WizBulbProfile import WizBulbProfile, Aliases
from LightController.exceptions._exceptions import *


class LightTemperatureValues(NamedTuple):
    CORRECT_LIGHT_TEMPERATURE_VALUES: list[Aliases.KelvinTemperature]
    NEGATIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE: Aliases.KelvinTemperature
    POSITIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE: Aliases.KelvinTemperature
    STR_LIGHT_TEMPERATURE_VALUE: str
    FLOAT_LIGHT_TEMPERATURE_VALUE: float
    INT_LIGHT_TEMPERATURE_VALUE: int

class Test_LightTemperature:
    profile = WizBulbProfile()
    values = LightTemperatureValues(
        CORRECT_LIGHT_TEMPERATURE_VALUES=[1000, 2333, 5343, 6000, 10000],
        NEGATIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE=999,
        POSITIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE=10001,
        STR_LIGHT_TEMPERATURE_VALUE="5000",
        FLOAT_LIGHT_TEMPERATURE_VALUE=4400.0,
        INT_LIGHT_TEMPERATURE_VALUE=4400
    )

    def test_init_light_temperature(self):
        assert self.profile.get_params() == {}
        assert len(self.profile.get_params()) == 0

    def test_str_light_temperature(self):
        with pytest.raises(LightTemperatureTypeError):
            self.profile.set_new_light_temperature(self.values.STR_LIGHT_TEMPERATURE_VALUE)

    def test_wrong_value_light_temperature(self):
        with pytest.raises(LightTemperatureValueError):
            self.profile.set_new_light_temperature(self.values.NEGATIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE)
        with pytest.raises(LightTemperatureValueError):
            self.profile.set_new_light_temperature(self.values.POSITIVE_OUT_OF_RANGE_LIGHT_TEMPERATURE_VALUE)

    def test_correct_values_light_temperature(self):
        for value in self.values.CORRECT_LIGHT_TEMPERATURE_VALUES:
            self.profile.set_new_light_temperature(value)
            assert type(self.profile.get_params()['light_temperature']) is Aliases.HexCode
        self.profile.set_new_light_temperature(self.values.FLOAT_LIGHT_TEMPERATURE_VALUE)
        assert type(self.profile.get_params()['light_temperature']) is Aliases.HexCode
        self.profile.set_new_light_temperature(self.values.INT_LIGHT_TEMPERATURE_VALUE)
        assert type(self.profile.get_params()['light_temperature']) is Aliases.HexCode
