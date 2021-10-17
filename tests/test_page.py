import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

import src.page

# Test basic x% success page

# Check it returns True or False
def test_bernoulli_page():
    page = src.page.BernoulliPage(0.5)
    for i in range(100):
        test = page.test()
        assert(type(test) == bool)
            

# Check it only accepts a valid probability
def test_bernoulli_page_valid():
    with pytest.raises(Exception) as e:
        page = src.page.BernoulliPage(1.5)
        page = src.page.BernoulliPage(-3)
        page = src.page.BernoulliPage('Seems pretty likely')


# Check page list creator

# Check it returns a list of Pages with correct length
def test_bernoulli_list():
    lst = [0.4, 0.5, 0.6]
    pages = src.page.getBernoulliPageList(lst)
    assert(len(pages) == 3)
    for i in range(len(pages)):
        assert(type(pages[i]) == src.page.BernoulliPage)

