import pywizlight.bulb
from pywizlight import wizlight, PilotBuilder

class WizBulbController:
    def __init__(
            self,
            wizlight_bulb: wizlight,
            pilot_builder: PilotBuilder = PilotBuilder()
    ) -> None:
        self._bulb: wizlight = wizlight_bulb
        self._pilot_builder: PilotBuilder = pilot_builder
        self._config: pywizlight.bulb.PilotParser
        self._status: bool

    def __dict__(self):
        return {
            'ip': self._bulb.ip,
            'mac': self._bulb.mac
        }

    async def __update_config(self):
        self._config = await self._bulb.updateState()

    async def get_status(self):
        await self.__update_status()
        return self._status

    async def __update_status(self):
        await self.__update_config()
        self._status = self._config.get_state()

    async def turn_on(self):
        await self._bulb.turn_on(pilot_builder=self._pilot_builder)

    async def turn_off(self):
        await self._bulb.turn_off()
