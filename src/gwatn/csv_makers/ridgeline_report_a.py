import time
from typing import List
from typing import NamedTuple
from typing import Optional

import pendulum
import xlsxwriter
from gwproto.enums import TelemetryName
from pydantic import BaseModel

from gwatn.csv_makers.scada_report_a import ScadaReportA_Maker
from gwatn.enums import Unit


OUT_STUB = "output_data/freedom_flow"
timezone_string = "US/Eastern"


def c_to_f(temp_c: float) -> float:
    return (temp_c * 1.8) + 32


class RidgelineOutputRow(BaseModel):
    TimeUtc: str
    TimeEastern: str
    DistSwtTempF: Optional[float]
    DistRwtTempF: Optional[float]
    DistFlowGpm: Optional[float]
    GlycolSwtTempF: Optional[float]
    GlycolRwtTempF: Optional[float]
    GlycolFlowGpm: Optional[float]


class DataChannel(NamedTuple):
    AboutShNodeName: str
    DaveName: str
    InTelemetryName: TelemetryName
    OutUnits: Unit


class DataChannelItem(BaseModel):
    Channel: DataChannel
    TimeUnixMs: int
    TimeUtc: str
    Value: float


DIST_SWT = DataChannel(
    AboutShNodeName="a.distsourcewater.temp",
    DaveName="Dist SWT",
    InTelemetryName=TelemetryName.WaterTempCTimes1000,
    OutUnits=Unit.Fahrenheit,
)

DIST_RWT = DataChannel(
    AboutShNodeName="a.distreturnwater.temp",
    DaveName="Dist RWT",
    InTelemetryName=TelemetryName.WaterTempCTimes1000,
    OutUnits=Unit.Fahrenheit,
)

DIST_FLOW = DataChannel(
    AboutShNodeName="a.distsourcewater.pump.flowmeter",
    DaveName="Dist Flow",
    InTelemetryName=TelemetryName.GallonsTimes100,
    OutUnits=Unit.Gpm,
)


GLYCOL_SWT = DataChannel(
    AboutShNodeName="a.heatpump.condensorloopsource.temp",
    DaveName="Glycol SWT",
    InTelemetryName=TelemetryName.WaterTempCTimes1000,
    OutUnits=Unit.Fahrenheit,
)

GLYCOL_RWT = DataChannel(
    AboutShNodeName="a.heatpump.condensorloopreturn.temp",
    DaveName="Glycol RWT",
    InTelemetryName=TelemetryName.WaterTempCTimes1000,
    OutUnits=Unit.Fahrenheit,
)

GLYCOL_FLOW = DataChannel(
    AboutShNodeName="a.heatpump.condensorloopsource.pump.flowmeter",
    DaveName="Glycol Flow",
    InTelemetryName=TelemetryName.GallonsTimes100,
    OutUnits=Unit.Gpm,
)


