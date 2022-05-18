from packages import *

"""
Use Monte Carlo simulations to test bandit algorithms.
Link: https://www.investopedia.com/terms/m/montecarlosimulation.asp
"""
class BernoulliArm:
    """
    Draw an arm's reward from a Bernoulli distribution.
    Parameters
    ----------
    p : float
            probability of getting reward for a specific arm.

    Attributes
    ----------
    draw : float
        rewards drawn using Bernoulli probability distribution.
    """
    def __init__(self, p):
        self.p = p

    def draw(self):
        z = np.random.random()
        if z > self.p:
            return 0.0
        return 1.0
        # An arm rewards you with a value of 1 some percentage of the time and rewards you with a value of 0 the rest of the time.