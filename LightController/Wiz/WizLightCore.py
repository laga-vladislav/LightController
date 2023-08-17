import dataclasses
from LightController.Core.bulb import InstanceOfBulb
import pywizlight.scenes as wiz_scenes

WIZ_SCENES = wiz_scenes


@dataclasses.dataclass
class WizBulb(InstanceOfBulb):
    supported_scene_ids: WIZ_SCENES.SCENES
