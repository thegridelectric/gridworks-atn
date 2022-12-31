"""Tests for schema enum g.node.status.100"""
from gwatn.enums import GNodeStatus


def test_g_node_status() -> None:
    assert set(GNodeStatus.values()) == set(
        [
            "Unknown",
            "Pending",
            "Active",
            "PermanentlyDeactivated",
            "Suspended",
        ]
    )

    assert GNodeStatus.default() == GNodeStatus.Unknown