def export_excel(
    start_s: int, channels: List[DataChannel], sync_rows: List[RidgelineOutputRow]
) -> str:
    duration_hrs = 24
    start_utc = pendulum.from_timestamp(start_s)
    start_local = start_utc.in_timezone(timezone_string)
    start_local.strftime("%Y/%m/%d %H:%M:%S")
    file_name = f"{OUT_STUB}/{start_local.strftime('%Y%m%d')}_freedom_flow.xlsx"
    print(f"Will attempt to write to {file_name}")
    workbook = xlsxwriter.Workbook(file_name)
    w = workbook.add_worksheet()
    w.freeze_panes(3, 0)
    header_format = workbook.add_format({"bg_color": "#E6F4D8", "align": "right"})
    data_format = workbook.add_format({"bg_color": "#E6F4D8"})
    date_width = 13
    channel_width = 13
    w.set_column("A:A", date_width)
    w.set_column("B:B", date_width)
    w.set_column("C:C", channel_width)
    w.set_column("D:D", channel_width)
    w.set_column("E:E", channel_width)
    w.set_column("F:F", channel_width)
    w.set_column("G:G", channel_width)
    w.set_column("H:H", 5)
    w.write(0, 0, "Start Date (ET)", header_format)
    w.write(1, 0, start_local.strftime("%Y/%m/%d"), header_format)
    w.write(0, 8, "Data for Millinocket pilot first house (Freedom), from GridWorks")
    w.write(2, 0, "Eastern Time", header_format)

    for i in range(len(channels)):
        ch = channels[i]
        w.write(0, 1 + i, ch.AboutShNodeName, header_format)
        w.write(1, 1 + i, ch.OutUnits.value, header_format)
        w.write(2, 1 + i, ch.DaveName, header_format)

    for i in range(len(sync_rows)):
        row = sync_rows[i]
        w.write(3 + i, 0, row.TimeEastern, data_format)
        w.write(3 + i, 1, row.DistSwtTempF, data_format)
        w.write(3 + i, 2, row.DistRwtTempF, data_format)
        w.write(3 + i, 3, row.DistFlowGpm, data_format)
        w.write(3 + i, 4, row.GlycolSwtTempF, data_format)
        w.write(3 + i, 5, row.GlycolRwtTempF, data_format)
        w.write(3 + i, 6, row.GlycolFlowGpm, data_format)

    end = len(sync_rows) + 3
    dist_chart = workbook.add_chart({"type": "line"})
    dist_chart.add_series(
        {
            "name": f"Sheet1!$B$3",
            "categories": f"Sheet1!$A$4:$A${end}",
            "values": f"=Sheet1!$B$4:$B${end}",
            "line": {"color": "red"},
        }
    )
    dist_chart.add_series(
        {
            "name": f"Sheet1!$C$3",
            "values": f"=Sheet1!$C$4:$C${end}",
            "line": {"color": "blue"},
        }
    )
    dist_chart.add_series(
        {
            "name": f"Sheet1!$D$3",
            "values": f"=Sheet1!$D$4:$D${end}",
            "y2_axis": True,
            "line": {"color": "orange"},
        }
    )
    dist_chart.set_y_axis({"name": "Deg F", "min": 90})
    dist_chart.set_y2_axis({"name": "Gpm", "max": 12})
    dist_chart.set_title(
        {"name": f'Distribution Loop {start_local.strftime("%m/%d/%Y")}'}
    )
    dist_chart.set_size({"width": 720, "height": 432})
    w.insert_chart("I4", dist_chart)

    glycol_chart = workbook.add_chart({"type": "line"})
    glycol_chart.add_series(
        {
            "name": f"Sheet1!$E$3",
            "categories": f"Sheet1!$A$4:$A${end}",
            "values": f"=Sheet1!$E$4:$E${end}",
            "line": {"color": "red"},
        }
    )
    glycol_chart.add_series(
        {
            "name": f"Sheet1!$F$3",
            "values": f"=Sheet1!$F$4:$F${end}",
            "line": {"color": "blue"},
        }
    )
    glycol_chart.add_series(
        {
            "name": f"Sheet1!$G3",
            "values": f"=Sheet1!$G$4:$G${end}",
            "y2_axis": True,
            "line": {"color": "orange"},
        }
    )
    glycol_chart.set_y_axis({"name": "Deg F", "min": 90})
    glycol_chart.set_y2_axis({"name": "Gpm", "max": 24})
    glycol_chart.set_title({"name": f'Glycol Loop {start_local.strftime("%m/%d/%Y")}'})
    glycol_chart.set_size({"width": 720, "height": 432})
    w.insert_chart("I28", glycol_chart)
    workbook.close()
    return file_name


def make_spreadsheet(
    start_s: Optional[int] = None,
) -> str:
    atn_alias = "hw1.isone.me.freedom.apple"
    if start_s is None:
        t = time.time()
        time_utc = pendulum.from_timestamp(t)

        last_utc_midnight_unix_s = t - (t % (3600 * 24))
        start_s = last_utc_midnight_unix_s + 3600 * (
            time_utc.hour - time_utc.in_timezone(timezone_string).hour
        )
    start_time_unix_ms = int(start_s * 1000)
    duration_hrs = 24
    maker = ScadaReportA_Maker()
    rows = maker.get_csv_rows(
        start_time_unix_ms=start_time_unix_ms,
        duration_hrs=duration_hrs,
        atn_alias=atn_alias,
    )

    temp_channels = [DIST_SWT, DIST_RWT, GLYCOL_SWT, GLYCOL_RWT]
    flow_channels = [DIST_FLOW, GLYCOL_FLOW]
    channels = [DIST_SWT, DIST_RWT, DIST_FLOW, GLYCOL_SWT, GLYCOL_RWT, GLYCOL_FLOW]

    readings = {}
    scada_alias = atn_alias + ".scada"
    for ch in channels:
        readings[ch] = sorted(
            list(
                filter(
                    lambda x: x.AboutShNode == ch.AboutShNodeName
                    and x.FromShNode != scada_alias,
                    rows,
                )
            ),
            key=lambda row: row.TimeUnixMs,
        )

    ridgeline_readings = {}
    for ch in flow_channels:
        dc_list = []
        for i in range(1, len(readings[ch])):
            prev_flow_gallons_times_100 = readings[ch][i - 1].Value
            this_flow_gallons_times_100 = readings[ch][i].Value
            delta_gallons = (
                this_flow_gallons_times_100 - prev_flow_gallons_times_100
            ) / 100
            prev_s = readings[ch][i - 1].IntTimeUnixS
            this_s = readings[ch][i].IntTimeUnixS
            if this_s == prev_s:
                flow_gpm = None
                print("duplicate times!")
                print(f"i is {i}")
                print(f"readings[ch][i-1] is {readings[ch][i-1]}")
                print(f"readings[ch][i] is {readings[ch][i]}")
            else:
                delta_min = (this_s - prev_s) / 60
                flow_gpm = delta_gallons / delta_min
            dc_list.append(
                DataChannelItem(
                    Channel=ch,
                    TimeUnixMs=readings[ch][i].TimeUnixMs,
                    TimeUtc=readings[ch][i].TimeUtc,
                    Value=round(flow_gpm, 1),
                )
            )
        ridgeline_readings[ch] = dc_list

    for ch in temp_channels:
        dc_list = []
        for i in range(0, len(readings[ch])):
            temp_c = readings[ch][i].Value / 1000
            temp_f = round(c_to_f(temp_c), 2)
            dc_list.append(
                DataChannelItem(
                    Channel=ch,
                    TimeUnixMs=readings[ch][i].TimeUnixMs,
                    TimeUtc=readings[ch][i].TimeUtc,
                    Value=temp_f,
                )
            )
        ridgeline_readings[ch] = dc_list

    sync_rows = []
    end_s = max(map(lambda x: x.TimeUnixMs, rows)) / 1000
    total_minutes = int((end_s - start_s) / 60)
    for i in range(total_minutes):
        sync_s = start_s + i * 60
        vals = {}
        for ch in channels:
            before = sorted(
                list(
                    filter(
                        lambda x: int(x.TimeUnixMs / 1000) <= sync_s,
                        ridgeline_readings[ch],
                    )
                ),
                key=lambda row: -row.TimeUnixMs,
            )
            if len(before) == 0:
                vals[ch] = None
            else:
                vals[ch] = before[0].Value

        sync_rows.append(
            RidgelineOutputRow(
                TimeUtc=pendulum.from_timestamp(sync_s).strftime("%Y/%m/%d %H:%M:%S"),
                TimeEastern=pendulum.from_timestamp(sync_s)
                .in_timezone(timezone_string)
                .strftime("%H:%M"),
                DistSwtTempF=vals[DIST_SWT],
                DistRwtTempF=vals[DIST_RWT],
                DistFlowGpm=vals[DIST_FLOW],
                # DistFlowGpm=3.5,
                GlycolSwtTempF=vals[GLYCOL_SWT],
                GlycolRwtTempF=vals[GLYCOL_RWT],
                GlycolFlowGpm=vals[GLYCOL_FLOW],
                # GlycolFlowGpm=8.2
            )
        )
    return export_excel(start_s, channels, sync_rows)


