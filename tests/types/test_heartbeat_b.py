"""Tests heartbeat.b type, version 001"""
import json

import pytest
from gridworks.errors import SchemaError
from pydantic import ValidationError

from gwatn.types import HeartbeatB_Maker as Maker


def test_heartbeat_b_generated() -> None:
    ...