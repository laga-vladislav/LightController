import asyncio
from abc import ABC

import pywizlight.bulb
from pywizlight import wizlight, PilotBuilder
from AbstractBulbController import BulbController
from WizBulbProfile import WizBulbProfile
from WizBulbProfile import Aliases

class WizBulbController(BulbController, ABC):
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
        await self.__update_status()
        return self._status

    async def turn_on(self) -> None:
        pilot_builder = await self.__convert_bulb_profile_to_pilot_builder()
        await self._bulb_instance.turn_on(pilot_builder=pilot_builder)

    async def turn_off(self) -> None:
        await self._bulb_instance.turn_off()

    # Individual methods
    async def __update_status(self) -> None:
        config = await self.__get_updated_config()
        self._status = config.get_state()

    async def __get_updated_config(self) -> pywizlight.bulb.PilotParser:
        config = await self._bulb_instance.updateState()
        print(config.__dict__)  # log
        return config

    async def __convert_bulb_profile_to_pilot_builder(self) -> PilotBuilder:
        await self.__update_status()
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

    def __get_rgb_pilot_builder(self) -> PilotBuilder:
        pass

    def __get_non_rgb_pilot_builder(self) -> PilotBuilder:
        pass

    def _get_brightness(self) -> Aliases.HexCode:
        return self._bulb_profile.get_params()["brightness"] \
            if "brightness" in self._bulb_profile.get_params().keys() \
            else self._config.get_brightness()

    def _get_light_temperature(self) -> Aliases.KelvinTemperature:
        return self._bulb_profile.get_params()["light_temperature"] \
            if "light_temperature" in self._bulb_profile.get_params().keys() \
            else self._config.get_colortemp()

    def _get_rgb_color(self):
        return self._bulb_profile.get_params()["RGBColor"] \
            if "RGBColor" in self._bulb_profile.get_params().keys() \
            else self._config.get_rgb()


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
