import pytest
import numpy.testing as npt
import numpy as np

from pkmodel.model import Model

def exponential_decay(t, y, Dose): 
    return Dose - 0.5 * y

def test_sim_instantaneous():
    sim_object = Model(exponential_decay, 'instantaneous', dose = 0.1, compartment = 1)
    sim_object.sim()
    npt.assert_almost_equal(sim_object.result.y[0], 0.1 * np.exp(-0.5 * sim_object.result.t), decimal=2)

def test_sim_steady():
    sim_object = Model(exponential_decay, 'steady', dose = 0.1, compartment = 1)
    sim_object.sim()
    npt.assert_almost_equal(sim_object.result.y[0], 0.2 * (1 - np.exp(-0.5 * sim_object.result.t)), decimal=2)

def test_sim_error():
    with pytest.raises(ValueError):
        error_expected = Model(exponential_decay, 'abc', compartment = 1)

def test_attributes():
    sim_object = Model(exponential_decay, 'instantaneous', dose = 0.1, compartment = 3)
    npt.assert_equal(sim_object.ic, [0.1, 0, 0])
    npt.assert_equal(sim_object.result, [[], [], []])
    npt.assert_equal(sim_object.time, 10)
    sim_object = Model(exponential_decay, 'steady', dose = 0.1, compartment = 3)
    npt.assert_equal(sim_object.ic, [0, 0, 0])
    npt.assert_equal(sim_object.result, [[], [], []])
    npt.assert_equal(sim_object.time, 10)

def test_plot_error():
    with pytest.raises(AssertionError):
        error_expected = Model(exponential_decay, 'steady', dose = 0.1, compartment = 1).plot()