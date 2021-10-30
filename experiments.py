import src.main
import src.page
import src.strategy

import numpy
from collections import defaultdict
import time


def test(total, pages, tests=10):
    results = defaultdict(list)
    
    for t in range(tests):
        strategies = []
        
        random_strategy = src.strategy.RandomStrategy(pages)
        strategies.append(random_strategy)

        for i in [total * 0.025, total * 0.05, total * 0.1, total * 0.2, total * 0.4]:
            epsilon_first_strategy = src.strategy.EpsilonFirstStrategy(pages, i)
            strategies.append(epsilon_first_strategy)
        
        for e in [0.025, 0.05, 0.1, 0.2, 0.4]:
            epsilon_greedy_strategy = src.strategy.EpsilonGreedyStrategy(pages, e)
            strategies.append(epsilon_greedy_strategy)
        
        for e in [0.025, 0.05, 0.1, 0.2, 0.4]:
            for r in [0.99, 0.997, 0.999]:
                epsilon_decreasing_strategy = \
                    src.strategy.EpsilonDecreasingStrategy(pages, e, r)
                strategies.append(epsilon_decreasing_strategy)
            
        thompson_sampling_strategy = src.strategy.ThompsonSamplingStrategy(pages)
        strategies.append(thompson_sampling_strategy)

        
        result =  src.main.run(total, strategies, pages)
        
        
        for k in result:
            results[k].append(result[k]['total'])
            
    return(results)
    

pages = src.page.getBernoulliPageList([0.04, 0.06])

for TOTAL in [2000, 5000, 20000, 50000, 100000]:
    start = time.time()
    results = test(TOTAL, pages, tests=100)
    end = time.time()
    print('Test finished in ' + str(end - start) + ' seconds.')
    for r in results:
        median = "{:0.3f}".format(100 * numpy.median(results[r])/TOTAL) + '%'
        mean = "{:0.3f}".format(100 * numpy.mean(results[r])/TOTAL) + '%'
        print(r + ' -  median: ' + median + ', mean: ' + mean)