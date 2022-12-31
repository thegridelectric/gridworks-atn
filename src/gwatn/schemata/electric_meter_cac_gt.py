"""Type electric.meter.cac.gt, version 000"""
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

from gwatn.data_classes.cacs.electric_meter_cac import ElectricMeterCac
from gwatn.enums import LocalCommInterface
from gwatn.enums import MakeModel


class LocalCommInterface000SchemaEnum:
    enum_name: str = "local.comm.interface.000"
    symbols: List[str] = [
        "653c73b8",
        "0843a726",
        "9ec8bc49",
        "46ac6589",
        "efc144cd",
        "00000000",
        "c1e7a955",
        "ae2d4cd8",
        "a6a4ac9f",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class LocalCommInterface000(StrEnum):
    ANALOG_4_20_MA = auto()
    RS232 = auto()
    I2C = auto()
    WIFI = auto()
    SIMRABBIT = auto()
    UNKNOWN = auto()
    ETHERNET = auto()
    ONEWIRE = auto()
    RS485 = auto()

    @classmethod
    def default(cls) -> "LocalCommInterface000":
        return cls.UNKNOWN

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class LocalCommInterfaceMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> LocalCommInterface:
        if not LocalCommInterface000SchemaEnum.is_symbol(symbol):
            raise SchemaError(f"{symbol} must belong to LocalCommInterface000 symbols")
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, LocalCommInterface, LocalCommInterface.default())

    @classmethod
    def local_to_type(cls, local_comm_interface: LocalCommInterface) -> str:
        if not isinstance(local_comm_interface, LocalCommInterface):
            raise SchemaError(
                f"{local_comm_interface} must be of type {LocalCommInterface}"
            )
        versioned_enum = as_enum(
            local_comm_interface, LocalCommInterface000, LocalCommInterface000.default()
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, LocalCommInterface000] = {
        "653c73b8": LocalCommInterface000.ANALOG_4_20_MA,
        "0843a726": LocalCommInterface000.RS232,
        "9ec8bc49": LocalCommInterface000.I2C,
        "46ac6589": LocalCommInterface000.WIFI,
        "efc144cd": LocalCommInterface000.SIMRABBIT,
        "00000000": LocalCommInterface000.UNKNOWN,
        "c1e7a955": LocalCommInterface000.ETHERNET,
        "ae2d4cd8": LocalCommInterface000.ONEWIRE,
        "a6a4ac9f": LocalCommInterface000.RS485,
    }

    versioned_enum_to_type_dict: Dict[LocalCommInterface000, str] = {
        LocalCommInterface000.ANALOG_4_20_MA: "653c73b8",
        LocalCommInterface000.RS232: "0843a726",
        LocalCommInterface000.I2C: "9ec8bc49",
        LocalCommInterface000.WIFI: "46ac6589",
        LocalCommInterface000.SIMRABBIT: "efc144cd",
        LocalCommInterface000.UNKNOWN: "00000000",
        LocalCommInterface000.ETHERNET: "c1e7a955",
        LocalCommInterface000.ONEWIRE: "ae2d4cd8",
        LocalCommInterface000.RS485: "a6a4ac9f",
    }


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


