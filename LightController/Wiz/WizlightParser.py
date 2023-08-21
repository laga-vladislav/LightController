from pywizlight import wizlight, PilotParser

from LightController.core.BulbCore import BulbType
from LightController.core.library import Features

from .WizLightCore import WizBulbInstance
from .WizBulbTypeDeterminator import WizBulbTypeDeterminator
from .WizBulbFeaturesDeterminator import WizBulbFeaturesDeterminator

class ParserWizlightToWizBulbInstance:
    """
    Parse wizlight from pywizlight to WizBulbInstance.
    """
    def __init__(self, bulb: wizlight):
        self._bulb = bulb
        self._pilot_parser_config: PilotParser

    async def get_WizBulbInstance(self) -> WizBulbInstance:
        """
        Parameters to be parsed:
            name: str
            status: bool
            type: BulbType
            features: Features
            parent_instance: INSTANCE_BULB_TYPES
            supported_scene_ids: WIZ_SCENES.SCENES
        :return WizBulbInstance:
        """
        bulb_name = await self.get_name()
        bulb_status = await self.get_status()
        bulb_type = await self.get_bulb_type()
        bulb_features = await self.parse_wizlight_features()
        scenes = await self.get_supported_scenes()
        # print(bulb_name, bulb_status, bulb_type, bulb_features, self._bulb, scenes) log
        return WizBulbInstance(
            name=bulb_name,
            status=bulb_status,
            type=bulb_type,
            features=bulb_features,
            parent_instance=self._bulb,
            supported_scene_names=scenes
        )

    async def get_name(self) -> str:
        config = await self._bulb.getBulbConfig()
        return config['result']['moduleName']

    async def get_status(self) -> bool:
        await self._update_pilot_parser()
        status = self._pilot_parser_config.get_state()
        return status

    async def get_bulb_type(self) -> BulbType:
        bulb_type = await WizBulbTypeDeterminator(
            self._bulb
        ).define_type()
        return bulb_type

    async def parse_wizlight_features(self) -> Features:
        features = await WizBulbFeaturesDeterminator(self._bulb).get_features()
        return features

    async def get_supported_scenes(self) -> list[str]:
        scenes = await self._bulb.getSupportedScenes()
        return scenes

    async def _update_pilot_parser(self) -> None:
        self._pilot_parser_config = await self._bulb.updateState()


if __name__ == "__main__":
    ParserWizlightToWizBulbInstance(wizlight(ip="192.168.1.203", port=38899, mac="6c2990a2b30d")).get_WizBulbInstance()
