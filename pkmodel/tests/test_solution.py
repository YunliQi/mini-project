import pytest
import numpy.testing as npt
from pkmodel.solution import Solution


def test_attributes():
    solution = Solution(2, [1, 2], 1)
    npt.assert_equal(solution.ic, [1, 2])
    npt.assert_equal(solution.result, [[], []])
    npt.assert_equal(solution.time, 1)
    with pytest.raises(ValueError):
        error_expected = Solution(2, [], 1)
    with pytest.raises(ValueError):
        error_expected = Solution(-1, [])
    with pytest.raises(ValueError):
        error_expected = Solution(1, [0], -1)
    with pytest.raises(TypeError):
        error_expected = Solution(1.5, [0])
