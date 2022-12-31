"""Type telemetry.snapshot.spaceheat, version 000"""
import json
from enum import auto
from typing import Any
from typing import Dict
from typing import List
from typing import Literal

from fastapi_utils.enums import StrEnum
from gridworks import property_format
from gridworks.errors import SchemaError
from gridworks.message import as_enum
from gridworks.property_format import predicate_validator
from pydantic import BaseModel
from pydantic import validator

from gwatn.enums import TelemetryName


class SpaceheatTelemetryName000SchemaEnum:
    enum_name: str = "spaceheat.telemetry.name.000"
    symbols: List[str] = [
        "00000000",
        "af39eec9",
        "5a71d4b3",
        "c89d0ba1",
        "793505aa",
        "d70cce28",
        "ad19e79c",
        "329a68c0",
        "aeed9c8e",
        "bb6fdd59",
        "e0bb014b",
        "337b8659",
    ]

    @classmethod
    def is_symbol(cls, candidate: str) -> bool:
        if candidate in cls.symbols:
            return True
        return False


class SpaceheatTelemetryName000(StrEnum):
    Unknown = auto()
    PowerW = auto()
    RelayState = auto()
    WaterTempCTimes1000 = auto()
    WaterTempFTimes1000 = auto()
    WaterFlowGpmTimes100 = auto()
    CurrentRmsMicroAmps = auto()
    GallonsPerMinuteTimes10 = auto()
    CurrentRmsMilliAmps = auto()
    VoltageRmsMilliVolts = auto()
    PhaseAngleDegreesTimes10 = auto()
    WattHours = auto()

    @classmethod
    def default(cls) -> "SpaceheatTelemetryName000":
        return cls.Unknown

    @classmethod
    def values(cls) -> List[str]:
        return [elt.value for elt in cls]


class TelemetryNameMap:
    @classmethod
    def type_to_local(cls, symbol: str) -> TelemetryName:
        if not SpaceheatTelemetryName000SchemaEnum.is_symbol(symbol):
            raise SchemaError(
                f"{symbol} must belong to SpaceheatTelemetryName000 symbols"
            )
        versioned_enum = cls.type_to_versioned_enum_dict[symbol]
        return as_enum(versioned_enum, TelemetryName, TelemetryName.default())

    @classmethod
    def local_to_type(cls, telemetry_name: TelemetryName) -> str:
        if not isinstance(telemetry_name, TelemetryName):
            raise SchemaError(f"{telemetry_name} must be of type {TelemetryName}")
        versioned_enum = as_enum(
            telemetry_name,
            SpaceheatTelemetryName000,
            SpaceheatTelemetryName000.default(),
        )
        return cls.versioned_enum_to_type_dict[versioned_enum]

    type_to_versioned_enum_dict: Dict[str, SpaceheatTelemetryName000] = {
        "00000000": SpaceheatTelemetryName000.Unknown,
        "af39eec9": SpaceheatTelemetryName000.PowerW,
        "5a71d4b3": SpaceheatTelemetryName000.RelayState,
        "c89d0ba1": SpaceheatTelemetryName000.WaterTempCTimes1000,
        "793505aa": SpaceheatTelemetryName000.WaterTempFTimes1000,
        "d70cce28": SpaceheatTelemetryName000.WaterFlowGpmTimes100,
        "ad19e79c": SpaceheatTelemetryName000.CurrentRmsMicroAmps,
        "329a68c0": SpaceheatTelemetryName000.GallonsPerMinuteTimes10,
        "aeed9c8e": SpaceheatTelemetryName000.CurrentRmsMilliAmps,
        "bb6fdd59": SpaceheatTelemetryName000.VoltageRmsMilliVolts,
        "e0bb014b": SpaceheatTelemetryName000.PhaseAngleDegreesTimes10,
        "337b8659": SpaceheatTelemetryName000.WattHours,
    }

    versioned_enum_to_type_dict: Dict[SpaceheatTelemetryName000, str] = {
        SpaceheatTelemetryName000.Unknown: "00000000",
        SpaceheatTelemetryName000.PowerW: "af39eec9",
        SpaceheatTelemetryName000.RelayState: "5a71d4b3",
        SpaceheatTelemetryName000.WaterTempCTimes1000: "c89d0ba1",
        SpaceheatTelemetryName000.WaterTempFTimes1000: "793505aa",
        SpaceheatTelemetryName000.WaterFlowGpmTimes100: "d70cce28",
        SpaceheatTelemetryName000.CurrentRmsMicroAmps: "ad19e79c",
        SpaceheatTelemetryName000.GallonsPerMinuteTimes10: "329a68c0",
        SpaceheatTelemetryName000.CurrentRmsMilliAmps: "aeed9c8e",
        SpaceheatTelemetryName000.VoltageRmsMilliVolts: "bb6fdd59",
        SpaceheatTelemetryName000.PhaseAngleDegreesTimes10: "e0bb014b",
        SpaceheatTelemetryName000.WattHours: "337b8659",
    }


