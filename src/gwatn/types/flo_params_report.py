"""Type flo.params.report, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field
from pydantic import validator

from gwatn.types.flo_params import FloParams
from gwatn.types.flo_params import FloParams_Maker


class FloParamsReport(BaseModel):
    """Flo Params Report.

    Type used for a message provided by an AtomicTNode or SCADA actor re the flo parameters just used to run a FLO.
    [More info](https://gridworks-atn.readthedocs.io/en/latest/flo.html#flo-params).
    """

    GNodeAlias: str = Field(
        title="GNodeAlias",
    )
    GNodeInstanceId: str = Field(
        title="GNodeInstanceId",
    )
    FloParamsTypeName: str = Field(
        title="FloParamsTypeName",
    )
    FloParamsTypeVersion: str = Field(
        title="FloParamsTypeVersion",
    )
    ReportGeneratedTimeUnixS: int = Field(
        title="ReportGeneratedTimeUnixS",
    )
    IrlTimeUnixS: Optional[int] = Field(
        title="IrlTimeUnixS",
        default=None,
    )
    Params: FloParams = Field(
        title="Params",
    )
    TypeName: str = Field(
        title="TypeName",
        default="flo.params.report",
    )
    Version: str = "000"

    class Config:
        extra = Extra.allow

    @validator("TypeName")
    def _check_type_name(cls, v: str) -> str:
        if not v.startswith("flo.params.report"):
            raise ValueError(f"TypeName {v} must start with 'flo.params.report'")
        return v

    @validator("GNodeAlias")
    def _check_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"GNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("GNodeInstanceId")
    def _check_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"GNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("FloParamsTypeName")
    def _check_flo_params_type_name(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FloParamsTypeName failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("ReportGeneratedTimeUnixS")
    def _check_report_generated_time_unix_s(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_s(v)
        except ValueError as e:
            raise ValueError(
                f"ReportGeneratedTimeUnixS failed ReasonableUnixTimeS format validation: {e}"
            )
        return v

    @validator("IrlTimeUnixS")
    def _check_irl_time_unix_s(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        try:
            check_is_reasonable_unix_time_s(v)
        except ValueError as e:
            raise ValueError(
                f"IrlTimeUnixS failed ReasonableUnixTimeS format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        if d["IrlTimeUnixS"] is None:
            del d["IrlTimeUnixS"]
        d["Params"] = self.Params.as_dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class FloParamsReport_Maker:
    type_name = "flo.params.report"
    version = "000"

    def __init__(
        self,
        g_node_alias: str,
        g_node_instance_id: str,
        flo_params_type_name: str,
        flo_params_type_version: str,
        report_generated_time_unix_s: int,
        irl_time_unix_s: Optional[int],
        params: FloParams,
    ):
        self.tuple = FloParamsReport(
            GNodeAlias=g_node_alias,
            GNodeInstanceId=g_node_instance_id,
            FloParamsTypeName=flo_params_type_name,
            FloParamsTypeVersion=flo_params_type_version,
            ReportGeneratedTimeUnixS=report_generated_time_unix_s,
            IrlTimeUnixS=irl_time_unix_s,
            Params=params,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: FloParamsReport) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> FloParamsReport:
        """
        Given a serialized JSON type object, returns the Python class object
        """
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> FloParamsReport:
        d2 = dict(d)
        if "GNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeAlias")
        if "GNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing GNodeInstanceId")
        if "FloParamsTypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FloParamsTypeName")
        if "FloParamsTypeVersion" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FloParamsTypeVersion")
        if "ReportGeneratedTimeUnixS" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ReportGeneratedTimeUnixS")
        if "IrlTimeUnixS" not in d2.keys():
            d2["IrlTimeUnixS"] = None
        if "Params" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Params")
        if not isinstance(d2["Params"], dict):
            raise SchemaError(f"d['Params'] {d2['Params']} must be a FloParams!")
        params = FloParams_Maker.dict_to_tuple(d2["Params"])
        d2["Params"] = params
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return FloParamsReport(
            GNodeAlias=d2["GNodeAlias"],
            GNodeInstanceId=d2["GNodeInstanceId"],
            FloParamsTypeName=d2["FloParamsTypeName"],
            FloParamsTypeVersion=d2["FloParamsTypeVersion"],
            ReportGeneratedTimeUnixS=d2["ReportGeneratedTimeUnixS"],
            IrlTimeUnixS=d2["IrlTimeUnixS"],
            Params=d2["Params"],
            TypeName=d2["TypeName"],
            Version="000",
        )
