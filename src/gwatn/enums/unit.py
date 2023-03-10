from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class Unit(StrEnum):
    """
    Specifies the physical unit of sensed data reported by SCADA

    Choices and descriptions:

      * Unknown:
      * Unitless:
      * W:
      * Celcius:
      * Fahrenheit:
      * Gpm:
      * WattHours:
      * AmpsRms:
      * VoltsRms:
      * Gallons:
    """

    Unknown = auto()
    Unitless = auto()
    W = auto()
    Celcius = auto()
    Fahrenheit = auto()
    Gpm = auto()
    WattHours = auto()
    AmpsRms = auto()
    VoltsRms = auto()
    Gallons = auto()

    @classmethod
    def default(cls) -> "Unit":
        """
        Returns default value Unknown
        """
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
