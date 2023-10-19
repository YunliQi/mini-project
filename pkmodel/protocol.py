#
# Protocol class

from pkmodel.model import Model
from pkmodel.solution import Solution

class intravenous(Model):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, Vc, Vp1, CL, Qp1, amount = 0, Dose = 'steady'):
        if amount < 0:
            raise ValueError("Amount has to be non-negative.")
        def intra(t, y, Dose):
            y[0] = Dose - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
            y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
            return y
        super().__init__(intra, Dose, dose = amount)   
class subcutaneous(Model):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, Vc, Vp1, CL, Qp1, ka, amount = 0, Dose = 'steady'):
        if amount < 0:
            raise ValueError("Amount has to be non-negative.")
        def sub(t, y, Dose):
            y[0] = Dose - ka * y[0]
            y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
            y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
            return y
        super().__init__(sub, Dose, dose = amount, compartment = 3)

