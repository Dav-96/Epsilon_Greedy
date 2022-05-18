# Epsilon_Greedy Algorithm

#### This package as an Alpha version of Epsilon-Greedy algorithm implemented for a university course.

### One example of a similar problem is described below:

Imagine your company is running marketing campaigns based on emails. Some customers are more likely to open the emails and some are not. But before running anything, you know nothing about your customers. The only way to learn is to collect the data by sending them whole bunch of emails and observe the responding rate.

The question is: "How many emails do we have to send to all customer to establish statistical significance?" Meanwhile, we also want to target the customer who has the highest respond rate, and they give the best reward. It is an explore-exploit tradeoff. The exploration, exploitation trade-off is a dilemma we frequently face in choosing between options. Should you choose what you know and get something close to what you expect (‘exploit’) or choose something you aren’t sure about and possibly learn more (‘explore’)? The challenge can exist in many different contexts. Such as marketing campaign, website A/B testing or your gambling strategies. The core of the challenge is essentially the same.

To solve the exploit and explore problem, epsilon greedy algorithm assigns a probability that we randomly explore more customers. In the rest of the time, we exploit the customer with the highest probability based on we’ve known so far.

References:

1) https://medium.com/coinmonks/target-customers-smartly-5c3f49add85d
2) https://medium.com/analytics-vidhya/multi-armed-bandits-part-1-epsilon-greedy-algorithm-with-python-code-534b9e2abc9
3) https://packaging.python.org/en/latest/tutorials/packaging-projects/
