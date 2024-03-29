"""Type gt.dispatch.boolean, version 110"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import validator


def check_is_uuid_canonical_textual(v: str) -> None:
    """
    UuidCanonicalTextual format:  A string of hex words separated by hyphens
    of length 8-4-4-4-12.

    Raises:
        ValueError: if not UuidCanonicalTextual format
    """
    try:
        x = v.split("-")
    except AttributeError as e:
        raise ValueError(f"Failed to split on -: {e}")
    if len(x) != 5:
        raise ValueError(f"{v} split by '-' did not have 5 words")
    for hex_word in x:
        try:
            int(hex_word, 16)
        except ValueError:
            raise ValueError(f"Words of {v} are not all hex")
    if len(x[0]) != 8:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[1]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[2]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[3]) != 4:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")
    if len(x[4]) != 12:
        raise ValueError(f"{v} word lengths not 8-4-4-4-12")


def check_is_left_right_dot(v: str) -> None:
    """
    LeftRightDot format: Lowercase alphanumeric words separated by periods,
    most significant word (on the left) starting with an alphabet character.

    Raises:
        ValueError: if not LeftRightDot format
    """
    from typing import List

    try:
        x: List[str] = v.split(".")
    except:
        raise ValueError(f"Failed to seperate {v} into words with split'.'")
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(f"Most significant word of {v} must start with alphabet char.")
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of {v} split by by '.' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of {v} must be lowercase.")


def check_is_reasonable_unix_time_ms(v: str) -> None:
    """
    ReasonableUnixTimeMs format: time in unix milliseconds between Jan 1 2000 and Jan 1 3000

    Raises:
        ValueError: if not ReasonableUnixTimeMs format
    """
    import pendulum

    if pendulum.parse("2000-01-01T00:00:00Z").int_timestamp * 1000 > v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be after Jan 1 2000")
    if pendulum.parse("3000-01-01T00:00:00Z").int_timestamp * 1000 < v:  # type: ignore[attr-defined]
        raise ValueError(f"{v} must be before Jan 1 3000")


class GtDispatchBoolean(BaseModel):
    """.

    Boolean dispatch command sent over the cloud broker from one GNode (FromGNodeAlias/ FromGNodeId) to another (ToGNodeAlias). AboutNodeAlias is the node getting dispatched. It may be a GNode, but it can also be a SpaceHeatNode.
    """

    AboutNodeName: str = Field(
        title="The Spaceheat Node getting dispatched",
    )
    ToGNodeAlias: str = Field(
        title="GNodeAlias of the SCADA",
        description=" [More info](https://gridworks.readthedocs.io/en/latest/scada.html).",
    )
    FromGNodeAlias: str = Field(
        title="GNodeAlias of AtomicTNode",
        description=" [More info](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html).",
    )
    FromGNodeInstanceId: str = Field(
        title="GNodeInstance of the AtomicTNode",
    )
    RelayState: int = Field(
        title="0 or 1",
    )
    SendTimeUnixMs: int = Field(
        title="Time the AtomicTNode sends the dispatch, by its clock",
    )
    TypeName: Literal["gt.dispatch.boolean"] = "gt.dispatch.boolean"
    Version: str = "110"

    @validator("AboutNodeName")
    def _check_about_node_name(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"AboutNodeName failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("ToGNodeAlias")
    def _check_to_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(f"ToGNodeAlias failed LeftRightDot format validation: {e}")
        return v

    @validator("FromGNodeAlias")
    def _check_from_g_node_alias(cls, v: str) -> str:
        try:
            check_is_left_right_dot(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeAlias failed LeftRightDot format validation: {e}"
            )
        return v

    @validator("FromGNodeInstanceId")
    def _check_from_g_node_instance_id(cls, v: str) -> str:
        try:
            check_is_uuid_canonical_textual(v)
        except ValueError as e:
            raise ValueError(
                f"FromGNodeInstanceId failed UuidCanonicalTextual format validation: {e}"
            )
        return v

    @validator("SendTimeUnixMs")
    def _check_send_time_unix_ms(cls, v: int) -> int:
        try:
            check_is_reasonable_unix_time_ms(v)
        except ValueError as e:
            raise ValueError(
                f"SendTimeUnixMs failed ReasonableUnixTimeMs format validation: {e}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))  # noqa


class GtDispatchBoolean_Maker:
    type_name = "gt.dispatch.boolean"
    version = "110"

    def __init__(
        self,
        about_node_name: str,
        to_g_node_alias: str,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        relay_state: int,
        send_time_unix_ms: int,
    ):
        self.tuple = GtDispatchBoolean(
            AboutNodeName=about_node_name,
            ToGNodeAlias=to_g_node_alias,
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            RelayState=relay_state,
            SendTimeUnixMs=send_time_unix_ms,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: GtDispatchBoolean) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> GtDispatchBoolean:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> GtDispatchBoolean:
        d2 = dict(d)
        if "AboutNodeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing AboutNodeName")
        if "ToGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ToGNodeAlias")
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "RelayState" not in d2.keys():
            raise SchemaError(f"dict {d2} missing RelayState")
        if "SendTimeUnixMs" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SendTimeUnixMs")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return GtDispatchBoolean(
            AboutNodeName=d2["AboutNodeName"],
            ToGNodeAlias=d2["ToGNodeAlias"],
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            RelayState=d2["RelayState"],
            SendTimeUnixMs=d2["SendTimeUnixMs"],
            TypeName=d2["TypeName"],
            Version="110",
        )