# ch = DIST_FLOW
# #ch = GLYCOL_FLOW
# ch = DIST_RWT
# delta_s = []
# for i in range(1,len(readings[ch])):
#     row = readings[ch][i]
#     prev = readings[ch][i-1]
#     delta_s.append([row.TimeUtc, row.IntTimeUnixS, row.IntTimeUnixS - prev.IntTimeUnixS])
#
# med = list(filter(lambda x: x[2]>65, delta_s))
# print(delta_s)
#
# dist_flow_long =[['2023-03-28 00:33:50', 1679963630, 236],
#  ['2023-03-28 01:02:03', 1679965323, 124],
#  ['2023-03-28 01:09:36', 1679965776, 333],
#  ['2023-03-28 01:50:00', 1679968200, 302],
#  ['2023-03-28 04:22:04', 1679977324, 185],
#  ['2023-03-28 06:04:58', 1679983498, 315],
#  ['2023-03-28 06:13:21', 1679984001, 202],
#  ['2023-03-28 06:29:24', 1679984964, 297],
#  ['2023-03-28 07:47:58', 1679989678, 183],
#  ['2023-03-28 08:32:11', 1679992331, 180],
#  ['2023-03-28 10:51:45', 1680000705, 152],
#  ['2023-03-28 11:06:19', 1680001579, 86],
#  ['2023-03-28 13:18:53', 1680009533, 285]]
#
# glycol_flow_long = [['2023-03-28 00:33:50', 1679963630, 290],
#  ['2023-03-28 01:02:03', 1679965323, 179],
#  ['2023-03-28 01:09:36', 1679965776, 333],
#  ['2023-03-28 01:50:00', 1679968200, 302],
#  ['2023-03-28 04:22:04', 1679977324, 168],
#  ['2023-03-28 06:04:58', 1679983498, 307],
#  ['2023-03-28 06:13:21', 1679984001, 262],
#  ['2023-03-28 06:29:24', 1679984964, 297],
#  ['2023-03-28 07:47:58', 1679989678, 233],
#  ['2023-03-28 08:32:11', 1679992331, 178],
#  ['2023-03-28 10:51:45', 1680000705, 164],
#  ['2023-03-28 11:06:19', 1680001579, 89],
#  ['2023-03-28 13:18:53', 1680009533, 280]]
#
# dist_swt_above_65 = [['2023-03-28 00:33:47', 1679963627, 282],
#  ['2023-03-28 01:02:00', 1679965320, 124],
#  ['2023-03-28 01:09:33', 1679965773, 333],
#  ['2023-03-28 01:49:57', 1679968197, 318],
#  ['2023-03-28 04:22:01', 1679977321, 123],
#  ['2023-03-28 06:04:55', 1679983495, 335],
#  ['2023-03-28 06:13:18', 1679983998, 253],
#  ['2023-03-28 06:29:21', 1679984961, 275],
#  ['2023-03-28 07:47:55', 1679989675, 200],
#  ['2023-03-28 08:32:08', 1679992328, 177],
#  ['2023-03-28 10:51:42', 1680000702, 113],
#  ['2023-03-28 11:06:16', 1680001576, 78],
#  ['2023-03-28 13:18:50', 1680009530, 273]]
