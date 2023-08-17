import asyncio
import time

from pywizlight import discovery, wizlight
from LightController.exceptions._exceptions import RetriesError

from LightController.Core.BulbFinder import BulbFinder
from LightController.Core.config import INSTANCE_BULB_TYPES, MAX_ATTEMPTS_TO_FIND_BULBS


class WizBulbFinder(BulbFinder):
    """
    Uses it for finding wiz lights in local network.
    """
    async def get_bulbs(self) -> list[INSTANCE_BULB_TYPES]:
        try:
            await self.__find_wizlight_bulbs_by_attempts()
        except RetriesError as e:
            print(e)  # log
            return self._bulbs
        return self._bulbs

    async def __find_wizlight_bulbs_by_attempts(self) -> None:
        attempt_counter = 0
        while attempt_counter < MAX_ATTEMPTS_TO_FIND_BULBS:
            try:
                print("start time:", time.strftime('%X'), self._bulbs, attempt_counter)  # log
                self._bulbs = await self.__discover_bulbs()
                break
            except TimeoutError as e:
                print(e)  # log
                attempt_counter += 1
            except asyncio.exceptions.TimeoutError as e:
                print(e)  # log
                attempt_counter += 1
            finally:
                print("end time:", time.strftime('%X'))  # log
        else:
            raise RetriesError('Count of finding retries exceeded')

    async def __discover_bulbs(self) -> list[wizlight]:
        bulbs = await asyncio.wait_for(discovery.discover_lights(
            broadcast_space=self._local_ip,
            wait_time=1), timeout=1.1
        )
        if not bulbs:
            raise TimeoutError('Finding bulbs time exceeded')
        return bulbs

async def main():
    finder = WizBulbFinder()
    bulbs = await finder.get_bulbs()
    print(bulbs)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
