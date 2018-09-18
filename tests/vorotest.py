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

if __name__ == '__main__':
    test_dovoro()
