import pytest
import numpy.testing as npt
import numpy as np
from pkmodel.solution import Solution


class TestSolution(unittest.TestCase):

    def test_solution_initialization(self):
        # Test with specified parameters
        s = Solution(compartment=2, ic=[1, 2], time=5)
        
        self.assertEqual(s.ic, [1, 2])
        self.assertEqual(s.time, 5)
        self.assertEqual(s.result, [[], []])

        # Test with default time parameter
        s_default = Solution(compartment=3, ic=[1, 2, 3])
        
        self.assertEqual(s_default.ic, [1, 2, 3])
        self.assertEqual(s_default.time, 10)
        self.assertEqual(s_default.result, [[], [], []])

    def test_solution_invalid_compartment(self):
        with self.assertRaises(ValueError):
            Solution(compartment=0, ic=[])

        with self.assertRaises(ValueError):
            Solution(compartment=3, ic=[1, 2])

        with self.assertRaises(ValueError):
            Solution(compartment=2, ic=[1, 2, 3])
