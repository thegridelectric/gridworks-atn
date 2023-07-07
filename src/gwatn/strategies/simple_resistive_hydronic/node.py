""" SimpleResistiveHydronic DNode Definition
"""
from typing import Optional

from gwatn.data_classes.d_node import DNode


SIG_FIGS_FOR_OUTPUT = 6


class Node_SimpleResistiveHydronic(DNode):
    def __init__(
        self,
        ts_idx: int,
        store_idx: int,
        energy_wh: float,
    ):
        """
        A node in the SimpleResistiveHydronic Dijkstra graph.

        [More Info](https://gridworks-atn.readthedocs.io/en/latest/simple-resistive-hydronic.html)
        """

        DNode.__init__(
            self,
            ts_idx=ts_idx,
            store_idx=store_idx,
        )
        self.store_idx = store_idx
        """
        The "fullness" of the thermal store, as a number ranging from 0 (which
        corresponds to the tank uniformly at the return water temperature of the heating system) to the
        params.StorageSteps (which corresponds to the tank uniformly at the maximum water temperature
        for the tank). Since the model assumes perfect stratification with an idealized and totally
        horizontal thermocline, as soon as there is ANY additional energy in the tank it happens at the
        top with max water temp that can be used to provide the maximum thermal transfer to the heating
        system (albiet for possibly a short time).
        """
        self.energy_wh = energy_wh
        """
        The energy in Wh associated to this node. It is linear in the store_idx, and goes from 0 to
        the flo.max_energy_kwh * 1000.
        """

    def __repr__(
        self,
    ) -> str:
        rep = f"DNode => TimeSliceIdx: {self.ts_idx}, StoreIdx: {self.store_idx}"
        if self.path_cost:
            rep += f", Path cost: ${round(self.path_cost, 3)}"
        if self.energy_wh:
            rep += f", Energy: {round(self.energy_wh / 1000, 2)} kWh"
        return rep
