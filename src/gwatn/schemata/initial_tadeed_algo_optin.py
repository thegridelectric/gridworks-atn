"""Type initial.tadeed.algo.optin, version 002"""
import json
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from algosdk import encoding
from gridworks.errors import SchemaError
from pydantic import BaseModel
from pydantic import Field
from pydantic import root_validator
from pydantic import validator

from gwatn import property_format
from gwatn.property_format import predicate_validator


def check_is_lrd_format(candidate: str) -> None:
    """Lowercase AlphanumericString separated by periods, with the most
    significant word (on the left) starting with an alphabet character.
    """
    try:
        x = candidate.split(".")
    except:
        raise ValueError("Failed to seperate into words with split'.'")
    first_word: str = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word must start with alphabet char. Got '{first_word}'"
        )
    for word in x:
        w: str = str(word)
        if not w.isalnum():
            raise ValueError(f"words seperated by dots must be alphanumeric. Got '{w}'")
    if not candidate.islower():
        raise ValueError(f"alias must be lowercase. Got '{candidate}'")


def _axiom_1(v: Dict) -> Dict:
    SignedInitialDaemonFundingTxn = v.get("SignedInitialDaemonFundingTxn", None)
    if not property_format.is_algo_msg_pack_encoded(SignedInitialDaemonFundingTxn):
        raise ValueError(
            f"SignedInitialDaemonFundingTxn: is_algo_msg_pack_encoded fails for [{SignedInitialDaemonFundingTxn}]"
        )
    txn = encoding.future_msgpack_decode(SignedInitialDaemonFundingTxn)
    if not isinstance(txn, SignedInitialDaemonFundingTxn):
        raise ValueError(
            "Axiom 1 (SignedTransaction): "
            "Decoded SignedInitialDaemonFundingTxn must have type SignedTransaction"
            f", got {type(txn)}"
        )
    return v


class InitialTadeedAlgoOptin(BaseModel):
    """Used by TaOwner to instruct TaDaemonAPI to opt into the initial Algorand
    TaDeed, allowing the GNodeFactory to instantiate the TaOwner's TerminalAsset.

    In addition to attribute-level validations, the class is validated with
    the following rules:

      * **ValidatorAddr matches TerminalAssetAlias** The Algorand 2-sig Multi Address
      [GNodeFactoryAdmin, ValidatorAddr] has created a TaDeed for the TerminalAssetAlias.

      * **TaOwner funded Daemon** The private key associated to the public address
      TaOwnerAddr signed SignedInitialDaemonFundingTxn.

    """

    TerminalAssetAlias: str = Field(
        title="The GNodeAlias for the TerminalAsset GNode.",
        description="""
These formatting rules apply:

    * [LeftRightDot format]: Lowercase AlphanumericString separated by periods, with the most
    significant word (on the left) starting with an alphabet character
    * [TerminalAssetAlias format]: Final word is `ta` (for terminal asset)

""",
        example="d1.isone.me.freedom.apple.ta",
    )

    TaOwnerAddr: str = Field(
        description="The GNodeAlias of the TerminalAsset owned by the TaOwner.",
    )  #
    ValidatorAddr: str = Field(
        description="The Algorand address for the Validator of the TerminalAsset.",
    )  #
    SignedInitialDaemonFundingTxn: str = Field(
        description="Funding transaction for the TaDaemon account, signed by the TaOwner.",
    )  #
    TypeName: Literal["initial.tadeed.algo.optin"] = "initial.tadeed.algo.optin"

    Version: str = Field(title="Version of schema type", default="002")

    @validator("TerminalAssetAlias")
    def _validator_terminal_asset_alias(cls, v: str) -> str:
        try:
            check_is_lrd_format(v)
        except ValueError as e:
            raise ValueError(e)

    _validator_ta_owner_addr = predicate_validator(
        "TaOwnerAddr", property_format.is_algo_address_string_format
    )

    _validator_validator_addr = predicate_validator(
        "ValidatorAddr", property_format.is_algo_address_string_format
    )

    _validator_signed_initial_daemon_funding_txn = predicate_validator(
        "SignedInitialDaemonFundingTxn", property_format.is_algo_msg_pack_encoded
    )

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
