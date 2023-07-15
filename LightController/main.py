import asyncio

from pywizlight import wizlight
from WizBulbFinder import WizBulbFinder
from WizBulbController import WizBulbController

async def main():
    bulb_finder = WizBulbFinder()
    bulbs = await bulb_finder.get_bulbs()
    print(bulbs)
    # bulb = wizlight(ip="192.168.1.108", port=38899, mac="6c2990a286f5")
    # await bulb.turn_on()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
