import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.strategy
import src.page



def run(trials, strategies, pages):

    for s in strategies:
    
        # Set up strategy
        agent = s(pages)
        total = 0
    
        # Simulate 'trials' number of people accessing a page
        for t in range(trials):
            # Choose a page to show them
            page = agent.choice()
            # See if the person converts
            result = page.test()
            
            if result:
                total += 1
        print(s, ':', total)
            
if __name__ == "__main__":
    TRIALS = 20000
    STRATEGIES = [src.strategy.RandomStrategy]
    PAGES = src.page.getBernoulliPageList([0.04, 0.06])
    run(TRIALS, STRATEGIES, PAGES)