import dataclasses

from pywizlight.scenes import SCENES

from LightController.core.BulbCore import AbstractInstanceOfBulb


@dataclasses.dataclass
class WizBulbInstance(AbstractInstanceOfBulb):
    supported_scene_names: list[str]
