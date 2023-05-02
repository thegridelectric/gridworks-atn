import csv
import json

import pendulum
from satn.config import Settings

from gwatn.types import AtnParamsHeatpumpwithbooststore as AtnParams
from gwatn.types import (
    AtnParamsReportHeatpumpwithbooststore_Maker as AtnParamsReport_Maker,
)
from gwatn.types.csv_distp_sync import CsvDistpSync_Maker
from gwatn.types.csv_eprt_sync import CsvEprtSync_Maker
from gwatn.types.csv_weather_forecast_sync import CsvWeatherForecastSync_Maker


eprt_csv = "input_data/elec_price_data.csv"
ep = CsvEprtSync_Maker(elec_price_file=eprt_csv).tuple

distp_csv = "input_data/dist_price_data.csv"
dp = CsvDistpSync_Maker(dist_price_file=distp_csv).tuple

temp_csv = "input_data/temperature_data.csv"
temp = CsvWeatherForecastSync_Maker(weather_csv=temp_csv).tuple

params_file = "input_data/atn_params_data.csv"
params = []
with open(params_file) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        params.append(row)
start = pendulum.datetime(year=2020, month=1, day=1, hour=4)

for j in range(1, 19):
    alias = params[1][j]
    atn_params = AtnParams(
        GNodeAlias=alias,
        GNodeInstanceId="00000000-0000-0000-0000-000000000000",
        BetaOt=params[2][j],
        HouseHeatingCapacity=params[3][j],
        AmbientPowerInKw=params[4][j],
        AnnualHvacKwhTh=params[5][j],
        StoreSizeGallons=params[8][j],
        RatedHeatpumpElectricityKw=params[9][j],
        StoreMaxPowerKw=params[10][j],
        SystemMaxHeatOutputDeltaTempF=params[11][j],
        SystemMaxHeatOutputGpm=params[12][j],
        SystemMaxHeatOutputSwtF=params[13][j],
        FloSlices=48,
        SliceDurationMinutes=60,
    )
    try:
        report = AtnParamsReport_Maker(
            g_node_alias=alias,
            g_node_instance_id=Settings().g_node_instance_id,
            time_unix_s=start.int_timestamp,
            atn_params=atn_params,
            irl_time_unix_s=None,
        ).tuple
    except:
        print(f"Problem with {alias}")

    file_name = f"input_data/eventstore/{alias}-{AtnParamsReport_Maker.type_name}-{start.int_timestamp * 1000}.json"
    json_object = json.dumps(report.as_dict())

    # Writing to sample.json
    with open(file_name, "w") as outfile:
        outfile.write(json_object)
