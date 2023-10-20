#
# Solution class
#

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------
    compartment: int
        The number of compartments in the PK model.
    ic: list
        Initial conditions for each compartment.
    time: numeric, optional
        The duration of the simulation (default is 10).

    Attributes
    ----------
    ic: list
        List of initial conditions for each compartment.
    time: numeric
        Duration of the simulation.
    result: list
        List to store simulation results for each compartment.

    Raises
    ------
    ValueError
        - If `compartment` is less than or equal to 0.
        - If the length of `ic` does not match the specified `compartment`.
        - If `time` is negative.

    """
    def __init__(self, compartment: int, ic, time = 10):
        self.ic = ic
        self.time = time
        self.result = [[]] * compartment
        if compartment <= 0:
            raise ValueError("You need to have at least one compartment.")
        if len(self.ic) != compartment:
            raise ValueError("You need to provide an appropriate number of initial conditions.")
        if time < 0:
            raise ValueError("Time need to be non-negative.")

