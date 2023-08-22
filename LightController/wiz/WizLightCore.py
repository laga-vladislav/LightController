import dataclasses

from LightController.core.BulbCore import AbstractInstanceOfBulb


@dataclasses.dataclass
class WizBulbInstance(AbstractInstanceOfBulb):
    supported_scene_names: list[str]
