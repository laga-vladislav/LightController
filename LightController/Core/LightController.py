from abc import ABC, abstractmethod
from bulb import BulbProfile, InstanceOfBulb

class LightController(ABC):
    def __init__(
            self,
            bulb_instance: InstanceOfBulb,
            bulb_profile: BulbProfile
    ):
        self._bulb_instance = bulb_instance
        self._bulb_profile = bulb_profile

    def set_new_profile(self, new_profile: BulbProfile):
        self._bulb_profile = new_profile

    def get_status(self) -> bool:
        """True -> ON, False -> OFF"""
        return self._bulb_instance.status

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    def switch(self) -> None:
        """
        Turn ON if status is False (OFF), turn OFF in status if True (ON)
        :return: None
        """
        if self._bulb_instance.status:
            self.turn_off()
        else:
            self.turn_on()
