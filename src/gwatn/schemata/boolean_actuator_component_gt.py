"""Type boolean.actuator.component.gt, version 000"""
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

from gwatn.data_classes.components.boolean_actuator_component import (
    BooleanActuatorComponent,
)
from gwatn.schemata.boolean_actuator_cac_gt import BooleanActuatorCacGt
from gwatn.schemata.boolean_actuator_cac_gt import BooleanActuatorCacGt_Maker


class BooleanActuatorComponentGt(BaseModel):
    ComponentId: str  #
    ComponentAttributeClass: BooleanActuatorCacGt  #
    DisplayName: Optional[str] = None
    Gpio: Optional[int] = None
    HwUid: Optional[str] = None
    TypeName: Literal["boolean.actuator.component.gt"] = "boolean.actuator.component.gt"
    Version: str = "000"

    _validator_component_id = predicate_validator(
        "ComponentId", property_format.is_uuid_canonical_textual
    )

    def as_dict(self) -> Dict[str, Any]:
        d = self.dict()
        d["ComponentAttributeClass"] = self.ComponentAttributeClass.as_dict()
        if d["DisplayName"] is None:
            del d["DisplayName"]
        if d["Gpio"] is None:
            del d["Gpio"]
        if d["HwUid"] is None:
            del d["HwUid"]
        return d

    def as_type(self) -> str:
        return json.dumps(self.as_dict())


class BooleanActuatorComponentGt_Maker:
    type_name = "boolean.actuator.component.gt"
    version = "000"

    def __init__(
        self,
        component_id: str,
        component_attribute_class: BooleanActuatorCacGt,
        display_name: Optional[str],
        gpio: Optional[int],
        hw_uid: Optional[str],
    ):
        self.tuple = BooleanActuatorComponentGt(
            ComponentId=component_id,
            ComponentAttributeClass=component_attribute_class,
            DisplayName=display_name,
            Gpio=gpio,
            HwUid=hw_uid,
            #
        )

    @classmethod
    def tuple_to_type(cls, tuple: BooleanActuatorComponentGt) -> str:
        return tuple.as_type()

    @classmethod
    def type_to_tuple(cls, t: str) -> BooleanActuatorComponentGt:
        try:
            d = json.loads(t)
        except TypeError:
            raise SchemaError("Type must be string or bytes!")
        if not isinstance(d, dict):
            raise SchemaError(f"Deserializing {t} must result in dict!")
        return cls.dict_to_tuple(d)

    @classmethod
    def dict_to_tuple(cls, d: dict[str, Any]) -> BooleanActuatorComponentGt:
        d2 = dict(d)
        if "ComponentId" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentId")
        if "ComponentAttributeClass" not in d2.keys():
            raise SchemaError(f"dict {d2} missing ComponentAttributeClass")
        if not isinstance(d2["ComponentAttributeClass"], dict):
            raise SchemaError(
                f"d['ComponentAttributeClass'] {d2['ComponentAttributeClass']} must be a BooleanActuatorCacGt!"
            )
        component_attribute_class = BooleanActuatorCacGt_Maker.dict_to_tuple(
            d2["ComponentAttributeClass"]
        )
        d2["ComponentAttributeClass"] = component_attribute_class
        if "DisplayName" not in d2.keys():
            d2["DisplayName"] = None
        if "Gpio" not in d2.keys():
            d2["Gpio"] = None
        if "HwUid" not in d2.keys():
            d2["HwUid"] = None
        if "TypeName" not in d2.keys():
            raise SchemaError(f"dict {d2} missing TypeName")

        return BooleanActuatorComponentGt(
            ComponentId=d2["ComponentId"],
            ComponentAttributeClass=d2["ComponentAttributeClass"],
            DisplayName=d2["DisplayName"],
            Gpio=d2["Gpio"],
            HwUid=d2["HwUid"],
            TypeName=d2["TypeName"],
            Version="000",
        )

    @classmethod
    def tuple_to_dc(cls, t: BooleanActuatorComponentGt) -> BooleanActuatorComponent:
        if t.ComponentId in BooleanActuatorComponent.by_id.keys():
            dc = BooleanActuatorComponent.by_id[t.ComponentId]
        else:
            dc = BooleanActuatorComponent(
                component_id=t.ComponentId,
                component_attribute_class=t.ComponentAttributeClass,
                display_name=t.DisplayName,
                gpio=t.Gpio,
                hw_uid=t.HwUid,
            )

        return dc

    @classmethod
    def dc_to_tuple(cls, dc: BooleanActuatorComponent) -> BooleanActuatorComponentGt:
        t = BooleanActuatorComponentGt_Maker(
            component_id=dc.component_id,
            component_attribute_class=dc.component_attribute_class,
            display_name=dc.display_name,
            gpio=dc.gpio,
            hw_uid=dc.hw_uid,
        ).tuple
        return t

    @classmethod
    def type_to_dc(cls, t: str) -> BooleanActuatorComponent:
        return cls.tuple_to_dc(cls.type_to_tuple(t))

    @classmethod
    def dc_to_type(cls, dc: BooleanActuatorComponent) -> str:
        return cls.dc_to_tuple(dc).as_type()

    @classmethod
    def dict_to_dc(cls, d: dict[Any, str]) -> BooleanActuatorComponent:
        return cls.tuple_to_dc(cls.dict_to_tuple(d))
