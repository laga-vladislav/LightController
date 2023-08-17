from abc import ABC, abstractmethod
from .config import LOCAL_IP, INSTANCE_BULB_TYPES


class BulbFinder(ABC):
    """
    Finds bulbs in local network
    :returns list with all kinds of bulb instances
    """
    def __init__(
            self,
            local_ip: str = LOCAL_IP
    ):
        self._local_ip = local_ip
        self._bulbs = list[INSTANCE_BULB_TYPES]

    @abstractmethod
    def get_bulbs(self) -> list[INSTANCE_BULB_TYPES]:
        pass
