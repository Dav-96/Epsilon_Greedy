from packages import *
from EpsilonGreedy import EpsilonGreedy
from BernoulliArm import BernoulliArm

def test_algorithm(algorithm, arms, num_simulations, horizon):
    chosen_arms = np.zeros((num_simulations, horizon))
    rewards = np.zeros((num_simulations, horizon))
    for sim in range(num_simulations):
        algorithm.initialize(len(arms))
        for t in range(horizon):
            chosen_arm = algorithm.select_arm()
            chosen_arms[sim, t] = chosen_arm
            reward = arms[chosen_arm].draw()
            rewards[sim, t] = reward
            algorithm.update(chosen_arm, reward)
    average_rewards = np.mean(rewards, axis=0)
    cumulative_rewards = np.cumsum(average_rewards)
    return chosen_arms, average_rewards, cumulative_rewards


"""
Plots Bandit Algorithms performance.
"""
ALGORITHMS = {
    "epsilon-Greedy": EpsilonGreedy
}

def plot_algorithm(
        algorithm_name="epsilon-Greedy", arms=None, best_arm_index=None,
        hyper_parameters=None, num_simulations=1000, horizon=100, label=None,
        fig_size=(18, 6)):
    # Check if the algorithm doesn't have hyperparameter
    if hyper_parameters is None:
        # Run the algorithm
        algorithm = ALGORITHMS[algorithm_name]()
        chosen_arms, average_rewards, cumulative_rewards = test_algorithm(
            algorithm, arms, num_simulations, horizon)
        probabilities_average = np.where(chosen_arms == best_arm_index, 1, 0).sum(
            axis=0) / num_simulations

        # Plot the 3 metrics of the algorithm
        fig, axes = plt.subplots(1, 3, figsize=fig_size)
        axes[0].plot(probabilities_average)
        axes[0].set_xlabel("Time", fontsize=14)
        axes[0].set_ylabel("Probability of Selecting Best Arm", fontsize=14)
        axes[0].set_title(
            f"Accuray of {algorithm_name} alg.", y=1.05, fontsize=16)
        axes[0].set_ylim([0, 1.05])
        axes[1].plot(average_rewards)
        axes[1].set_xlabel("Time", fontsize=14)
        axes[1].set_ylabel("Average Reward", fontsize=14)
        axes[1].set_title(
            f"Avg. Rewards of {algorithm_name} alg.", y=1.05, fontsize=16)
        axes[1].set_ylim([0, 1.0])
        axes[2].plot(cumulative_rewards)
        axes[2].set_xlabel("Time", fontsize=14)
        axes[2].set_ylabel("Cumulative Rewards of Chosen Arm", fontsize=14)
        axes[2].set_title(
            f"Cumulative Rewards of {algorithm_name} alg.", y=1.05, fontsize=16)
        plt.tight_layout()

    else:
        fig, axes = plt.subplots(1, 3, figsize=fig_size)
        for hyper_parameter in hyper_parameters:
            # Run the algorithm
            algorithm = ALGORITHMS[algorithm_name](hyper_parameter)
            chosen_arms, average_rewards, cumulative_rewards = test_algorithm(
                algorithm, arms, num_simulations, horizon)
            probabilities_average = np.where(chosen_arms == best_arm_index, 1, 0).sum(
                axis=0) / num_simulations

            # Plot the 3 metrics of the algorithm
            axes[0].plot(probabilities_average, label=f"{label} = {hyper_parameter}")
            axes[0].set_xlabel("Time", fontsize=14)
            axes[0].set_ylabel(
                "Probability of Selecting Best Arm", fontsize=14)
            axes[0].set_title(
                f"Accuray of {algorithm_name} alg.", y=1.05, fontsize=16)
            axes[0].legend()
            axes[0].set_ylim([0, 1.05])
            axes[1].plot(average_rewards, label=f"{label} = {hyper_parameter}")
            axes[1].set_xlabel("Time", fontsize=14)
            axes[1].set_ylabel("Average Reward", fontsize=14)
            axes[1].set_title(
                f"Avg. Rewards of {algorithm_name} alg.", y=1.05, fontsize=16)
            axes[1].legend()
            axes[1].set_ylim([0, 1.0])
            axes[2].plot(cumulative_rewards, label=f"{label} = {hyper_parameter}")
            axes[2].set_xlabel("Time", fontsize=14)
            axes[2].set_ylabel("Cumulative Rewards of Chosen Arm", fontsize=14)
            axes[2].set_title(
                f"Cumulative Rewards of {algorithm_name} alg.", y=1.05, fontsize=16)
            axes[2].legend(loc="lower right")
            plt.tight_layout()

        axes[0].plot(probabilities_average, label=algorithm.__ne__())
        axes[0].set_xlabel("Time", fontsize=12)
        axes[0].set_ylabel("Probability of Selecting Best Arm", fontsize=12)
        axes[0].set_title(
            f"Accuray of Different Algorithms", y=1.05, fontsize=14)
        axes[0].set_ylim([0, 1.05])
        axes[0].legend(loc="lower right")
        axes[1].plot(average_rewards, label=algorithm.__ne__())
        axes[1].set_xlabel("Time", fontsize=12)
        axes[1].set_ylabel("Average Reward", fontsize=12)
        axes[1].set_title(
            f"Average Rewards of Different Algorithms", y=1.05, fontsize=14)
        axes[1].set_ylim([0, 1.0])
        axes[1].legend(loc="lower right")
        axes[2].plot(cumulative_rewards, label=algorithm.__ne__())
        axes[2].set_xlabel("Time", fontsize=12)
        axes[2].set_ylabel("Cumulative Rewards of Chosen Arm", fontsize=12)
        axes[2].set_title(
            f"Cumulative Rewards of Different Algorithms", y=1.05, fontsize=14)
        axes[2].legend(loc="lower right")
        plt.tight_layout()
        plt.show()


np.random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
n_arms = len(means)
np.random.shuffle(means)
arms = list(map(lambda mu: BernoulliArm(mu), means))
print("Best arm is " + str(means.index(max(means))))

best_arm_index = np.argmax(means) # Getting best arm index
epsilon = [0.01, 0.1, 0.2, 0.5] # Checking for different epsilon values

# Plot the epsilon-Greedy algorithm
plot_algorithm(algorithm_name="epsilon-Greedy", arms=arms, best_arm_index=best_arm_index,
                   hyper_parameters=epsilon, num_simulations=500, horizon=500, label="eps")
