#
# Model class
#

from pkmodel.solution import Solution
import numpy as np
import scipy
import matplotlib.pyplot as plt

class Model(Solution):
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, governing_eqn, dose_proto, dose = 0, compartment = 2):
        if dose_proto == ("steady" or "Steady"):
            def eqn(t, y):
                return governing_eqn(t, y, dose)
            self.eqn = eqn
            super().__init__(compartment, ic = [0] * compartment, time = 10)
        elif dose_proto == ("instantaneous" or "Instantaneous"):
            def eqn(t,y):
                return governing_eqn(t, y, 0)
            self.eqn = eqn
            super().__init__(compartment, ic = [dose] + [0] * (compartment - 1), time = 10)
        else:
            raise ValueError("You need to specify the type of dose protocol correctly")

    def sim(self):
        self.result = scipy.integrate.solve_ivp(self.eqn, [0, self.time], self.ic, max_step = 0.01)

    def plot(self, legend = None):
        plt.plot(np.array(self.result.t), np.array(self.result.y).T)
        plt.xlabel("t")
        plt.ylabel("Consentration")
        if len(self.ic) == 2:
            plt.legend(["c", "p1"], shadow = True)
        elif len(self.ic) == 3:
            plt.legend(["p0", "c", "p1"], shadow = True)
        else:
            plt.legend(legend, shadow = True)
        plt.title("PK Model Simulation")
        plt.show()

    def compare(self, another_model, legend_current = None, legend_out = None):
        figure, axis = plt.subplots(1, 2)
        figure.tight_layout(pad = 4, h_pad = 4)

        axis[0].plot(np.array(self.result.t), np.array(self.result.y).T) 
        axis[0].set_title("Current Model")
        axis[0].set_xlabel("t")
        axis[0].set_ylabel("Consentration")
        if len(self.ic) == 2:
            axis[0].legend(["c", "p1"], shadow = True)
        elif len(self.ic) == 3:
            axis[0].legend(["p0", "c", "p1"], shadow = True)
        else:
            axis[0].legend(legend_current, shadow = True)

        axis[1].plot(np.array(another_model.result.t), np.array(another_model.result.y).T) 
        axis[1].set_title("The Other Model")
        axis[1].set_xlabel("t")
        if len(another_model.ic) == 2:
            axis[1].legend(["c", "p1"], shadow = True)
        elif len(another_model.ic) == 3:
            axis[1].legend(["p0", "c", "p1"], shadow = True)
        else:
            axis[1].legend(legend_out, shadow = True)

        plt.show()