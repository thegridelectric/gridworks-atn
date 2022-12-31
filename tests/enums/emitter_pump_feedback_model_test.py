"""Tests for schema enum emitter.pump.feedback.model.000"""
from gwatn.enums import EmitterPumpFeedbackModel


def test_emitter_pump_feedback_model() -> None:
    assert set(EmitterPumpFeedbackModel.values()) == {
        "ConstantDeltaT",
        "ConstantGpm",
    }

    assert EmitterPumpFeedbackModel.default() == EmitterPumpFeedbackModel.ConstantDeltaT
