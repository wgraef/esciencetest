#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the esciencetest module.
"""
import pytest

from esciencetest import esciencetest
import numpy


def test_dovoro():
    dim_x = 2.1
    dim_y = 3.2
    cells = 20
    (cellcount, volume) = esciencetest.dovoro(dim_x, dim_y, cells)
    print('got ', cellcount, ' cells with a total volume of ', volume)
    assert numpy.isclose(volume, dim_x*dim_y, rtol=1e-05, atol=1e-08, equal_nan=False)
    assert cellcount == cells

#def test_without_test_object():
#    assert False
#
#
#class TestEsciencetest(object):
#    @pytest.fixture
#    def return_a_test_object(self):
#        pass
#
#    def test_esciencetest(self, esciencetest):
#        assert False
#
#    def test_with_error(self, esciencetest):
#        with pytest.raises(ValueError):
#            pass
