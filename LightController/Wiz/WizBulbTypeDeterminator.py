from LightController.core.BulbCore import AbstractBulbTypeDeterminator, BulbType

from LightController.exceptions._exceptions import WrongBulbTypeInput


class WizBulbTypeDeterminator(AbstractBulbTypeDeterminator):
    async def define_type(self) -> BulbType:
        bulb_type = await self._specific_instance.get_bulbtype()
        for type_name in BulbType:
            if type_name.name == bulb_type.bulb_type.name:
                return type_name
        raise WrongBulbTypeInput(f"Invalid bulb type. type should be {BulbType} instance, but got {bulb_type}.")
