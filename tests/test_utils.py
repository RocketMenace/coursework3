"""
Module for testing utils module.
"""

import utils


def test_get_operations():
    file = utils.get_operations()
    assert isinstance(file, list)