class TelemetrySnapshotSpaceheat(BaseModel):
    ReportTimeUnixMs: int  #
    AboutNodeAliasList: List[str]  #
    ValueList: List[int]  #
    TelemetryNameList: List[TelemetryName]
    #
    TypeName: Literal["telemetry.snapshot.spaceheat"] = "telemetry.snapshot.spaceheat"
    Version: str = "000"

    _validator_report_time_unix_ms = predicate_validator(
        "ReportTimeUnixMs", property_format.is_reasonable_unix_time_ms
    )

    @validator("AboutNodeAliasList")
    def _validator_about_node_alias_list(cls, v: List) -> List:
        for elt in v:
            if not property_format.is_lrd_alias_format(elt):
                raise ValueError(
                    f"failure of predicate is_lrd_alias_format() on elt {elt} of AboutNodeAliasList"
                )
        return v

    @validator("TelemetryNameList")
    def _validator_telemetry_name_list(
        cls, v: SpaceheatTelemetryName000
    ) -> [SpaceheatTelemetryName000]:
        if not isinstance(v, List):
            raise ValueError("TelemetryNameList must be a list!")
        enum_list = []
        for elt in v:
            enum_list.append(as_enum(elt, TelemetryName, TelemetryName.Unknown))
        return enum_list

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        del d["TelemetryNameList"]
        telemetry_name_list = []
        for elt in self.TelemetryNameList:
            telemetry_name_list.append(TelemetryNameMap.local_to_type(elt))
        d["TelemetryNameList"] = telemetry_name_list
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class TelemetrySnapshotSpaceheat_Maker:
    type_name = "telemetry.snapshot.spaceheat"
    version = "000"

    def __init__(
        self,
        report_time_unix_ms: int,
        about_node_alias_list: List[str],
        value_list: List[int],
        telemetry_name_list: List[TelemetryName],
    ):
        self.tuple = TelemetrySnapshotSpaceheat(
            ReportTimeUnixMs=report_time_unix_ms,
            AboutNodeAliasList=about_node_alias_list,
            ValueList=value_list,
            TelemetryNameList=telemetry_name_list,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: TelemetrySnapshotSpaceheat) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> TelemetrySnapshotSpaceheat:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> TelemetrySnapshotSpaceheat:
        d2 = dict(d)
        if "ReportTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ReportTimeUnixMs")
        if "AboutNodeAliasList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AboutNodeAliasList")
        if "ValueList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValueList")
        if "TelemetryNameList" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TelemetryNameList")
        telemetry_name_list = []
        if not isinstance(d2["TelemetryNameList"], List):
            raise SchemaError("TelemetryNameList must be a List!")
        for elt in d2["TelemetryNameList"]:
            if elt in SpaceheatTelemetryName000SchemaEnum.symbols:
                v = TelemetryNameMap.type_to_local(elt)
            else:
                v = SpaceheatTelemetryName000.Unknown  #

            telemetry_name_list.append(v)
        d2["TelemetryNameList"] = telemetry_name_list
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return TelemetrySnapshotSpaceheat(
            ReportTimeUnixMs=d2["ReportTimeUnixMs"],
            AboutNodeAliasList=d2["AboutNodeAliasList"],
            ValueList=d2["ValueList"],
            TelemetryNameList=d2["TelemetryNameList"],
            TypeName=d2["TypeName"],
            Version="000",
        )
