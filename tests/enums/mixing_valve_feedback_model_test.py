"""Tests for schema enum mixing.valve.feedback.model.000"""
from gwatn.enums import MixingValveFeedbackModel


def test_mixing_valve_feedback_model() -> None:
    assert set(MixingValveFeedbackModel.values()) == set(
        [
            "ConstantSwt",
            "NaiveVariableSwt",
            "CautiousVariableSwt",
        ]
    )

    assert MixingValveFeedbackModel.default() == MixingValveFeedbackModel.ConstantSwt
