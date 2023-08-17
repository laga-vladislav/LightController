import dataclasses
from LightController.Core.bulb_core import InstanceOfBulb
import pywizlight.scenes as wiz_scenes

WIZ_SCENES = wiz_scenes


@dataclasses.dataclass
class WizBulb(InstanceOfBulb):
    supported_scene_ids: WIZ_SCENES.SCENES

class WizBulbController(BulbController, ABC):
    def __init__(
            self,
            bulb_instance: wizlight,
            bulb_profile: WizBulbProfile = WizBulbProfile()
    ) -> None:
        super().__init__(bulb_instance, bulb_profile)
        self._pilot_parser_config: PilotParser

    def __dict__(self):
        return {
            'ip': self._bulb_instance.ip,
            'mac': self._bulb_instance.mac
        }

    # Abstract methods
    async def get_status(self) -> bool:
        """
        True is ON
        False is OFF
        """
        await self._update_status()
        return self._status

    async def turn_on(self) -> None:
        pilot_builder = await self._convert_bulb_profile_to_pilot_builder()
        await self._bulb_instance.turn_on(pilot_builder=pilot_builder)

    async def turn_off(self) -> None:
        await self._bulb_instance.turn_off()

    # Individual methods
    async def _update_status(self) -> None:
        await self._update_pilot_parser_config()
        self._status = self._pilot_parser_config.get_state()

    async def _update_pilot_parser_config(self) -> pywizlight.bulb.PilotParser:
        self._pilot_parser_config = await self._bulb_instance.updateState()
        print(self._pilot_parser_config.__dict__)  # log

    async def _convert_bulb_profile_to_pilot_builder(self) -> PilotBuilder:
        await self._update_pilot_parser_config()
        brightness = self._get_brightness()
        print(brightness)
        light_temperature = self._get_light_temperature()
        print(light_temperature)
        rgb_color = self._get_rgb_color()
        print(rgb_color)
        return PilotBuilder(
            brightness=brightness,
            colortemp=light_temperature,
        )

    def _get_rgb_pilot_builder(self) -> PilotBuilder:
        pass

    def _get_non_rgb_pilot_builder(self) -> PilotBuilder:
        pass

    def _get_brightness(self) -> Aliases.HexCode:
        return self._bulb_profile.get_params()["brightness"] \
            if "brightness" in self._bulb_profile.get_params().keys() \
            else self._pilot_parser_config.get_brightness()

    def _get_light_temperature(self) -> Aliases.KelvinTemperature:
        return self._bulb_profile.get_params()["light_temperature"] \
            if "light_temperature" in self._bulb_profile.get_params().keys() \
            else self._pilot_parser_config.get_colortemp()

    def _get_rgb_color(self):
        return self._bulb_profile.get_params()["RGBColor"] \
            if "RGBColor" in self._bulb_profile.get_params().keys() \
            else self._pilot_parser_config.get_rgb()


async def main():
    bulb = wizlight(ip="192.168.1.135", port=38899, mac="6c2990a286f5")
    bulb2 = wizlight(ip="192.168.1.155", port=38899, mac="6c2990a2a00e")
    profile = WizBulbProfile(
        brightness=255,
        light_temperature=4400
    )
    controller = WizBulbController(bulb2, profile)
    await controller.turn_on()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
