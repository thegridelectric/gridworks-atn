"""MessageMaker for r.gnode.distp.req.1_0_0"""

import time
import uuid
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from gridworks.errors import SchemaError

import gwatn.types.hack_test_dummy as test_dummy
from gwatn.types.gnode_distprequest_ps.r_gnode_distp_req.r_gnode_distp_req_1_0_0_payload import (
    Payload,
)
from gwatn.types.hack_type_base import HackTypeBase
from gwatn.types.hack_utils import log_style_utc_date_w_millis


class R_Gnode_Distp_Req_1_0_0(HackTypeBase):
    mp_alias = "r.gnode.distp.req.1_0_0"
    routing_key_base = "gnode.distprequest.ps"

    @classmethod
    def create_payload_from_camel_dict(cls, d: dict) -> Payload:
        if "MpAlias" not in d.keys():
            d["MpAlias"] = "r.gnode.distp.req.1_0_0"
        if "IrlTimeUtc" not in d.keys():
            d["IrlTimeUtc"] = None
        if "WorldInstanceAlias" not in d.keys():
            d["WorldInstanceAlias"] = None
        p = Payload(
            MpAlias=d["MpAlias"],
            MessageId=d["MessageId"],
            ToGNodeAlias=d["ToGNodeAlias"],
            IrlTimeUtc=d["IrlTimeUtc"],
            FromGNodeAlias=d["FromGNodeAlias"],
            FromGNodeInstanceId=d["FromGNodeInstanceId"],
            PriceUid=d["PriceUid"],
            WorldInstanceAlias=d["WorldInstanceAlias"],
        )
        is_valid, errors = p.is_valid()
        if not is_valid:
            raise SchemaError(errors)
        return p

    @classmethod
    def payload_is_valid(
        cls, payload_as_dict: Dict[str, Any]
    ) -> Tuple[bool, Optional[List[str]]]:
        try:
            p = cls.create_payload_from_camel_dict(payload_as_dict)
        except SchemaError as e:
            errors = [e]
            return False, errors
        return p.is_valid()

    def __init__(
        self,
        agent,
        to_g_node_alias: str,
        price_uid: str,
        irl_time_utc: Optional[str] = None,
    ):
        super().__init__(routing_key_base="gnode.distprequest.ps", agent=agent)
        self.errors = []
        self.payload = None
        if agent is None:
            raise Exception(
                f"Message protocol {R_Gnode_Distp_Req_1_0_0.mp_alias} must be generated by a message agent"
            )
        if agent == test_dummy.TEST_DUMMY_AGENT:
            from_g_node_alias = test_dummy.TEST_DUMMY_G_NODE_ALIAS
            from_g_node_instance_id = test_dummy.TEST_DUMMY_G_NODE_INSTANCE_ID
            world_instance_alias = test_dummy.TEST_DUMMY_WORLD_INSTANCE_ALIAS
            irl_time_utc = log_style_utc_date_w_millis(time.time())
        else:
            if not agent.gni.g_node.is_g_node:
                raise Exception(
                    f"Message protocol {R_Gnode_Distp_Req_1_0_0.mp_alias} must come from a GNode"
                )
            from_g_node_alias = agent.gni.g_node.alias
            from_g_node_instance_id = agent.gni.g_node_instance_id
            if agent.world_instance.is_simulated:
                world_instance_alias = agent.world_instance.alias
            else:
                world_instance_alias = None
            if agent.is_debug_mode:
                irl_time_utc = log_style_utc_date_w_millis(time.time())
            else:
                irl_time_utc = None

        p = Payload(
            MpAlias=R_Gnode_Distp_Req_1_0_0.mp_alias,
            WorldInstanceAlias=world_instance_alias,
            FromGNodeAlias=from_g_node_alias,
            FromGNodeInstanceId=from_g_node_instance_id,
            ToGNodeAlias=to_g_node_alias,
            IrlTimeUtc=irl_time_utc,
            PriceUid=price_uid,
            MessageId=str(uuid.uuid4()),
        )

        is_valid, errors = p.is_valid()
        if is_valid is False:
            raise SchemaError(f"Failed to create payload due to these errors: {errors}")
        self.payload = p