class ElectricMeterCacGt(BaseModel):
    ComponentAttributeClassId: str  #
    MakeModel: MakeModel  #
    DisplayName: str  #
    MaxNumberOfCts: int  #
    LocalCommInterface: LocalCommInterface  #
    HasInternalCurrentMeasurement: bool  #
    UpdatePeriodMs: Optional[int] = None
    DefaultBaud: Optional[int] = None
    TypeName: Literal["electric.meter.cac.gt"] = "electric.meter.cac.gt"
    Version: str = "000"

    _validator_component_attribute_class_id = predicate_validator(
        "ComponentAttributeClassId", property_format.is_uuid_canonical_textual
    )

    @validator("MakeModel")
    def _validator_make_model(cls, v: MakeModel) -> MakeModel:
        return as_enum(v, MakeModel, MakeModel.UNKNOWNMAKE__UNKNOWNMODEL)

    _validator_max_number_of_cts = predicate_validator(
        "MaxNumberOfCts", property_format.is_positive_integer
    )

    @validator("LocalCommInterface")
    def _validator_local_comm_interface(
        cls, v: LocalCommInterface
    ) -> LocalCommInterface:
        return as_enum(v, LocalCommInterface, LocalCommInterface.UNKNOWN)

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["MakeModel"]
        MakeModel = as_enum(self.MakeModel, MakeModel, MakeModel.default())
        d["MakeModelGtEnumSymbol"] = MakeModelMap.local_to_type(MakeModel)
        del d["LocalCommInterface"]
        LocalCommInterface = as_enum(
            self.LocalCommInterface, LocalCommInterface, LocalCommInterface.default()
        )
        d["LocalCommInterfaceGtEnumSymbol"] = LocalCommInterfaceMap.local_to_type(
            LocalCommInterface
        )
        if d["UpdatePeriodMs"] is None:
            del d["UpdatePeriodMs"]
        if d["DefaultBaud"] is None:
            del d["DefaultBaud"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class ElectricMeterCacGt_Maker:
    type_name = "electric.meter.cac.gt"
    version = "000"

    def __init__(
        self,
        component_attribute_class_id: str,
        make_model: MakeModel,
        display_name: str,
        max_number_of_cts: int,
        local_comm_interface: LocalCommInterface,
        has_internal_current_measurement: bool,
        update_period_ms: Optional[int],
        default_baud: Optional[int],
    ):
        self.tuple = ElectricMeterCacGt(
            ComponentAttributeClassId=component_attribute_class_id,
            MakeModel=make_model,
            DisplayName=display_name,
            MaxNumberOfCts=max_number_of_cts,
            LocalCommInterface=local_comm_interface,
            HasInternalCurrentMeasurement=has_internal_current_measurement,
            UpdatePeriodMs=update_period_ms,
            DefaultBaud=default_baud,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: ElectricMeterCacGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> ElectricMeterCacGt:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ElectricMeterCacGt:
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
        if "MaxNumberOfCts" not in d2.keys():
            raise SchemaError(f"dict {d2} missing MaxNumberOfCts")
        if "LocalCommInterfaceGtEnumSymbol" not in d2.keys():
            raise SchemaError(f"dict {d2} missing LocalCommInterfaceGtEnumSymbol")
        if (
            d2["LocalCommInterfaceGtEnumSymbol"]
            in LocalCommInterface000SchemaEnum.symbols
        ):
            d2["LocalCommInterface"] = LocalCommInterfaceMap.type_to_local(
                d2["LocalCommInterfaceGtEnumSymbol"]
            )
        else:
            d2["LocalCommInterface"] = LocalCommInterface.default()
        if "HasInternalCurrentMeasurement" not in d2.keys():
            raise SchemaError(f"dict {d2} missing HasInternalCurrentMeasurement")
        if "UpdatePeriodMs" not in d2.keys():
            d2["UpdatePeriodMs"] = None
        if "DefaultBaud" not in d2.keys():
            d2["DefaultBaud"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return ElectricMeterCacGt(
            ComponentAttributeClassId=d2["ComponentAttributeClassId"],
            MakeModel=d2["MakeModel"],
            DisplayName=d2["DisplayName"],
            MaxNumberOfCts=d2["MaxNumberOfCts"],
            LocalCommInterface=d2["LocalCommInterface"],
            HasInternalCurrentMeasurement=d2["HasInternalCurrentMeasurement"],
            UpdatePeriodMs=d2["UpdatePeriodMs"],
            DefaultBaud=d2["DefaultBaud"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: ElectricMeterCacGt) -> ElectricMeterCac:
        if t.ComponentAttributeClassId in ElectricMeterCac.by_id.keys():
            dc = ElectricMeterCac.by_id[t.ComponentAttributeClassId]
        else:
            dc = ElectricMeterCac(
                component_attribute_class_id=t.ComponentAttributeClassId,
                make_model=t.MakeModel,
                display_name=t.DisplayName,
                max_number_of_cts=t.MaxNumberOfCts,
                local_comm_interface=t.LocalCommInterface,
                has_internal_current_measurement=t.HasInternalCurrentMeasurement,
                update_period_ms=t.UpdatePeriodMs,
                default_baud=t.DefaultBaud,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ElectricMeterCac) -> ElectricMeterCacGt:
        t = ElectricMeterCacGt_Maker(
            component_attribute_class_id=dc.component_attribute_class_id,
            make_model=dc.make_model,
            display_name=dc.display_name,
            max_number_of_cts=dc.max_number_of_cts,
            local_comm_interface=dc.local_comm_interface,
            has_internal_current_measurement=dc.has_internal_current_measurement,
            update_period_ms=dc.update_period_ms,
            default_baud=dc.default_baud,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> ElectricMeterCac:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ElectricMeterCac) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ElectricMeterCac:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
