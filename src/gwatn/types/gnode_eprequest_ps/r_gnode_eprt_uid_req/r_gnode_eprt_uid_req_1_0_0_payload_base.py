"""PayloadBase for r.gnode.eprt.uid.req.1_0_0"""
import datetime
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Tuple

import gwatn.types.hack_property_format as property_format


class PayloadBase(NamedTuple):
    FromGNodeAlias: str  #
    ToGNodeAlias: str  #
    FromGNodeInstanceId: str  #
    MessageId: str  #
    PriceUid: str  #
    IrlTimeUtc: Optional[str] = None
    WorldInstanceAlias: Optional[str] = None
    MpAlias: str = "r.gnode.eprt.uid.req.1_0_0"

    def asdict(self):
        d = self._asdict()
        if d["WorldInstanceAlias"] is None:
            del d["WorldInstanceAlias"]
        if d["IrlTimeUtc"] is None:
            del d["IrlTimeUtc"]
        return d

    def passes_derived_validations(self) -> Tuple[bool, Optional[List[str]]]:
        is_valid = True
        errors = []
        if self.MpAlias != "r.gnode.eprt.uid.req.1_0_0":
            is_valid = False
            errors.append(
                f"Payload requires MpAlias of r.gnode.eprt.uid.req.1_0_0, not {self.MpAlias}."
            )
        if not isinstance(self.FromGNodeAlias, str):
            is_valid = False
            errors.append(f"FromGNodeAlias {self.FromGNodeAlias} must have type str.")
        if not property_format.is_lrd_alias_format(self.FromGNodeAlias):
            is_valid = False
            errors.append(
                f"FromGNodeAlias {self.FromGNodeAlias} must have format GNodeLrdAliasFormat."
            )
        if not isinstance(self.ToGNodeAlias, str):
            is_valid = False
            errors.append(f"ToGNodeAlias {self.ToGNodeAlias} must have type str.")
        if not property_format.is_lrd_alias_format(self.ToGNodeAlias):
            is_valid = False
            errors.append(
                f"ToGNodeAlias {self.ToGNodeAlias} must have format GNodeLrdAliasFormat."
            )
        if not isinstance(self.FromGNodeInstanceId, str):
            is_valid = False
            errors.append(
                f"FromGNodeInstanceId {self.FromGNodeInstanceId} must have type str."
            )
        if not property_format.is_uuid_canonical_textual(self.FromGNodeInstanceId):
            is_valid = False
            errors.append(
                f"FromGNodeInstanceId {self.FromGNodeInstanceId} must have format UuidCanonicalTextual."
            )
        if not isinstance(self.MessageId, str):
            is_valid = False
            errors.append(f"MessageId {self.MessageId} must have type str.")
        if not property_format.is_uuid_canonical_textual(self.MessageId):
            is_valid = False
            errors.append(
                f"MessageId {self.MessageId} must have format UuidCanonicalTextual."
            )
        if not isinstance(self.PriceUid, str):
            is_valid = False
            errors.append(f"PriceUid {self.PriceUid} must have type str.")
        if not property_format.is_uuid_canonical_textual(self.PriceUid):
            is_valid = False
            errors.append(
                f"PriceUid {self.PriceUid} must have format UuidCanonicalTextual."
            )
        if self.WorldInstanceAlias:
            if not isinstance(self.WorldInstanceAlias, str):
                is_valid = False
                errors.append(
                    f"WorldInstanceAlias {self.WorldInstanceAlias} must have type str."
                )
            if not property_format.is_world_instance_alias_format(
                self.WorldInstanceAlias
            ):
                is_valid = False
                errors.append(
                    f"WorldInstanceAlias {self.WorldInstanceAlias} must have format WorldInstanceAliasFormat"
                )
        if self.IrlTimeUtc:
            if not isinstance(self.IrlTimeUtc, str):
                is_valid = False
                errors.append(f"IrlTimeUtc {self.IrlTimeUtc} must have type str.")
            if not property_format.is_log_style_utc_date_w_millis(self.IrlTimeUtc):
                is_valid = False
                errors.append(
                    f"IrlTimeUtc {self.IrlTimeUtc} must have format LogStyleUtcDateWMillis."
                )
        return is_valid, errors