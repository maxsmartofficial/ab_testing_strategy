import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.strategy
import src.page



def run(trials, strategies, pages):

    # {strategy name: {total: ..., page name 1: ..., ...}}
    results = {}

    for s in strategies:
        
        name = s.name
        page_totals = {p.name: 0 for p in pages}
        
        # Set up strategy
        agent = s
        total = 0
    
        # Simulate 'trials' number of people accessing a page
        for t in range(trials):
            # Choose a page to show them
            page = agent.choice()
            # See if the person converts
            result = page.test()
            
            if result:
                total += 1
                page_totals[page.name] += 1
                
            agent.update(page, result)
                
        page_totals['total'] = total
        results[name] = page_totals
        
    return(results)
            
if __name__ == "__main__":
    TRIALS = 20000
    PAGES = src.page.getBernoulliPageList([0.04, 0.06])
    AGENTS = [
            src.strategy.RandomStrategy(PAGES),
            src.strategy.EpsilonGreedyStrategy(PAGES, 0.2)
        ]
    results = run(TRIALS, AGENTS, PAGES)
    print(results)