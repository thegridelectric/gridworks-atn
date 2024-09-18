import time
import pendulum
from gwatn.csv_makers.scada_report_a import ScadaReportA_Maker

ATN_ALIAS = "hw1.isone.ma.ng.lily"

OUT_STUB = "/home/ubuntu/gdrive/MillinocketData/Lily"
timezone_string = "America/New_York"

start = pendulum.datetime(2024,1,1,0,0,0,tz="America/New_York").int_timestamp

maker = ScadaReportA_Maker(out_stub=OUT_STUB)

for day in range(120):
    local_midnight_s = start + day*24*3600
    print(f"{pendulum.from_timestamp(local_midnight_s, tz = timezone_string).strftime('%Y/%m/%d %H:%M')}")
    try:
        maker.make_csv(local_midnight_s, 24, ATN_ALIAS)
    except Exception as e:         
        print(f"Had trouble making csv for {ATN_ALIAS}: {e}.")

# while True:
#     print(f"{pendulum.now().in_timezone(timezone_string).strftime('%Y/%m/%d %H:%M')} Regenerating spreadsheet")
#     t = time.time()
#     time_utc = pendulum.from_timestamp(t)
#     last_utc_midnight_unix_s = t - (t % (3600 * 24))
#     last_local_midnight_unix_s = last_utc_midnight_unix_s + 3600 * (
#         time_utc.hour - time_utc.in_timezone(timezone_string).hour
#     )
#     try:
#         maker.make_csv(last_local_midnight_unix_s, duration_hrs=24, atn_alias=ATN_ALIAS)
#     except Exception as e:
#         print(f"Had trouble making csv for {ATN_ALIAS}: {e}.")

#     time.sleep(1)