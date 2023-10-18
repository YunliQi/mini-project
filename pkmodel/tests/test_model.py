import unittest
import pkmodel as pk
import pytest
import scipy
import numpy.testing as npt
import numpy as np
import matplotlib.pyplot as plt

def exponential_decay(t, y): return -0.5 * y

from pkmodel import sim
sim_object= sim(exponential_decay, 0.1, 10, 0)
class test_sim(sim_object):
    sim_object.result = scipy.integrate.solve_ivp(sim_object.eqn, [0, sim_object.time], sim_object.ic, max_step = 0.01)
    npt.assert_almost_equal(sim_object.result.y[5], 0.1 * np.exp(-0.5 * sim_object.result.t)[5], decimal=2)


from pkmodel import solution 

class test_plot(sim_object):
    """
    Tests the :class:`Model` class.
    """
    from pkmodel.model import plot
    plt.plot(np.array(sim_object.result.t), np.array(sim_object.result.y))
    plt.show()



