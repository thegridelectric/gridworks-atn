"""Type join.dispatch.contract, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

import gridworks.algo_utils as algo_utils
import gridworks.api_utils as api_utils
import gridworks.gw_config as config
from algosdk import encoding
from algosdk.future import transaction
from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
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


def check_is_algo_msg_pack_encoded(v: str) -> None:
    """
    AlgoMSgPackEncoded format: the format of an  transaction sent to
    the Algorand blockchain.

    Raises:
        ValueError: if not AlgoMSgPackEncoded  format
    """
    import algosdk

    try:
        algosdk.encoding.future_msgpack_decode(v)
    except Exception as e:
        raise ValueError(f"Not AlgoMsgPackEncoded format: {e}")


class JoinDispatchContract(BaseModel):
    """Sent from a Scada to its paired AtomicTNode on RabbitMQ.

    This is sent as an invitation to join the DispatchContract. Upon receipt of this,
    the AtomicTNode can check that the DispatchContract has finished the first part of
    its bootstrapping. This means it is well-funded, and also has the Scada Cert Id
    and the Scada Addr publicly available. The AtomicTNode can check these against
    the signature provided by the SCADA in its invitation. An AtomicTNode actor accepts
    the invitation by finishing the Dispatch Contract bootstrap (which it can only do
    if its Algorand Account holds the associated TaTradingRights certificate) and
    then responding to the SCADA via RabbitMQ with a dispatch.contract.confirmed payload.

    https://gridworks.readthedocs.io/en/latest/dispatch-contract.html
    """

    FromGNodeAlias: str = Field(
        title="FromGNodeAlias",
    )
    FromGNodeInstanceId: str = Field(
        title="FromGNodeInstanceId",
    )
    DispatchContractAppId: int = Field(
        title="DispatchContractAppId",
    )
    SignedProof: str = Field(
        title="SignedProof",
    )
    TypeName: Literal["join.dispatch.contract"] = "join.dispatch.contract"
    Version: str = "000"

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

    @validator("SignedProof")
    def _check_signed_proof(cls, v: str) -> str:
        try:
            check_is_algo_msg_pack_encoded(v)
        except ValueError as e:
            raise ValueError(
                f"SignedProof failed AlgoMsgPackEncoded format validation: {e}"
            )
        return v

    @root_validator
    def check_axiom_0(cls, v: dict) -> dict:
        """
        Axiom 0: ScadaCert matches FromGNodeAlias.
        The name in the ScadaCert should be the GNodeAlias of the TerminalAsset corresponding
        to the sending SCADA. Therefore, FromGNodeAlias should be equal to the name of the
        ScadaCert ASA with `.scada` appended.
        """
        txn = encoding.future_msgpack_decode(v.get("SignedProof", None))
        DispatchContractAppId = v.get("DispatchContractAppId", None)
        FromGNodeAlias = v.get("FromGNodeAlias", None)

        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class JoinDispatchContract_Maker:
    type_name = "join.dispatch.contract"
    version = "000"

    def __init__(
        self,
        from_g_node_alias: str,
        from_g_node_instance_id: str,
        dispatch_contract_app_id: int,
        signed_proof: str,
    ):
        self.tuple = JoinDispatchContract(
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            DispatchContractAppId=dispatch_contract_app_id,
            SignedProof=signed_proof,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: JoinDispatchContract) -> str:
        """
        Given a Python class object, returns the serialized JSON type object
        """
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> JoinDispatchContract:
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
    def dict_to_tuple(cls, d: dict[str, Any]) -> JoinDispatchContract:
        d2 = dict(d)
        if "FromGNodeAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeAlias")
        if "FromGNodeInstanceId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing FromGNodeInstanceId")
        if "DispatchContractAppId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing DispatchContractAppId")
        if "SignedProof" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedProof")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return JoinDispatchContract(
            FromGNodeAlias=d2["FromGNodeAlias"],
            FromGNodeInstanceId=d2["FromGNodeInstanceId"],
            DispatchContractAppId=d2["DispatchContractAppId"],
            SignedProof=d2["SignedProof"],
            TypeName=d2["TypeName"],
            Version="000",
        )
