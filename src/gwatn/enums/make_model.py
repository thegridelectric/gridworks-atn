from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MakeModel(StrEnum):
    """
    Determines Make/Model of device associated to a Spaceheat Node supervised by SCADA

    Choices and descriptions:

      * UnknownMake__UnknownModel:
      * Egauge__4030:
      * NCD__PR8-14-SPST:
      * Adafruit__642:
      * GridWorks__TSnap1:
      * GridWorks__WaterTempHighPrecision:
      * Gridworks__SimPm1:
      * SchneiderElectric__Iem3455:
      * GridWorks__SimBool30AmpRelay:
      * OpenEnergy__EmonPi:
      * Magnelab__SCT-0300-050:
      * YMDC__SCT013-100:
      * GridWorks__SimTSnap1:
      * Atlas__EzFlo:
    """

    UNKNOWNMAKE__UNKNOWNMODEL = auto()
    EGAUGE__4030 = auto()
    MAGNELAB__SCT0300050 = auto()
    YMDC__SCT013100 = auto()
    GRIDWORKS__SIMTSNAP1 = auto()
    ATLAS__EZFLO = auto()
    NCD__PR814SPST = auto()
    ADAFRUIT__642 = auto()
    GRIDWORKS__TSNAP1 = auto()
    GRIDWORKS__WATERTEMPHIGHPRECISION = auto()
    GRIDWORKS__SIMPM1 = auto()
    SCHNEIDERELECTRIC__IEM3455 = auto()
    GRIDWORKS__SIMBOOL30AMPRELAY = auto()
    OPENENERGY__EMONPI = auto()

    @classmethod
    def default(cls) -> "MakeModel":
        """
        Returns default value UNKNOWNMAKE__UNKNOWNMODEL
        """
        return cls.UNKNOWNMAKE__UNKNOWNMODEL

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
