import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

import src.strategy
import src.page

# Test a basic strategy

# Check the agent only accepts pages as valid initialisation input
def test_valid():
    with pytest.raises(Exception) as e:
        agent = src.strategy.RandomStrategy([])
        agent = src.strategy.RandomStrategy([1, 2])
        
    pages = src.page.getBernoulliPageList([0.1, 0.2])
    agent = src.strategy.RandomStrategy(pages)

# Check the agent gives one of the pages as output
def test_output():
    pages = src.page.getBernoulliPageList([0.1, 0.2])
    agent = src.strategy.RandomStrategy(pages)
    result = agent.choice()
    assert(result in pages)

# Test best page
def test_best_page():
    pages = src.page.getBernoulliPageList([0.1, 0.2])
    agent = src.strategy.EpsilonGreedyStrategy(pages, 0.1)
    # Create more successes for page 0 than page 1
    for i in range(20):
        agent.update(pages[0], True)
    for i in range(20):
        agent.update(pages[0], False)
    for i in range(10):
        agent.update(pages[1], True)
    for i in range(30):
        agent.update(pages[1], False)      

    bestPage = agent._getBestPage()
    assert(bestPage == pages[0])
    