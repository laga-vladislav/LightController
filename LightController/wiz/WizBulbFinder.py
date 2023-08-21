import asyncio
import time

from pywizlight import discovery, wizlight
from LightController.exceptions._exceptions import RetriesError

from .WizLightCore import WizBulbInstance
from .WizlightParser import ParserWizlightToWizBulbInstance

from LightController.core.AbstractBulbFinder import AbstractBulbFinder

class WizBulbFinder(AbstractBulbFinder):
    """
    Uses for finding wiz lights in local network.
    """
    async def get_bulbs(self) -> list[WizBulbInstance]:
        try:
            await self._find_wizlight_bulbs_by_attempts()
        except RetriesError as e:
            print(e)  # log
            return self._bulbs
        return self._bulbs

    async def _find_wizlight_bulbs_by_attempts(self) -> None:
        attempt_counter = 0
        while attempt_counter < self._max_attempts:
            try:
                # print("start time:", time.strftime('%X'), self._bulbs, attempt_counter)  # log
                wiz_bulbs = await self._discover_bulbs()
                self._bulbs = await convert_wizlight_bulbs_to_wiz_bulb_instances(wiz_bulbs)
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

    async def _discover_bulbs(self) -> list[wizlight]:
        bulbs = await asyncio.wait_for(discovery.discover_lights(
            broadcast_space=self._local_ip,
            wait_time=1), timeout=1.1
        )
        if not bulbs:
            raise TimeoutError('Finding bulbs time exceeded')
        return bulbs

async def convert_wizlight_bulbs_to_wiz_bulb_instances(bulbs: list[wizlight]) -> list[WizBulbInstance]:
    wiz_instances = []
    for bulb in bulbs:
        bulb_instance = await ParserWizlightToWizBulbInstance(bulb).get_WizBulbInstance()
        wiz_instances.append(
            bulb_instance
        )
    return wiz_instances
