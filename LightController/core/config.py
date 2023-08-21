from typing import Union
from pywizlight import wizlight
from LightController.core.library import Aliases

TIME_FORMAT_FOR_LOGGER = '%X'

INSTANCE_BULB_TYPES = Union[wizlight]  # add new types later
MIN_BRIGHTNESS_VALUE: Aliases.HexCode = 0
MAX_BRIGHTNESS_VALUE: Aliases.HexCode = 255

LOCAL_IP = "192.168.1.255"
MAX_ATTEMPTS_TO_FIND_BULBS = 3