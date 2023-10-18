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
    def __init__(self, compartment, ic, time = [0, 10]):
        self.ic = ic
        self.time = time
        self.result = [[]] * compartment

