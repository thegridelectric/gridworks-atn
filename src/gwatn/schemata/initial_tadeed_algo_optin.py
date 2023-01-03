"""Type initial.tadeed.algo.optin, version 002"""
import json
from typing import Any
from typing import Dict
from typing import Literal

from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwatn import property_format
from gwatn.property_format import predicate_validator


class InitialTadeedAlgoOptin(BaseModel):
    TerminalAssetAlias: str = Field(
        title="TerminalAssetAlias", description="A STRANGE KANGAROO."
    )  #
    TaOwnerAddr: str = Field(
        title="TaOwnerAddr",
        description="The GNodeAlias of the TerminalAsset owned by the TaOwner.",
    )  #
    ValidatorAddr: str = Field(
        title="ValidatorAddr",
        description="The Algorand address for the Validator of the TerminalAsset.",
    )  #
    SignedInitialDaemonFundingTxn: str = Field(
        title="SignedInitialDaemonFundingTxn",
        description="Funding transaction for the TaDaemon account, signed by the TaOwner.",
    )  #
    TypeName: Literal["initial.tadeed.algo.optin"] = Field(
        eq="initial.tadeed.algo.optin"
    )
    Version: str = "002"

    _validator_terminal_asset_alias = predicate_validator(
        "TerminalAssetAlias", property_format.is_lrd_alias_format
    )

    _validator_ta_owner_addr = predicate_validator(
        "TaOwnerAddr", property_format.is_algo_address_string_format
    )

    _validator_validator_addr = predicate_validator(
        "ValidatorAddr", property_format.is_algo_address_string_format
    )

    _validator_signed_initial_daemon_funding_txn = predicate_validator(
        "SignedInitialDaemonFundingTxn", property_format.is_algo_msg_pack_encoded
    )

    @root_validator(pre=True)
    def _axiom_1(cls, v) -> Any:
        """Axiom 1 (SignedTransaction) Decoded SignedInitialDaemonFundingTxn must have type SignedTransaction"""
        SignedTaDeedCreationTxn = v.get("SignedInitialDaemonFundingTxn", None)
        if not property_format.is_algo_msg_pack_encoded(SignedTaDeedCreationTxn):
            raise ValueError(
                f"SignedInitialDaemonFundingTxn: is_algo_msg_pack_encoded fails for [{SignedInitialDaemonFundingTxn}]"
            )
        txn = encoding.future_msgpack_decode(SignedTaDeedCreationTxn)
        if not isinstance(txn, SignedTaDeedCreationTxn):
            raise ValueError(
                "Axiom 1 (SignedTransaction): "
                "Decoded SignedInitialDaemonFundingTxn must have type SignedTransaction"
                f", got {type(txn)}"
            )
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class InitialTadeedAlgoOptin_Maker:
    type_name = "initial.tadeed.algo.optin"
    version = "002"

    def __init__(
        self,
        terminal_asset_alias: str,
        ta_owner_addr: str,
        validator_addr: str,
        signed_initial_daemon_funding_txn: str,
    ):
        self.tuple = InitialTadeedAlgoOptin(
            TerminalAssetAlias=terminal_asset_alias,
            TaOwnerAddr=ta_owner_addr,
            ValidatorAddr=validator_addr,
            SignedInitialDaemonFundingTxn=signed_initial_daemon_funding_txn,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: InitialTadeedAlgoOptin) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> InitialTadeedAlgoOptin:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> InitialTadeedAlgoOptin:
        d2 = dict(d)
        if "TerminalAssetAlias" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TerminalAssetAlias")
        if "TaOwnerAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TaOwnerAddr")
        if "ValidatorAddr" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ValidatorAddr")
        if "SignedInitialDaemonFundingTxn" not in d2.keys():
            raise SchemaError(f"dict {d2} missing SignedInitialDaemonFundingTxn")
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return InitialTadeedAlgoOptin(
            TerminalAssetAlias=d2["TerminalAssetAlias"],
            TaOwnerAddr=d2["TaOwnerAddr"],
            ValidatorAddr=d2["ValidatorAddr"],
            SignedInitialDaemonFundingTxn=d2["SignedInitialDaemonFundingTxn"],
            TypeName=d2["TypeName"],
            Version="002",
        )
