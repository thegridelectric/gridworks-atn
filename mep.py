import time
import pendulum
from gwatn.csv_makers.scada_report_a import ScadaReportA_Maker

ATNS = ["hw1.isone.ma.ng.lily",
]

OUT_STUB = "/home/ubuntu/gdrive/MillinocketData/LilyData"
timezone_string = "US/Eastern"

maker = ScadaReportA_Maker(out_stub=OUT_STUB)
while True:
    print(f"{pendulum.now().in_timezone(timezone_string).strftime('%Y/%m/%d %H:%M')} Regenerating spreadsheet")
    t = time.time()
    time_utc = pendulum.from_timestamp(t)
    last_utc_midnight_unix_s = t - (t % (3600 * 24))
    last_local_midnight_unix_s = last_utc_midnight_unix_s + 3600 * (
        time_utc.hour - time_utc.in_timezone(timezone_string).hour
    )
    start = last_utc_midnight_unix_s + 18 * 3600
    for atn_alias in ATNS:
        try:
            maker.make_csv(last_local_midnight_unix_s, duration_hrs=24, atn_alias=atn_alias)
        except Exception as e:
            print(f"Had trouble making csv for {atn_alias}: {e}.")

    time.sleep(1)