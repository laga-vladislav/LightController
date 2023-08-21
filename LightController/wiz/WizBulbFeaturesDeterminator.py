import pywizlight.bulblibrary
from pywizlight import wizlight

from LightController.core.library import Features


def convert_wizlight_features_to_light_controller_features(wizlight_features: pywizlight.bulblibrary.Features) -> Features:
    light_controller_features = Features(
        brightness=wizlight_features.brightness,
        colortemp=wizlight_features.color_tmp,
        color=wizlight_features.color
    )
    return light_controller_features


class WizBulbFeaturesDeterminator:
    def __init__(self, bulb_instance: wizlight):
        self._bulb_instance: wizlight = bulb_instance

    async def get_features(self) -> Features:
        bulb_config = await self._bulb_instance.get_bulbtype()
        wizlight_features = bulb_config.features
        features = convert_wizlight_features_to_light_controller_features(wizlight_features)
        return features
