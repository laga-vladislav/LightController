from enum import Enum
from pywizlight import wizlight, PilotBuilder

class Status(Enum):
    Off = 0
    On = 1


class WizBulbController:
    def __init__(self, wizlight_bulb: wizlight) -> None:
        self.bulb = wizlight_bulb
        self.pilot_builder = PilotBuilder
        self.status = Status[self.bulb.state]

    def __dict__(self):
        return {
            'ip': self.bulb.ip,
            'mac': self.bulb.mac
        }

    async def turn_on(
            self,
            pilot_builder: PilotBuilder = PilotBuilder(colortemp=4400, brightness=255)
    ):
        await self.bulb.turn_on(pilot_builder=pilot_builder)
        self.status = Status.On

    async def turn_off(self):
        await self.bulb.turn_off()
        self.status = Status.Off

    async def get_status(self):
        print(self.bulb.status)
