from typing import NamedTuple


class Aliases(NamedTuple):
    HexCode = int  # Hex 0-255 values
    KelvinTemp = int  # from 1000 to 10000
    RGBColor = tuple[int, int, int]  # every int from 0 to 255

class Features(NamedTuple):
    brightness: bool
    colortemp: bool
    color: bool
