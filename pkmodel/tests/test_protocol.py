import pytest
import numpy.testing as npt
from pkmodel.protocol import intravenous, subcutaneous  # Adjust the module name

def intra(t, y, Dose):
    y[0] = Dose - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
    y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
    return y

def sub(t, y, Dose):
    y[0] = Dose - ka * y[0]
    y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
    y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
    return y

def test_int_attribute():
    test = intravenous(1, 1, 1, 1, amount = 1, Dose = 'steady')
    npt.assert_equal(test.ic, [0, 0])
    test = intravenous(1, 1, 1, 1, amount = 1, Dose = 'instantaneous')
    npt.assert_equal(test.ic, [1, 0])
    test = subcutaneous(1, 1, 1, 1, 1, amount = 1, Dose = 'steady')
    npt.assert_equal(test.ic, [0, 0, 0])
    test = subcutaneous(1, 1, 1, 1, 1, amount = 1, Dose = 'instantaneous')
    npt.assert_equal(test.ic, [1, 0, 0])
    with pytest.raises(ValueError):
        test = intravenous(1, 1, 1, 1, amount = -1, Dose = 'steady')
    with pytest.raises(ValueError):
        test = subcutaneous(1, 1, 1, 1, 1, amount = -1, Dose = 'steady')

