"""Tests for schema enum message.category.000"""
from gwatn.enums import MessageCategory


def test_message_category() -> None:
    assert set(MessageCategory.values()) == set(
        [
            "Unknown",
            "RabbitJsonDirect",
            "RabbitJsonBroadcast",
            "RabbitGwSerial",
            "MqttJsonBroadcast",
            "RestApiPost",
            "RestApiPostResponse",
            "RestApiGet",
        ]
    )

    assert MessageCategory.default() == MessageCategory.Unknown
