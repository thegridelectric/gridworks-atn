"""Tests for schema enum spaceheat.telemetry.name.000"""
from gwatn.enums import TelemetryName


def test_telemetry_name() -> None:
    assert set(TelemetryName.values()) == {
        "Unknown",
        "PowerW",
        "PhaseAngleDegreesTimes10",
        "WattHours",
        "RelayState",
        "WaterTempCTimes1000",
        "WaterTempFTimes1000",
        "WaterFlowGpmTimes100",
        "CurrentRmsMicroAmps",
        "GallonsPerMinuteTimes10",
        "CurrentRmsMilliAmps",
        "VoltageRmsMilliVolts",
    }

    assert TelemetryName.default() == TelemetryName.Unknown
