## Example of problem Definition
  Imagine your company is running marketing campaigns based on emails. Naturally, some customers are more likely to open the emails and some are not. But before running   any campaign, you know nothing about your customers. The only way to learn how likely a customer will open the email is to collect the data by sending them whole   
  bunch of emails and observe the responding rate. The question is, how many emails do we have to send to all customer to establish statistical significance?
  If we send 100 emails to each customer, we probably be able get some idea of who is our optimal targets. But it is very inefficient! As the campaign goes, we want to   
  reach to as much customer as possible as. Meanwhile, we also want to target the customer who has the highest respond rate, those are our optimal customers give the 
  best reward. It is an explore-exploit tradeoff.
  
  
# Visualizations
## 1st Plot - Probability of Selecting the Best Arm over time

X-axis: Number of times the algorithm has been able to pull on any of the five arms that are available. I have set the value to 5000. 

Y-axis: shows the probability line [0,1], when we called select_arm(), chooses the best of the five arms for each value of X.

When epsilon is high the algorithm explores meaning it tries to find the best arm, yet after finding it still explores which is not worth doing anymore since it already have found the best arm.

The lowest value of epsilon, 0.01, causes the algorithm to explore much more slowly, and provides even worse result. Yet for 0.1 value the algorithm reaches a much higher peak performance level.Providing the best Trade-off point.

Similar to AB Testing model this algorithm is also concentrated on time, when a company uses this they need to consider the length of time

## 2nd Plot - The Average Reward at each Time Point

Another visualization I have used is the average reward with time points. Averaging the values gives better result since there could be arms which are a sometimes similar to the best arm sometimes a bit worse and averaging will provide more understandable graphs. 

## 3rd Plot - The Cumulative Reward at each Time Point

To decide whether increased exploration is worth the trouble, we should concentrate on cumulative performance over time, not on performance at each time point.
This can be of use since it make the algorithm to explore at first when no arm is yet explored and this will provide a better performance.
