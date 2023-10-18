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
    def __init__(self, governing_eqn, compartment = 2):
        self.eqn = governing_eqn
        super().__init__(compartment, ic = [0] * compartment, time = 10)

    def sim(self, initial_condition):
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