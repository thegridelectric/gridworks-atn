"""Type electric.meter.component.gt, version 000"""
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

from gwatn.data_classes.components.electric_meter_component import (
    ElectricMeterComponent,
)
from gwatn.schemata.electric_meter_cac_gt import ElectricMeterCacGt
from gwatn.schemata.electric_meter_cac_gt import ElectricMeterCacGt_Maker


class ElectricMeterComponentGt(BaseModel):
    ComponentId: str  #
    ComponentAttributeClass: ElectricMeterCacGt  #
    DisplayName: Optional[str] = None
    HwUid: Optional[str] = None
    TypeName: Literal["electric.meter.component.gt"] = "electric.meter.component.gt"
    Version: str = "000"

    _validator_component_id = predicate_validator(
        "ComponentId", property_format.is_uuid_canonical_textual
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["ComponentAttributeClass"] = self.ComponentAttributeClass.as_dict()
        if d["DisplayName"] is None:
            del d["DisplayName"]
        if d["HwUid"] is None:
            del d["HwUid"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class ElectricMeterComponentGt_Maker:
    type_name = "electric.meter.component.gt"
    version = "000"

    def __init__(
        self,
        component_id: str,
        component_attribute_class: ElectricMeterCacGt,
        display_name: Optional[str],
        hw_uid: Optional[str],
    ):
        self.tuple = ElectricMeterComponentGt(
            ComponentId=component_id,
            ComponentAttributeClass=component_attribute_class,
            DisplayName=display_name,
            HwUid=hw_uid,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: ElectricMeterComponentGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> ElectricMeterComponentGt:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> ElectricMeterComponentGt:
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentId")
        if "ComponentAttributeClass" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentAttributeClass")
        if not isinstance(d2["ComponentAttributeClass"], dict):
            raise SchemaError(
                f"d['ComponentAttributeClass'] {d2['ComponentAttributeClass']} must be a ElectricMeterCacGt!"
            )
        component_attribute_class = ElectricMeterCacGt_Maker.dict_to_tuple(
            d2["ComponentAttributeClass"]
        )
        d2["ComponentAttributeClass"] = component_attribute_class
        if "DisplayName" not in d2.keys():
            d2["DisplayName"] = None
        if "HwUid" not in d2.keys():
            d2["HwUid"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return ElectricMeterComponentGt(
            ComponentId=d2["ComponentId"],
            ComponentAttributeClass=d2["ComponentAttributeClass"],
            DisplayName=d2["DisplayName"],
            HwUid=d2["HwUid"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: ElectricMeterComponentGt) -> ElectricMeterComponent:
        if t.ComponentId in ElectricMeterComponent.by_id.keys():
            dc = ElectricMeterComponent.by_id[t.ComponentId]
        else:
            dc = ElectricMeterComponent(
                component_id=t.ComponentId,
                component_attribute_class=t.ComponentAttributeClass,
                display_name=t.DisplayName,
                hw_uid=t.HwUid,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: ElectricMeterComponent) -> ElectricMeterComponentGt:
        t = ElectricMeterComponentGt_Maker(
            component_id=dc.component_id,
            component_attribute_class=dc.component_attribute_class,
            display_name=dc.display_name,
            hw_uid=dc.hw_uid,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> ElectricMeterComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: ElectricMeterComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> ElectricMeterComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
