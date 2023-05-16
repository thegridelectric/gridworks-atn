"""Payload for r.weather.tmy.temp.1_0_0"""
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from gwatn.types.ws_typicalmodeledyear_gnode.r_weather_tmy_temp.r_weather_tmy_temp_1_0_0_payload_base import (
    PayloadBase,
)


class Payload(PayloadBase):
    def is_valid(self) -> Tuple[bool, Optional[List[str]]]:
        is_valid, errors = self.passes_derived_validations()
        if len(errors) > 0:
            errors.insert(0, "Errors making r.weather.tmy.temp.1_0_0 msg.")
        return is_valid, errors

    # hand-code schema axiom validations below
