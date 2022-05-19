# Epsilon greedy

This is a package python for Marketing Analytics

It includes:

Implementation of the Epsilon-Greedy Algorithm with testing and plotting on Bernoulli distribution.

3 Visualizations:
  1) Probability of Selecting the Best Arm over time
  2) The Average Reward at each Time Point
  3) The Cumulative Reward at each Time Point
 
## Example of problem Definition
  Imagine your company is running marketing campaigns based on emails. Naturally, some customers are more likely to open the emails and some are not. But before running   any campaign, you know nothing about your customers. The only way to learn how likely a customer will open the email is to collect the data by sending them whole   
  bunch of emails and observe the responding rate. The question is, how many emails do we have to send to all customer to establish statistical significance?
  If we send 100 emails to each customer, we probably be able get some idea of who is our optimal targets. But it is very inefficient! As the campaign goes, we want to   
  reach to as much customer as possible as. Meanwhile, we also want to target the customer who has the highest respond rate, those are our optimal customers give the 
  best reward. It is an explore-exploit tradeoff.
  
  
References:
1) https://packaging.python.org/en/latest/tutorials/packaging-projects/
2) https://github.com/audreyfeldroy/cookiecutter-pypackage
3) https://medium.com/coinmonks/target-customers-smartly-5c3f49add85d
4) https://medium.com/analytics-vidhya/multi-armed-bandits-part-1-epsilon-greedy-algorithm-with-python-code-534b9e2abc9
