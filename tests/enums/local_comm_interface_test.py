"""Tests for schema enum local.comm.interface.000"""
from gwatn.enums import LocalCommInterface


def test_local_comm_interface() -> None:
    assert set(LocalCommInterface.values()) == {
        "ANALOG_4_20_MA",
        "RS232",
        "I2C",
        "WIFI",
        "SIMRABBIT",
        "UNKNOWN",
        "ETHERNET",
        "ONEWIRE",
        "RS485",
    }

    assert LocalCommInterface.default() == LocalCommInterface.UNKNOWN
