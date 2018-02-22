#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from systeminfo.skeleton import fib

__author__ = "Alan Treanor"
__copyright__ = "Alan Treanor"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
