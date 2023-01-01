"""Type new.tadeed.algo.optin, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import validator

from gwatn import property_format
from gwatn.property_format import predicate_validator


class NewTadeedAlgoOptin(BaseModel):
    NewTaDeedIdx: int  #
    OldTaDeedIdx: int  #
    TaDaemonAddr: str  #
    ValidatorAddr: str  #
    SignedTaDeedCreationTxn: str  #
    TypeName: Literal["new.tadeed.algo.optin"] = "new.tadeed.algo.optin"
    Version: str = "000"

    _validator_ta_daemon_addr = predicate_validator(
        "TaDaemonAddr", property_format.is_algo_address_string_format
    )

    _validator_validator_addr = predicate_validator(
        "ValidatorAddr", property_format.is_algo_address_string_format
    )

    _validator_signed_ta_deed_creation_txn = predicate_validator(
        "SignedTaDeedCreationTxn", property_format.is_algo_msg_pack_encoded
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class NewTadeedAlgoOptin_Maker:
    type_name = "new.tadeed.algo.optin"
    version = "000"

    def __init__(
        self,
        new_ta_deed_idx: int,
        old_ta_deed_idx: int,
        ta_daemon_addr: str,
        validator_addr: str,
        signed_ta_deed_creation_txn: str,
    ):
        self.tuple = NewTadeedAlgoOptin(
            NewTaDeedIdx=new_ta_deed_idx,
            OldTaDeedIdx=old_ta_deed_idx,
            TaDaemonAddr=ta_daemon_addr,
            ValidatorAddr=validator_addr,
            SignedTaDeedCreationTxn=signed_ta_deed_creation_txn,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: NewTadeedAlgoOptin) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> NewTadeedAlgoOptin:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> NewTadeedAlgoOptin:
        d2 = dict(d)
        if "NewTaDeedIdx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing NewTaDeedIdx")
        if "OldTaDeedIdx" not in d2.keys():
            raise SchemaError(f"dict {d2} missing OldTaDeedIdx")
        if "TaDaemonAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TaDaemonAddr")
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "SignedTaDeedCreationTxn" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedTaDeedCreationTxn")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return NewTadeedAlgoOptin(
            NewTaDeedIdx=d2["NewTaDeedIdx"],
            OldTaDeedIdx=d2["OldTaDeedIdx"],
            TaDaemonAddr=d2["TaDaemonAddr"],
            ValidatorAddr=d2["ValidatorAddr"],
            SignedTaDeedCreationTxn=d2["SignedTaDeedCreationTxn"],
            TypeName=d2["TypeName"],
            Version="000",
        )
