import pytest

from LightController import WizBulbFinder as Finder

@pytest.mark.asyncio
class Test_WizBulbFinder:
    local_ip = '192.168.1.255'
    finder = Finder.WizBulbFinder(local_ip)

    @staticmethod
    async def test_bulbs_are_list():
        bulbs = await Test_WizBulbFinder.finder.get_bulbs()
        assert type(bulbs) == list
