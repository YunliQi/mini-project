#
# Solution class
#

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    value: numeric, optional
        an example paramter

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

