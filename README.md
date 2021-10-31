# A/B Testing Strategy

A/B testing is an effective way of optimising conversion rates, but it is important to consider the cost of the test itself - how many customers is conducting the test costing you? There are a variety of different methods that can replace standard A/B testing, with differing costs and tradeoffs.

This project simulates a series of users being shown two different web pages, each with an inherent conversion rate (4% and 6%). The goal is to optimise the overall conversion rate, which is the percentage of the total number of users that convert. Several strategies are tested:

### Random Strategy
A baseline strategy that involves displaying a page at random. We'd expect this to give a total conversion rate equal to the average of each page's conversion rate (in this case 5%).

### Epsilon-first Strategy (Standard A/B testing)
The first n users are directed to a randomly chosen page. After the first n users, the best performing page is always displayed to the remaining users. This requires the number of initial users e as a parameter where n is the product of e and the total number of users (e.g. for 10,000 users, if e=0.2, n=2,000).

### Epsilon-greedy Strategy
Each user is directed to a random page with probability e. Otherwise, they are directed to the best performing page so far. If there is no best performing page yet, they are again directed to a random page. This requires the probability e as a parameter.

### Epsilon-decreasing Strategy
This strategy is similar to the epsilon-greedy strategy but with the probability e decreasing over time, as more users are directed. The probability e is given by e = e0 x r^T where e0 is the initial probability, r is the rate of decrease and T is the number of users encountered so far. This approach requires e0 and r as parameters.

### Thompson Sampling Strategy
Thompson Sampling involves assuming a prior distribution for how each page will perform, then updating these distributions based on observed results so far. We then sample from these posterior distributions, and display the page corresponding to the best performing sample. Given that we can assume each page has an inherent fixed conversion rate, we can model each page's probability of converting as a Beta Distribution Beta(a, b) where the parameters a and b are given by the number of successful and unsuccessful conversions respectively. We then sample from each page's distribution, and display the page with the highest sampled probability.

## Results

The table displays the results of the tests run over 100 simulations for a varying total number of users. The mean conversion rate over these simulations is displayed, with the median in brackets. 

N | 1,000 | 2,000 | 5,000 | 10,000 | 20,000 | 50,000 | 100,000
--|-------|-------|-------|--------|--------|--------|--------
Random | 4.906% (4.95%) | 5.08% (5.05%) | 4.97% (4.96%) | 5.006% (5%) | 5.001% (4.98%) | 5% (5.004%) | 5.007% (5.011%)
Epsilon-first (e = 0.025) | 5.191% (5.4%) | 5.337% (5.6%) | %.564% (5.85%) | 5.807% (5.925%) | 5.834% (5.955%) | 5.963% (5.948%) | 5972% (5.972%)