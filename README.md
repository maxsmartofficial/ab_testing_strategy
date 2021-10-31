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
This strategy is similar to the epsilon-greedy strategy but with the probability e decreasing over time, as more users are directed. The probability e is given by e = e0 \* r^T where e0 is the initial probability, r is the rate of decrease and T is the number of users encountered so far. This approach requires e0 and r as parameters.

### Thompson Sampling Strategy
Thompson Sampling involves assuming a prior distribution for how each page will perform, then updating these distributions based on observed results so far. We then sample from these posterior distributions, and display the page corresponding to the best performing sample. Given that we can assume each page has an inherent fixed conversion rate, we can model each page's probability of converting as a Beta Distribution Beta(a, b) where the parameters a and b are given by the number of successful and unsuccessful conversions respectively. We then sample from each page's distribution, and display the page with the highest sampled probability.

## Results

The table displays the results of the tests run over 100 simulations for a varying total number of users. The mean conversion rate over these simulations is displayed, with the median in brackets. 

N | 1,000 | 2,000 | 5,000 | 10,000 | 20,000 | 50,000 | 100,000
--|-------|-------|-------|--------|--------|--------|--------
Random | 4.906% (4.95%) | 5.08% (5.05%) | 4.97% (4.96%) | 5.006% (5%) | 5.001% (4.98%) | 5% (5.004%) | 5.007% (5.011%)
Epsilon-first (e = 0.025) | 5.191% (5.4%) | 5.337% (5.6%) | 5.564% (5.85%) | 5.807% (5.925%) | 5.834% (5.955%) | 5.963% (5.948%) | 5972% (5.972%)
Epsilon-first (e = 0.05) | 5.378% (5.5%) | 5.146% (5.65%) | 5.701% (5.91%) | 5.737% (5.92%) | 5.946% (5.975%) | 5.951% (5.96%) | 5.946% (5.955%)
Epsilon-first (e = 0.1) | 5.408% (5.5%) | 5.630% (5.775%) | 5.775% (5.9%) | 5.923% (5.915%) | 5.927% (5.920%) | 5.904% (5.902%) | 5.902% (5.914%)
Epsilon-first (e = 0.2) | 5.476% (5.5%) | 5.622% (5.65%) | 5.714% (5.78%) | 5.746% (5.73%) | 5.755% (5.763%) | 5.808% (5.81%) | 5.792% (5.793%)
Epsilon-first (e = 0.4) | 5.508% (5.6%) | 5.548% (5.55%) | 5.591% (5.56%) | 5.629% (5.63%) | 5.623% (5.622%) | 5.619% (5.622%) | 5.59% (5.594%)
Epsilon-greedy (e = 0.025) | 5.249% (5.4%) | 5.263% (5.6%) | 5.542% (5.75%) | 5.597% (5.82%) | 5.727% (5.9%) | 5.867% (5.908%) | 5.929% (5.956%)
Epsilon-greedy (e = 0.05) | 5.263% (5.3%) | 5.381% (5.575%) | 5.545% (5.75%) | 5.724% (5.805%) | 5.867% (5.952%) | 5.908% (5.917%) | 5.919% (5.917%)
Epsilon-greedy (e = 0.1) | 5.404% (5.4%) | 5.473% (5.65%) | 5.68% (5.8%) | 5.771% (5.77%) | 5.836% (5.86%) | 5.871% (5.889%) | 5.887% (5.887%)
Epsilon-greedy (e = 0.2) | 5.329% (5.4%) | 5.452% (5.55%) | 5.605% (5.66%) | 5.697% (5.71%) | 5.754% (5.76%) | 5.771% (5.78%) | 5.795% (5.795%)
Epsilon-greedy (e = 0.4) | 5.269% (5.2%) | 5.452% (5.475%) | 5.534% (5.54%) | 5.545% (5.55%) | 5.578% (5.565%) | 5.599% (5.616%) | 5.58% (5.575%)
Epsilon-decreasing (e0 = 0.025, r = 0.99) | 5.165% (5.3%) | 5.104% (5.3%) | 5.37% (5.84%) | 5.17% (5.79%) | 5.242% (5.883%) | 5.209% (5.936%) | 5.361% (5.95%)
Epsilon-decreasing (e0 = 0.025, r = 0.997) | 5.453% (5.5%) | 5.223% (5.6%) | 5.363% (5.68%) | 5.249% (5.8%) | 5.245% (5.85%) | 5.346% (5.911%) | 5.45% (5.947%)
Epsilon-decreasing (e0 = 0.025, r = 0.999) | 5.381% (5.4%) | 5.348% (5.75%) | 5.339% (5.66%) | 5.244% (5.765%) | 5.335% (5.85%) | 5.321% (5.948%) | 5.391% (5.949%)
Epsilon-decreasing (e0 = 0.05, r = 0.99) | 5.307% (5.45%) | 5.176% (5.625%) | 5.21% (5.74%) | 5.288% (5.77%) | 5.329% (5.888%) | 5.247% (5.914%) | 5.061% (5.891%)
Epsilon-decreasing (e0 = 0.05, r = 0.997) | 5.345% (5.65%) | 5.194% (5.375%) | 5.403% (5.74%) | 5.348% (5.77%) | 5.401% (5.935%) | 5.272% (5.915%) | 5.379% (5.963%)
Epsilon-decreasing (e0 = 0.05, r = 0.999) | 5.172% (5.25%) | 5.317% (5.65%) | 5.553% (5.82%) | 5.453% (5.89%) | 5.48% (5.897%) | 5.478% (5.922%) | 5.427% (5.971%)
Epsilon-decreasing (e0 = 0.1, r = 0.99) | 5.166% (5.2%) | 5.178% (5.5%) | 5.350% (5.85%) | 5.266% (5.785%) | 5.257% (5.89%) | 5.38% (5.893%) | 5.459% (5.955%)
Epsilon-decreasing (e0 = 0.1, r = 0.997) | 5.465% (5.3%) | 5.434% (5.65%) | 5.443% (5.81%) | 5.574% (5.86%) | 5.435% (5.89%) | 5.556% (5.954%) | 5.327% (5.957%)
Epsilon-decreasing (e0 = 0.1, r = 0.999) | 5.388% (5.45%) | 5.584% (5.825%) | 5.591% (5.84%) | 5.584% (5.82%) | 5.723% (5.935%) | 5.743% (5.974%) | 5.65% (5.972%)
Epsilon-decreasing (e0 = 0.2, r = 0.99) | 5.284% (5.4%) | 5.29% (5.525%) | 5.186% (5.75%) | 5.208% (5.755%) | 5.354% (5.87%) | 5.321% (5.937%) | 5.26% (5.923%)
Epsilon-decreasing (e0 = 0.2, r = 0.997) | 5.375% (5.5%) | 5.459% (5.65%) | 5.597% (5.86%) | 5.622% (5.95%) | 5.535% (5.935%) | 5.552% (5.966%) | 5.562% (5.978%)
Epsilon-decreasing (e0 = 0.2, r = 0.999) | 5.639% (5.8%) | 5.46% (5.6%) | 5.615% (5.84%) | 5.822% (5.905%) | 5.772% (5.925%) | 5.685% (5.921%) | 5.804% (5.991%)
Epsilon-decreasing (e0 = 0.4, r = 0.99) | 5.234% (5.4%) | 5.515% (5.85%) | 5.516% (5.74%) | 5.362% (5.84%) | 5.558% (5.935%) | 5.358% (5.914%) | 5.447% (5.975%)
Epsilon-decreasing (e0 = 0.4, r = 0.997) | 5.475% (5.6%) | 5.43% (5.625%) | 5.548% (5.85%) | 5.74% (5.96%) | 5.605% (5.96%) | 5.618% (5.959%) | 5.636% (5.966%)
Epsilon-decreasing (e0 = 0.4, r = 0.999) | 5.462% (5.5%) | 5.686% (5.7%) | 5.723% (5.85%) | 5.824% (5.915%) | 5.847% (5.935%) | 5.956% (5.984%) | 5.881% (5.974%)
Thompson Sampling | 5.34% (5.3%) | 5.606% (5.675%) | 5.83% (5.78%) | 5.868% (5.875%) | 5.904% (5.895%) | 5.951% (5.962%) | 5.973% (5.97%)

## Summary
The expected number of 'exploratory' samples is approximately e \* N for an epsilon-first strategy and an epsilon-greedy strategy, and e0 / (1 - r) for an epsilon-decreasing strategy, where N is the total number of tests. With this in mind, it seems from the results that we need about 500 tests to reliably acheive significant results. This will depend on the difference between the inherent conversion rates of the two pages.

### Benefits of Epsilon-strategies
* Parameters can be set based on prior assumptions about conversion rates, but this requires knowledge of the relative difference in conversion rates to be effective.
* There is an explicit differentiation between exploration and exploitation of results - you get a single best page at the end.

### Benefits of Thompson Sampling
* No parameters - doesn't require knowledge of actual conversion rates to set total number of tests, but needs a prior distribution.
* The output is a posterior distribution which reflects our confidence in the result.

