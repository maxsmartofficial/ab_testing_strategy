import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

import src.strategy
import src.page
import src.main


# Test data is correct format

def test_data():
    trials = 1000
    pages = src.page.getBernoulliPageList([0.1, 0.2])
    agent = src.strategy.RandomStrategy(pages)
    agents = [agent]
    results = src.main.run(trials, agents, pages)
    # Assert there is only one result
    assert(len(results)==1)
    # Assert the result has the agent's name
    assert(agent.name in results)