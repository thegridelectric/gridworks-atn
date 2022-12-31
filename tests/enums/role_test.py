"""Tests for schema enum spaceheat.node.role.000"""
from gwatn.enums import Role


def test_role() -> None:
    assert set(Role.values()) == {
        "PrimaryScada",
        "HomeAlone",
        "Heatpump",
        "MultipurposeSensor",
        "CurrentTransformer",
        "RadiatorFan",
        "PipeFlowMeter",
        "BaseboardRadiator",
        "CirculatorPump",
        "DedicatedThermalStore",
        "HeatedSpace",
        "HydronicPipe",
        "PrimaryMeter",
        "Outdoors",
        "BoostElement",
        "BooleanActuator",
        "Atn",
        "TankWaterTempSensor",
        "PipeTempSensor",
        "RoomTempSensor",
        "OutdoorTempSensor",
    }

    assert Role.default() == Role.HeatedSpace
