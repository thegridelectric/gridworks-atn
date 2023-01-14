import pytest

import gwatn.config as config
from gwatn.dev_utils import DevValidator


@pytest.mark.skip(reason="Skipped so a package can be published")
def test_dev_validator_constructor():
    DevValidator(config.ValidatorSettings())
