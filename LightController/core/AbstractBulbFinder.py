from abc import ABC, abstractmethod

from LightController.core.BulbCore import AbstractInstanceOfBulb

class AbstractBulbFinder(ABC):
    def __init__(
            self,
            max_attempts: int,
            local_ip: str
    ):
        self._local_ip = local_ip
        self._bulbs: list[AbstractInstanceOfBulb] = []
        self._max_attempts = max_attempts

    @abstractmethod
    def get_bulbs(self) -> list[AbstractInstanceOfBulb]:
        pass
