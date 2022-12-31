"""Tests for schema enum spaceheat.actor.class.000"""
from gwatn.enums import ActorClass


def test_actor_class() -> None:
    assert set(ActorClass.values()) == set(
        [
            "NoActor",
            "PrimaryScada",
            "PrimaryMeter",
            "BooleanActuator",
            "SimpleSensor",
            "HomeAlone",
            "Atn",
            "MultipurposeSensor",
            "Thermostat",
        ]
    )

    assert ActorClass.default() == ActorClass.NoActor
