#
# Model class
#

import scipy
import matplotlib.pyplot as plt
import numpy as np

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, compartment, ic, time = 10):
        self.ic = ic
        self.time = time
        self.result = [[]] * compartment

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
        self.result = scipy.integrate.solv_ivp(self.eqn, [0, self.time], self.ic, max_step = 0.01)

    def plot(self):
        plt.plot(np.array(self.result.t), np.array(self.result.y))
        plt.show()