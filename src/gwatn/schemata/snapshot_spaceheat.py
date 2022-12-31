"""Type snapshot.spaceheat, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks import property_format
from gridworks.errors import SchemaError
from gridworks.property_format import predicate_validator
from pydantic import BaseModel
from pydantic import validator

from gwatn.schemata.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat
from gwatn.schemata.telemetry_snapshot_spaceheat import TelemetrySnapshotSpaceheat_Maker


class SnapshotSpaceheat(BaseModel):
    FromGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    Snapshot: TelemetrySnapshotSpaceheat  #
    TypeName: Literal["snapshot.spaceheat"] = "snapshot.spaceheat"
    Version: str = "000"

    _validator_from_g_node_alias = predicate_validator(
        "FromGNodeAlias", property_format.is_lrd_alias_format
    )

    _validator_from_g_node_instance_id = predicate_validator(
        "FromGNodeInstanceId", property_format.is_uuid_canonical_textual
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["Snapshot"] = self.Snapshot.as_dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class SnapshotSpaceheat_Maker:
    type_name = "snapshot.spaceheat"
    version = "000"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        snapshot: TelemetrySnapshotSpaceheat,
    ):
        self.tuple = SnapshotSpaceheat(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            Snapshot=snapshot,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: SnapshotSpaceheat) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> SnapshotSpaceheat:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> SnapshotSpaceheat:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "Snapshot" not in d2.keys():
            raise SchemaError(f"dict {d2} missing Snapshot")
        if not isinstance(d2["Snapshot"], dict):
            raise SchemaError(
                f"d['Snapshot'] {d2['Snapshot']} must be a TelemetrySnapshotSpaceheat!"
            )
        snapshot = TelemetrySnapshotSpaceheat_Maker.dict_to_tuple(d2["Snapshot"])
        d2["Snapshot"] = snapshot
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return SnapshotSpaceheat(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            Snapshot=d2["Snapshot"],
            TypeName=d2["TypeName"],
            Version="000",
        )
