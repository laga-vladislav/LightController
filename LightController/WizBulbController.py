import asyncio

import pywizlight.bulb
from pywizlight import wizlight, PilotBuilder, PilotParser
from WizBulbProfile import WizBulbProfile
from WizBulbProfile import Aliases

class WizBulbController:
    def __init__(
            self,
            wizlight_bulb: wizlight,
            bulb_profile: WizBulbProfile = WizBulbProfile()
    ) -> None:
        self._bulb: wizlight = wizlight_bulb
        self._bulb_profile: WizBulbProfile = bulb_profile
        self._config: pywizlight.bulb.PilotParser
        self._status: bool

    def __dict__(self):
        return {
            'ip': self._bulb.ip,
            'mac': self._bulb.mac
        }

    async def __update_config(self):
        self._config = await self._bulb.updateState()
        print(self._config.__dict__)

    async def get_status(self):
        await self.__update_status()
        return self._status

    async def __update_status(self):
        await self.__update_config()
        self._status = self._config.get_state()

    async def turn_on(self):
        pilot_builder = await self.__convert_bulb_profile_to_pilot_builder()
        await self._bulb.turn_on(pilot_builder=pilot_builder)

    async def __convert_bulb_profile_to_pilot_builder(self) -> PilotBuilder:
        await self.__update_config()
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
        return self._bulb_profile.get_params()["brightness"]\
            if "brightness" in self._bulb_profile.get_params().keys()\
            else self._config.get_brightness()

    def _get_light_temperature(self) -> Aliases.KelvinTemperature:
        return self._bulb_profile.get_params()["light_temperature"]\
            if "light_temperature" in self._bulb_profile.get_params().keys()\
            else self._config.get_colortemp()

    def _get_rgb_color(self):
        return self._bulb_profile.get_params()["RGBColor"]\
            if "RGBColor" in self._bulb_profile.get_params().keys()\
            else self._config.get_rgb()

    async def turn_off(self):
        await self._bulb.turn_off()

async def main():
    bulb = wizlight(ip="192.168.1.135", port=38899, mac="6c2990a286f5")
    bulb2 = wizlight(ip="192.168.1.155", port=38899, mac="6c2990a2a00e")
    profile = WizBulbProfile(
        brightness=255,
        light_temperature=1400,
        rgb_color=(100, 100, 100)
    )
    controller = WizBulbController(bulb2, profile)
    await controller.turn_on()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
