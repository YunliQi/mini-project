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
    def __init__(self, amount, Vc, Vp1, CL, Qp1, Dose = 'steady'):
        if Dose == ('steady' or 'Steady'):
            def steady_intra(t, y):
                y[0] = amount - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            super().__init__(steady_intra)
        elif Dose == ('instantaneous' or 'Instantaneous'):
            def ins_intra(t, y):
                y[0] = 0 - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            super().__init__(ins_intra)
            self.ic = [amount, 0]
        else:
            raise ValueError("You need to specify the type of dose correctly")
        
class subcutaneous(Model):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, amount, Vc, Vp1, CL, Qp1, ka, Dose = 'steady'):
        if Dose == ('steady' or 'Steady'):
            def steady_sub(t, y):
                y[0] = amount - ka * y[0]
                y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            super().__init__(steady_sub, compartment = 3)
        elif Dose == ('instantaneous' or 'Instantaneous'):
            def ins_sub(t, y):
                y[0] = 0 - ka * y[0]
                y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            super().__init__(ins_sub, compartment = 3)
            self.ic = [amount, 0, 0]
        else:
            raise ValueError("You need to specify the type of dose correctly")

