import pytest
import numpy.testing as npt
from pkmodel.protocol import intravenous, subcutaneous  # Adjust the module name

def test_attribute():
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
