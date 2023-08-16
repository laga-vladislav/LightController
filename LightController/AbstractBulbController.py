from abc import ABC, abstractmethod
from pywizlight import wizlight
from WizBulbProfile import WizBulbProfile

class BulbController(ABC):
    """
    Abstract class for controllers.
    Add new type to "bulb_instance" later
    """
    def __init__(
            self,
            bulb_instance: wizlight,
            bulb_profile: WizBulbProfile = WizBulbProfile()
    ) -> None:
        self._bulb_instance = bulb_instance
        self._bulb_profile = bulb_profile

    def set_new_profile(self, new_profile: WizBulbProfile):
        self._bulb_profile = new_profile

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def switch(self):
        pass
