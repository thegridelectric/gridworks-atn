""" Heatpumpwithbooststore Flo Edge Class Definition """
from typing import Optional
from typing import no_type_check

from gwatn.data_classes.d_edge import DEdge


SIG_FIGS_FOR_OUTPUT = 6


class Edge__SpaceHeat__Water_HeatPumpAndBoost__Alpha(DEdge):
    def __init__(
        self,
        start_ts_idx: int,
        start_idx: int,
        end_idx: int,
        source_water_temp_f: Optional[float] = None,
        return_water_temp_f: Optional[float] = None,
        heat_pump_source_water_temp_f: Optional[float] = None,
        hp_electricity_avg_kw: Optional[float] = None,
        hp_thermal_energy_generated_avg_kw: Optional[float] = None,
        boost_electricity_used_avg_kw: Optional[float] = None,
        cost: Optional[float] = None,
    ):
        DEdge.__init__(
            self,
            start_ts_idx=start_ts_idx,
            start_idx=start_idx,
            end_idx=end_idx,
            cost=cost,
        )
        self.source_water_temp_f = source_water_temp_f
        self.return_water_temp_f = return_water_temp_f

        self.heat_pump_source_water_temp_f = heat_pump_source_water_temp_f
        self.hp_electricity_avg_kw = hp_electricity_avg_kw
        self.hp_thermal_energy_generated_avg_kw = hp_thermal_energy_generated_avg_kw
        self.boost_electricity_used_avg_kw = boost_electricity_used_avg_kw

    def __repr__(self) -> str:
        rep = f"DEdge => Time Slice Idx: {self.start_ts_idx}, StartIdx: {self.start_idx}, EndIdx: {self.end_idx}"
        if self.cost is not None:
            rep += f" Cost => {self.cost}"
        return rep
