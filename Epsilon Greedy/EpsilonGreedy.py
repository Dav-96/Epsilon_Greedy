from packages import *

# Epsilon Greedy
"""
Implementing epsilon-Greedy algorithm in both standard and annealing forms.
"""
class EpsilonGreedy:
    """Implementing standard epsilon-Greedy algorithm.

    Parameters
    ----------
    Epsilon tells us the frequency with which we should explore one of the available arms. If epsilon = 0.01, then we will explore the available arms on 1% of our pulls.

    Counts describe how many times we have played each of the N arms in the current bandit problem.

    Values defines the average amount of reward when playing each of the N arms available to us.
    """
    def __init__(self, epsilon, number=None, values=None):
        self.epsilon = epsilon
        self.number = number
        self.values = values

    def initialize(self, n_arms):
        """Initialize number and values array with zeros."""
        self.number = np.zeros(n_arms, dtype=int)
        self.values = np.zeros(n_arms, dtype=float)

    def select_arm(self):
        z = np.random.random()
        if z > self.epsilon:
            # Pick the best arm. argmax returns the index of the maximum value
            return np.argmax(self.values)
        # Randomly pick any arm with prob 1 / len(self.number)
        return np.random.randint(0, len(self.values))

    def update(self, chosen_arm, reward):
        """Update number and estimated value of rewards for the chosen arm."""
        # Increment chosen arm's count by one
        self.number[chosen_arm] += 1
        n = self.number[chosen_arm]

        # Recompute the estimated value of chosen arm using new reward
        value = self.values[chosen_arm]
        new_value = value * ((n - 1) / n) + reward / n
        self.values[chosen_arm] = new_value

    def __ne__(self) -> str:
        return "eps = 0.3"