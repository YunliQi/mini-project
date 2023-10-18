#
# Protocol class
#
import model

class intravenous(model.Model):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, amount, Vc, Vp1, CL, Qp1, Dose = 'steady'):
        if Dose == 'steady' or 'Steady':
            def steady_intra(t, y):
                y[0] = amount - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            self.eqn = steady_intra
        elif Dose == 'instantaneous' or 'Instantaneous':
            def ins_intra(t, y):
                y[0] = 0 - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[1] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            self.eqn = ins_intra
            self.ic = [amount, 0]
        else:
            raise ValueError("You need to specify the type of dose correctly")
        
class subcutaneous(model.Model):
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, amount, Vc, Vp1, CL, Qp1, ka, Dose = 'steady'):
        if Dose == 'steady' or 'Steady':
            def steady_sub(t, y):
                y[0] = amount - ka * y[0]
                y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            self.eqn = steady_sub
        elif Dose == 'instantaneous' or 'Instantaneous':
            def ins_sub(t, y):
                y[0] = 0 - ka * y[0]
                y[1] = ka * y[0] - y[0] / Vc * CL - Qp1 * (y[0] / Vc - y[1] / Vp1)
                y[2] = Qp1 * (y[0] / Vc - y[1] / Vp1)
                return y
            self.eqn = ins_sub
            self.ic = [amount, 0, 0]
        else:
            raise ValueError("You need to specify the type of dose correctly")

