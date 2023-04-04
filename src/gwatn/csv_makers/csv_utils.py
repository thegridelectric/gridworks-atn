from typing import List
from typing import Optional

from pydantic import BaseModel

from gwatn.enums import TelemetryName
from gwatn.types.data_channel import DataChannel


APPLE_ATN_ALIAS = "hw1.isone.me.freedom.apple"
ORANGE_ATN_ALIAS = "hw1.isone.ct.newhaven.orange1"


class ChannelReading(BaseModel):
    Channel: DataChannel
    TimeUnixMs: int
    IntValue: Optional[int]
    FloatValue: Optional[float]
    TypeName: str = "channel.reading.000"


def get_named_channels(
    atn_alias: str = "hw1.isone.me.freedom.apple",
) -> List[DataChannel]:
    # TODO: replace when DataChannels exist in db in a way that
    # is uniquely referenced by the Atn
    scada_alias = atn_alias + ".scada"
    channels: List[DataChannel] = []
    if atn_alias == APPLE_ATN_ALIAS:
        channels.append(
            DataChannel(
                DisplayName="Buffer_Out_Temp",
                AboutName="a.buffer.out.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Dist_Pump_Power",
                AboutName="a.distsourcewater.pump",
                FromName="a.m",
                TelemetryName=TelemetryName.PowerW,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Dist_RWT",
                AboutName="a.distreturnwater.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Dist_Gallons",
                AboutName="a.distreturnwater.pump.flowmeter",
                FromName="a.distreturnwater.pump.flowmeter",
                TelemetryName=TelemetryName.GallonsTimes100,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Dist_SWT",
                AboutName="a.distsourcewater.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Heatpump_Power",
                AboutName="a.heatpump",
                FromName="a.m",
                TelemetryName=TelemetryName.PowerW,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Glycol_RWT",
                AboutName="a.heatpump.condensorloopreturn.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Glycol_Pump_Power",
                AboutName="a.heatpump.condensorloopsource.pump",
                FromName="a.m",
                TelemetryName=TelemetryName.PowerW,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Glycol_Gallons",
                AboutName="a.heatpump.condensorloopsource.pump.flowmeter",
                FromName="a.heatpump.condensorloopsource.pump.flowmeter",
                TelemetryName=TelemetryName.GallonsTimes100,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Glycol_SWT",
                AboutName="a.heatpump.condensorloopsource.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Hot_Store_In",
                AboutName="a.hotstore.in.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Hot_Store_Out_Gallons",
                AboutName="a.hotstore.out.flowmeter",
                FromName="a.hotstore.out.flowmeter",
                TelemetryName=TelemetryName.GallonsTimes100,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Hot_Store_Out",
                AboutName="a.hotstore.out.temp",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Hx_Pump_Power",
                AboutName="a.hxpump",
                FromName="a.m",
                TelemetryName=TelemetryName.PowerW,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Outside_Temp",
                AboutName="a.outside",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Elements_Atn_Dispatch",
                AboutName="a.tank1.elts.relay",
                FromName="hw1.isone.me.freedom.apple",
                TelemetryName=TelemetryName.RelayState,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Elements_SCADA_Dispatch",
                AboutName="a.tank1.elts.relay",
                FromName="a.s",
                TelemetryName=TelemetryName.RelayState,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Elements_Relay",
                AboutName="a.tank1.elts.relay",
                FromName="a.tank1.elts.relay",
                TelemetryName=TelemetryName.RelayState,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Elements_Power",
                AboutName="a.tank1.elts",
                FromName="a.m",
                TelemetryName=TelemetryName.PowerW,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Temp1",
                AboutName="a.tank1.temp1",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Temp2",
                AboutName="a.tank1.temp2",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
        channels.append(
            DataChannel(
                DisplayName="Tank1_Temp3",
                AboutName="a.tank1.temp3",
                FromName="a.s.analog.temp",
                TelemetryName=TelemetryName.WaterTempCTimes1000,
            )
        )
    return channels


def get_channel(
    atn_alias: str,
    from_name: str,
    about_name: str,
    telemetry_name: TelemetryName,
) -> DataChannel:
    if not isinstance(telemetry_name, TelemetryName):
        raise Exception(
            f"Error with from_name {from_name}, about_name {about_name}, telemetry_name {telemetry_name}"
        )
    named_channels = get_named_channels(atn_alias)
    this_channel_list = list(
        filter(
            lambda x: x.FromName == from_name
            and x.AboutName == about_name
            and x.TelemetryName == telemetry_name,
            named_channels,
        )
    )
    if len(this_channel_list) == 0:
        display_name = f"{about_name}_{telemetry_name.value}_{from_name}"
        return DataChannel(
            DisplayName=display_name,
            AboutName=about_name,
            FromName=from_name,
            TelemetryName=telemetry_name,
        )

    elif len(this_channel_list) == 1:
        return this_channel_list[0]
    else:
        raise Exception(f"duplicate channels {this_channel_list}")


def from_g_node_alias_from_kafka_topic(kafka_topic: str) -> str:
    try:
        from_alias = kafka_topic.split("-")[0]
    except:
        raise Exception(f"Failure getting from g node alias from kafka topic")
    return from_alias


def type_name_from_kafka_topic(kafka_topic: str) -> str:
    """
    Returns the type name from the kafka topic
    Args:
        kafka_topic (str):

    Returns:
        type_name
    """
    try:
        type_name = kafka_topic.split("-")[1]
    except:
        raise Exception(f"Failure getting type name from kafka topic")
    return type_name


def kafka_topic_from_s3_filename(s3_filename: str) -> str:
    try:
        topic = "-".join(s3_filename.split("/")[3].split("-")[0:2])
    except:
        raise Exception(f"Failure getting kafka topic from type name")
    return topic
