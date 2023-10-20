#
# Protocol class

from pkmodel.model import Model

class intravenous(Model):
    """A Pharmokinetic (PK) protocol for intravenous dosing

    Parameters
    ----------

    Vc: numeric
        Volume of central compartment.

    Vp1: numeric
        Volume of peripheral compartment 1.

    CL: numeric
        Clearance rate.

    Qp1: numeric
        Rate of transfer from central to peripheral compartment 1.

    amount: numeric, optional
        The dose amount, under "steady", it will be the rate of steady dosing, under "instantaneous", it will be the amount injected at the beginning (default is 0, but recommend to specify under "instantaneous" dosing).

    Dose: str, optional
        The type of dose protocol, either 'steady' or 'instantaneous' (default is 'steady').

    """
    def __init__(self, Vc, Vp1, CL, Qp1, amount = 0, Dose = 'steady'):
        if amount < 0:
            raise ValueError("Amount has to be non-negative.")
        def intra(t, y, Dose):
            y[0] = Dose - y[0]/Vc * CL - Qp1 * (y[0]/Vc - y[1]/Vp1)
            y[1] = Qp1 * (y[0]/Vc - y[1]/Vp1)
            return y
        super().__init__(intra, Dose, dose = amount)   
class subcutaneous(Model):
    """A Pharmokinetic (PK) protocol for subcutaneous administration

    Parameters
    ----------

    Vc: numeric
        Volume of central compartment.

    Vp1: numeric
        Volume of peripheral compartment 1.

    CL: numeric
        Clearance rate.

    Qp1: numeric
        Rate of transfer from central to peripheral compartment 1.

    ka: numeric
        Absorption rate constant.

    amount: numeric, optional
        The dose amount, under "steady", it will be the rate of steady dosing, under "instantaneous", it will be the amount injected at the beginning (default is 0, but recommend to specify under "instantaneous" dosing).

    Dose: str, optional
        The type of dose protocol, either 'steady' or 'instantaneous' (default is 'steady').

    """
    def __init__(self, Vc, Vp1, CL, Qp1, ka, amount = 0, Dose = 'steady'):
        if amount < 0:
            raise ValueError("Amount has to be non-negative.")
        def sub(t, y, Dose):
            y[0] = Dose - ka * y[0]
            y[1] = ka * y[0] - y[0]/Vc * CL - Qp1 * (y[0]/Vc - y[1]/Vp1)
            y[2] = Qp1 * (y[0]/Vc - y[1]/Vp1)
            return y
        super().__init__(sub, Dose, dose = amount, compartment = 3)

