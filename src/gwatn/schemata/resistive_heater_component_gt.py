"""Type resistive.heater.component.gt, version 000"""
import json
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from gridworks import property_format
from gridworks.errors import SchemaError
from gridworks.property_format import predicate_validator
from pydantic import BaseModel
from pydantic import validator

from gwatn.data_classes.components.resistive_heater_component import (
    ResistiveHeaterComponent,
)
from gwatn.schemata.resistive_heater_cac_gt import ResistiveHeaterCacGt
from gwatn.schemata.resistive_heater_cac_gt import ResistiveHeaterCacGt_Maker


class ResistiveHeaterComponentGt(BaseModel):
    ComponentId: str  #
    ComponentAttributeClass: ResistiveHeaterCacGt  #
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    TestedMaxHotMilliOhms: Optional[int] = None
    TestedMaxColdMilliOhms: Optional[int] = None
    TypeName: Literal["resistive.heater.component.gt"] = "resistive.heater.component.gt"
    Version: str = "000"

    _validator_component_id = predicate_validator(
        "ComponentId", property_format.is_uuid_canonical_textual
    )

    @validator("TestedMaxHotMilliOhms")
    def _validator_tested_max_hot_milli_ohms(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        if not property_format.is_positive_integer(v):
            raise ValueError(f"TestedMaxHotMilliOhms {v} must have PositiveInteger")
        return v

    @validator("TestedMaxColdMilliOhms")
    def _validator_tested_max_cold_milli_ohms(cls, v: Optional[int]) -> Optional[int]:
        if v is None:
            return v
        if not property_format.is_positive_integer(v):
            raise ValueError(f"TestedMaxColdMilliOhms {v} must have PositiveInteger")
        return v

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["ComponentAttributeClass"] = self.ComponentAttributeClass.as_dict()
        if d["DisplayName"] is None:
            del d["DisplayName"]
        if d["HwUid"] is None:
            del d["HwUid"]
        if d["TestedMaxHotMilliOhms"] is None:
            del d["TestedMaxHotMilliOhms"]
        if d["TestedMaxColdMilliOhms"] is None:
            del d["TestedMaxColdMilliOhms"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class ResistiveHeaterComponentGt_Maker:
    type_name = "resistive.heater.component.gt"
    version = "000"

    def __init__(
        self,
        component_id: str,
        component_attribute_class: ResistiveHeaterCacGt,
        display_name: Optional[str],
        hw_uid: Optional[str],
        tested_max_hot_milli_ohms: Optional[int],
        tested_max_cold_milli_ohms: Optional[int],
    ):
        self.tuple = ResistiveHeaterComponentGt(
            ComponentId=component_id,
            ComponentAttributeClass=component_attribute_class,
            DisplayName=display_name,
            HwUid=hw_uid,
            TestedMaxHotMilliOhms=tested_max_hot_milli_ohms,
            TestedMaxColdMilliOhms=tested_max_cold_milli_ohms,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: ResistiveHeaterComponentGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> ResistiveHeaterComponentGt:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ResistiveHeaterComponentGt:
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentId")
        if "ComponentAttributeClass" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentAttributeClass")
        if not isinstance(d2["ComponentAttributeClass"], dict):
            raise SchemaError(
                f"d['ComponentAttributeClass'] {d2['ComponentAttributeClass']} must be a ResistiveHeaterCacGt!"
            )
        component_attribute_class = ResistiveHeaterCacGt_Maker.dict_to_tuple(
            d2["ComponentAttributeClass"]
        )
        d2["ComponentAttributeClass"] = component_attribute_class
        if "DisplayName" not in d2.keys():
            d2["DisplayName"] = None
        if "HwUid" not in d2.keys():
            d2["HwUid"] = None
        if "TestedMaxHotMilliOhms" not in d2.keys():
            d2["TestedMaxHotMilliOhms"] = None
        if "TestedMaxColdMilliOhms" not in d2.keys():
            d2["TestedMaxColdMilliOhms"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return ResistiveHeaterComponentGt(
            ComponentId=d2["ComponentId"],
            ComponentAttributeClass=d2["ComponentAttributeClass"],
            DisplayName=d2["DisplayName"],
            HwUid=d2["HwUid"],
            TestedMaxHotMilliOhms=d2["TestedMaxHotMilliOhms"],
            TestedMaxColdMilliOhms=d2["TestedMaxColdMilliOhms"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: ResistiveHeaterComponentGt) -> ResistiveHeaterComponent:
        if t.ComponentId in ResistiveHeaterComponent.by_id.keys():
            dc = ResistiveHeaterComponent.by_id[t.ComponentId]
        else:
            dc = ResistiveHeaterComponent(
                component_id=t.ComponentId,
                component_attribute_class=t.ComponentAttributeClass,
                display_name=t.DisplayName,
                hw_uid=t.HwUid,
                tested_max_hot_milli_ohms=t.TestedMaxHotMilliOhms,
                tested_max_cold_milli_ohms=t.TestedMaxColdMilliOhms,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ResistiveHeaterComponent) -> ResistiveHeaterComponentGt:
        t = ResistiveHeaterComponentGt_Maker(
            component_id=dc.component_id,
            component_attribute_class=dc.component_attribute_class,
            display_name=dc.display_name,
            hw_uid=dc.hw_uid,
            tested_max_hot_milli_ohms=dc.tested_max_hot_milli_ohms,
            tested_max_cold_milli_ohms=dc.tested_max_cold_milli_ohms,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> ResistiveHeaterComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ResistiveHeaterComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ResistiveHeaterComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
