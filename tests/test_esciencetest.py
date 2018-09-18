#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the esciencetest module.
"""
import pytest

from esciencetest import esciencetest


def test_without_test_object():
    assert False


class TestEsciencetest(object):
    @pytest.fixture
    def return_a_test_object(self):
        pass

    def test_esciencetest(self, esciencetest):
        assert False

    def test_with_error(self, esciencetest):
        with pytest.raises(ValueError):
            pass
