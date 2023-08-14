class RetriesError(Exception):
    """Too many tries"""
    pass

class BrightnessValueError(Exception):
    """Wrong brightness value"""
    pass

class BrightnessTypeError(Exception):
    """Wrong type of brightness value"""
    pass

class LightTemperatureValueError(Exception):
    """Wrong kelvin value"""
    pass

class LightTemperatureTypeError(Exception):
    """Wrong type of kelvin value"""
    pass
class RGBValueError(Exception):
    """Wrong RGB value"""
    pass
class RGBTypeError(Exception):
    """Wrong type of RGB value"""
    pass
