import unittest
from your_module import intravenous, subcutaneous  # Adjust the module name

class TestPharmokineticModels(unittest.TestCase):

    def test_intravenous_steady(self):
        instance = intravenous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, Dose='steady')
        self.assertTrue(callable(instance.eqn))

    def test_intravenous_instantaneous(self):
        instance = intravenous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, Dose='instantaneous')
        self.assertTrue(callable(instance.eqn))
        self.assertEqual(instance.ic, [10, 0])

    def test_subcutaneous_steady(self):
        instance = subcutaneous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, ka=1, Dose='steady')
        self.assertTrue(callable(instance.eqn))
        # Assuming Model initializes some attribute "compartment" that's passed to it
        self.assertEqual(instance.compartment, 3)

    def test_subcutaneous_instantaneous(self):
        instance = subcutaneous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, ka=1, Dose='instantaneous')
        self.assertTrue(callable(instance.eqn))
        # Assuming Model initializes some attribute "compartment" that's passed to it
        self.assertEqual(instance.compartment, 3)
        self.assertEqual(instance.ic, [10, 0, 0])

    def test_incorrect_dose(self):
        with self.assertRaises(ValueError):
            intravenous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, Dose='incorrect_dose')

        with self.assertRaises(ValueError):
            subcutaneous(amount=10, Vc=1, Vp1=1, CL=1, Qp1=1, ka=1, Dose='incorrect_dose')


if __name__ == '__main__':
    unittest.main()
