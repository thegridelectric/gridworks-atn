import time

import pendulum

from gwatn.csv_makers.scada_report_a import ScadaReportA_Maker


timezone_string = "US/Eastern"

t = time.time()
time_utc = pendulum.from_timestamp(t)

last_utc_midnight_unix_s = t - (t % (3600 * 24))
last_local_midnight_unix_s = last_utc_midnight_unix_s + 3600 * (
    time_utc.hour - time_utc.in_timezone(timezone_string).hour
)

maker = ScadaReportA_Maker()

maker.make_csv(
    last_local_midnight_unix_s, duration_hrs=24, atn_alias="hw1.isone.me.freedom.apple"
)
