"""Type pipe.flow.sensor.cac.gt, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional

from fastapi_utils.enums import StrEnum
from gridworks import property_format
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from gridworks.property_format import predicate_validator
from pydantic import BaseModel
from pydantic import validator

from gwatn.data_classes.cacs.pipe_flow_sensor_cac import PipeFlowSensorCac
from gwatn.enums import MakeModel


class SpaceheatMakeModel000SchemaEnum:
    enum_name: str = "spaceheat.make.model.000"
    symbols: List[str] = [
        "127b0db8",
        "597ca6af",
        "00000000",
        "e81d74a8",
        "076da322",
        "f8b497e8",
        "fabfa505",
        "acd93fb3",
        "d300635e",
        "c75d269f",
        "4bb099ce",
        "899778cd",
        "a8d9a70d",
        "08da3f7d",
        "e3364590",
        "90566a90",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class SpaceheatMakeModel000(StrEnum):
    FREEDOM__RELAY = auto()
    OMEGAEZO__FTB800FLO = auto()
    UNKNOWNMAKE__UNKNOWNMODEL = auto()
    GRIDWORKS__SIMBOOL30AMPRELAY = auto()
    GRIDWORKS__SIMPM1 = auto()
    GRIDWORKS__WATERTEMPHIGHPRECISION = auto()
    NCD__PR814SPST = auto()
    ADAFRUIT__642 = auto()
    SCHNEIDERELECTRIC__IEM3455 = auto()
    OPENENERGY__EMONPI = auto()
    EGAUGE__3010 = auto()
    RHEEM__XE50T10H45U0 = auto()
    MAGNELAB__SCT0300050 = auto()
    YMDC__SCT013100 = auto()
    G1__NCD_ADS1115__TEWA_NTC_10K_A = auto()
    G1__NCD_ADS1115__AMPH_NTC_10K_A = auto()

    @classmethod
    def default(cls) -> "SpaceheatMakeModel000":
        return cls.UNKNOWNMAKE__UNKNOWNMODEL

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class MakeModelMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> MakeModel:
        if not SpaceheatMakeModel000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to SpaceheatMakeModel000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, MakeModel, MakeModel.default())

    @classmethod
    def local_to_type(cls, make_model: MakeModel) -> str:
        if not isinstance(make_model, MakeModel):
            raise SchemaError(f"{make_model} must be of type {MakeModel}")
        versioned_enum = as_enum(
            make_model, SpaceheatMakeModel000, SpaceheatMakeModel000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, SpaceheatMakeModel000] = {
        "127b0db8": SpaceheatMakeModel000.FREEDOM__RELAY,
        "597ca6af": SpaceheatMakeModel000.OMEGAEZO__FTB800FLO,
        "00000000": SpaceheatMakeModel000.UNKNOWNMAKE__UNKNOWNMODEL,
        "e81d74a8": SpaceheatMakeModel000.GRIDWORKS__SIMBOOL30AMPRELAY,
        "076da322": SpaceheatMakeModel000.GRIDWORKS__SIMPM1,
        "f8b497e8": SpaceheatMakeModel000.GRIDWORKS__WATERTEMPHIGHPRECISION,
        "fabfa505": SpaceheatMakeModel000.NCD__PR814SPST,
        "acd93fb3": SpaceheatMakeModel000.ADAFRUIT__642,
        "d300635e": SpaceheatMakeModel000.SCHNEIDERELECTRIC__IEM3455,
        "c75d269f": SpaceheatMakeModel000.OPENENERGY__EMONPI,
        "4bb099ce": SpaceheatMakeModel000.EGAUGE__3010,
        "899778cd": SpaceheatMakeModel000.RHEEM__XE50T10H45U0,
        "a8d9a70d": SpaceheatMakeModel000.MAGNELAB__SCT0300050,
        "08da3f7d": SpaceheatMakeModel000.YMDC__SCT013100,
        "e3364590": SpaceheatMakeModel000.G1__NCD_ADS1115__TEWA_NTC_10K_A,
        "90566a90": SpaceheatMakeModel000.G1__NCD_ADS1115__AMPH_NTC_10K_A,
    }

    versioned_enum_to_type_dict: Dict[SpaceheatMakeModel000, str] = {
        SpaceheatMakeModel000.FREEDOM__RELAY: "127b0db8",
        SpaceheatMakeModel000.OMEGAEZO__FTB800FLO: "597ca6af",
        SpaceheatMakeModel000.UNKNOWNMAKE__UNKNOWNMODEL: "00000000",
        SpaceheatMakeModel000.GRIDWORKS__SIMBOOL30AMPRELAY: "e81d74a8",
        SpaceheatMakeModel000.GRIDWORKS__SIMPM1: "076da322",
        SpaceheatMakeModel000.GRIDWORKS__WATERTEMPHIGHPRECISION: "f8b497e8",
        SpaceheatMakeModel000.NCD__PR814SPST: "fabfa505",
        SpaceheatMakeModel000.ADAFRUIT__642: "acd93fb3",
        SpaceheatMakeModel000.SCHNEIDERELECTRIC__IEM3455: "d300635e",
        SpaceheatMakeModel000.OPENENERGY__EMONPI: "c75d269f",
        SpaceheatMakeModel000.EGAUGE__3010: "4bb099ce",
        SpaceheatMakeModel000.RHEEM__XE50T10H45U0: "899778cd",
        SpaceheatMakeModel000.MAGNELAB__SCT0300050: "a8d9a70d",
        SpaceheatMakeModel000.YMDC__SCT013100: "08da3f7d",
        SpaceheatMakeModel000.G1__NCD_ADS1115__TEWA_NTC_10K_A: "e3364590",
        SpaceheatMakeModel000.G1__NCD_ADS1115__AMPH_NTC_10K_A: "90566a90",
    }


class PipeFlowSensorCacGt(BaseModel):
    ComponentAttributeClassId: str  #
    MakeModel: MakeModel  #
    DisplayName: str  #
    CommsMethod: Optional[str] = None
    TypeName: Literal["pipe.flow.sensor.cac.gt"] = "pipe.flow.sensor.cac.gt"
    Version: str = "000"

    _validator_component_attribute_class_id = predicate_validator(
        "ComponentAttributeClassId", property_format.is_uuid_canonical_textual
    )

    @validator("MakeModel")
    def _validator_make_model(cls, v: MakeModel) -> MakeModel:
        return as_enum(v, MakeModel, MakeModel.UNKNOWNMAKE__UNKNOWNMODEL)

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["MakeModel"]
        MakeModel = as_enum(self.MakeModel, MakeModel, MakeModel.default())
        d["MakeModelGtEnumSymbol"] = MakeModelMap.local_to_type(MakeModel)
        if d["CommsMethod"] is None:
            del d["CommsMethod"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class PipeFlowSensorCacGt_Maker:
    type_name = "pipe.flow.sensor.cac.gt"
    version = "000"

    def __init__(
        self,
        component_attribute_class_id: str,
        make_model: MakeModel,
        display_name: str,
        comms_method: Optional[str],
    ):
        self.tuple = PipeFlowSensorCacGt(
            ComponentAttributeClassId=component_attribute_class_id,
            MakeModel=make_model,
            DisplayName=display_name,
            CommsMethod=comms_method,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: PipeFlowSensorCacGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> PipeFlowSensorCacGt:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> PipeFlowSensorCacGt:
        d2 = dict(d)
        if "ComponentAttributeClassId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentAttributeClassId")
        if "MakeModelGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MakeModelGtEnumSymbol")
        if d2["MakeModelGtEnumSymbol"] in SpaceheatMakeModel000SchemaEnum.symbols:
            d2["MakeModel"] = MakeModelMap.type_to_local(d2["MakeModelGtEnumSymbol"])
        else:
            d2["MakeModel"] = MakeModel.default()
        if "DisplayName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing DisplayName")
        if "CommsMethod" not in d2.keys():
            d2["CommsMethod"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return PipeFlowSensorCacGt(
            ComponentAttributeClassId=d2["ComponentAttributeClassId"],
            MakeModel=d2["MakeModel"],
            DisplayName=d2["DisplayName"],
            CommsMethod=d2["CommsMethod"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: PipeFlowSensorCacGt) -> PipeFlowSensorCac:
        if t.ComponentAttributeClassId in PipeFlowSensorCac.by_id.keys():
            dc = PipeFlowSensorCac.by_id[t.ComponentAttributeClassId]
        else:
            dc = PipeFlowSensorCac(
                component_attribute_class_id=t.ComponentAttributeClassId,
                make_model=t.MakeModel,
                display_name=t.DisplayName,
                comms_method=t.CommsMethod,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: PipeFlowSensorCac) -> PipeFlowSensorCacGt:
        t = PipeFlowSensorCacGt_Maker(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            comms_method=dc.comms_method,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> PipeFlowSensorCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: PipeFlowSensorCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> PipeFlowSensorCac:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
