"""
THESE TESTS VERIFY THE FRAMEWORK IS SETUP CORRECTLY AND ARE EXECUTED BEFORE ALL OTHER TESTS
Author: Chinmay Mudholkar
Date: 04/2024
"""

import pytest
from libs import config_ops
import sys


class Test_Get:
    config = config_ops.config_operations()

    @pytest.mark.order(1)
    @pytest.mark.setup
    def test_setup_001(self):
        expected = 3.10
        actual = float(".".join(sys.version.split(sep=" ")[0].split(sep=".")[:2]))
        assert actual >= expected, "Invalid Python version"

    @pytest.mark.order(2)
    @pytest.mark.setup
    def test_setup_002(self):
        expected = "PYAPIBASICS"
        actual = self.config.get_project_name()
        assert expected == actual, "Could not find the config file."
