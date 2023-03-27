from gwproto import CallableDecoder
from gwproto import Decoders
from gwproto import MQTTCodec
from gwproto import create_message_payload_discriminator
from gwproto.messages import GtDispatchBoolean_Maker
from gwproto.messages import GtShCliAtnCmd_Maker
from gwproto.messages import GtShStatus_Maker
from gwproto.messages import PowerWatts_Maker
from gwproto.messages import SnapshotSpaceheat_Maker


S3MessageDecoder = create_message_payload_discriminator(
    "S3MessageDecoder",
    [
        "gwproto.messages",
    ],
)


class S3MQTTCodec(MQTTCodec):
    def __init__(self):
        super().__init__(
            Decoders.from_objects(
                [
                    GtDispatchBoolean_Maker,
                    GtShCliAtnCmd_Maker,
                    GtShStatus_Maker,
                    PowerWatts_Maker,
                    SnapshotSpaceheat_Maker,
                ],
                message_payload_discriminator=S3MessageDecoder,
            )
        )

    def validate_source_alias(self, source_alias: str):
        pass
