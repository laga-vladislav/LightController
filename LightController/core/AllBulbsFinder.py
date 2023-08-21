import asyncio
import dataclasses

from LightController.core.config import LOCAL_IP, MAX_ATTEMPTS_TO_FIND_BULBS
from LightController.core.BulbCore import AbstractInstanceOfBulb

# finders
from LightController.wiz.WizBulbFinder import WizBulbFinder

@dataclasses.dataclass
class Finders:
    Wiz: WizBulbFinder

class AllBulbsFinder:
    """
    Finds bulbs in local network
    :returns list with all kinds of bulb instances
    """
    def __init__(
            self,
            local_ip: str = LOCAL_IP
    ):
        self._local_ip: str = local_ip
        self._bulbs: list[AbstractInstanceOfBulb] = []
        self._finders: Finders = Finders(
            Wiz=WizBulbFinder(
                local_ip=local_ip,
                max_attempts=MAX_ATTEMPTS_TO_FIND_BULBS
            )
        )

    async def get_bulbs_all_types(self) -> list[AbstractInstanceOfBulb]:
        for finder in dataclasses.asdict(self._finders).items():
            bulbs = await finder[1].get_bulbs()
            self._bulbs += bulbs
        return self._bulbs

async def main():
    bulbs = await AllBulbsFinder().get_bulbs_all_types()
    print(bulbs)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

