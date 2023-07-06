import uuid

import gridworks.conversion_factors as cf

import gwatn.strategies.simple_resistive_hydronic.flo_utils as flo_utils
from gwatn.strategies.simple_resistive_hydronic.flo import (
    Flo_SimpleResistiveHydronic as Flo,
)
from gwatn.types import FloParamsSimpleresistivehydronic as FloParams


def test_flo_and_utils():
    params = FloParams(
        GNodeAlias="dw1.test",
        FloParamsUid=str(uuid.uuid4()),
        RtElecPriceUid=str(uuid.uuid4()),
        DistPriceUid=str(uuid.uuid4()),
        WeatherUid=str(uuid.uuid4()),
    )

    # Testing get_max_energy_kwh
    water_store_in_pounds = params.StoreSizeGallons * cf.POUNDS_OF_WATER_PER_GALLON
    assert water_store_in_pounds == 2001.6
    rwt_f = params.RequiredSourceWaterTempF - params.ReturnWaterDeltaTempF
    temp_delta_f = params.MaxStoreTempF - rwt_f
    assert temp_delta_f == 110

    # (pounds of water) * (temp_delta_f) is BTUS
    energy_btu = water_store_in_pounds * temp_delta_f
    assert energy_btu == 220176
    # cf.BTU_PER_KWH is 3412
    energy_kwh = energy_btu / cf.BTU_PER_KWH
    assert 64.52 < energy_kwh < 64.53
    assert flo_utils.get_max_energy_kwh(params) == energy_kwh

    flo = Flo(params=params, d_graph_id=str(uuid.uuid4()))

    assert flo.max_energy_kwh == flo.e_step_wh * flo.params.StorageSteps / 1000

    store_idx = 70
    ts_idx = 0
    # demonstrate that passive loss is the same whether or not the tank is stratified
    # or perfectly mixed
    hot_ratio = store_idx / params.StorageSteps
    rwt_f = params.RequiredSourceWaterTempF - params.ReturnWaterDeltaTempF
    avg_temp_f = hot_ratio * params.MaxStoreTempF + (1 - hot_ratio) * rwt_f
    store_pounds = params.StoreSizeGallons * cf.POUNDS_OF_WATER_PER_GALLON
    energy_above_ambient_wh = (
        (avg_temp_f - params.AmbientTempStoreF) * store_pounds * 1000 / cf.BTU_PER_KWH
    )
    slice_hrs = params.SliceDurationMinutes[ts_idx] / 60
    passive_loss_this_slice = (
        params.StorePassiveLossRatio * slice_hrs * energy_above_ambient_wh
    )
    # compare with results of flo_utils.get_passive_loss_wh, rounded to 3
    assert round(passive_loss_this_slice, 3) == round(
        flo_utils.get_passive_loss_wh(params, ts_idx, store_idx), 3
    )
