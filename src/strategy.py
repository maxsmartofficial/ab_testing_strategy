from abc import ABC, abstractmethod
import random
from collections import defaultdict

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.page

class Strategy(ABC):


    @abstractmethod
    def __init__(self, pages):
        """
        Initialise the agent with the choice of pages
        """
        name = "DEFAULT STRATEGY"
        pass
    
    @abstractmethod
    def choice(self):
        """
        Get which page to display
        Returns a subclass of Page
        """
        pass
        
    @staticmethod
    def update(self, page, result):
        """
        Update the agent based on the results of the test
        page is the page that was chosen
        result is a boolean representing whether the person converted
        """
        pass
        
        
class RandomStrategy(Strategy):

    """
    A basic strategy that chooses pages at random
    """
    
    
    def __init__(self, pages):
    
        self.name = "Random Strategy"
        
        for p in pages:
            if not issubclass(p.__class__, src.page.Page):
                raise Exception("Strategy must be given a list of Pages")
                
        self.pages = pages
        
    def choice(self):
        return(random.choice(self.pages))
        
    def update(self, page, result):
        pass
        


class GreedyStrategy(Strategy):

    def __init__(self, pages):
    
    
        for p in pages:
            if not issubclass(p.__class__, src.page.Page):
                raise Exception("Strategy must be given a list of Pages")
        
        self.pages = pages
        self.page_names = {p.name: p for p in pages}
        
        self.totals = defaultdict(int)
        self.successes = defaultdict(int)
    
    
    def _getBestPage(self):
        # Return best performing page
        average = 0
        for p in self.page_names.keys():
            if self.totals[p] != 0:
                mean = self.successes[p]/self.totals[p]
            else:
                mean = 0
                
            if mean > average:
                average = mean
                best_page = p
                
        # If there is no best page, or no data
        if average == 0:
            # Return a random page
            return(random.choice(self.pages))
        else:
            return(self.page_names[best_page])


    def update(self, page, result):
        
        self.totals[page.name] += 1
        if result:
            self.successes[page.name] += 1
        
        

class EpsilonGreedyStrategy(GreedyStrategy):
    
    def __init__(self, pages, epsilon):
    
        self.name = "Epsilon-greedy Strategy (" + str("{:0.2f}".format(epsilon)) + ")"
        
        self.epsilon = epsilon
        
        super().__init__(pages)
            
            
    def choice(self):
        # Sometimes, or if there is currently no data
        if random.random() < self.epsilon or sum(self.totals.values()) == 0:
            # Return a page at random
            return(random.choice(self.pages))
            
        else:
            # Return the currently best performing page
            return(self._getBestPage())
            
                    
                
class EpsilonFirstStrategy(GreedyStrategy):

    def __init__(self, pages, initial):
    
        self.name = "Epsilon-first Strategy (" + str(initial) + ")"
    
        self.initial = initial
        self.total = 0
        
        super().__init__(pages)
        
        
    def update(self, page, result):
    
        super().update(page, result)
    
        self.total += 1
        
            
    def choice(self):
        
        if self.total < self.initial:
            # Return random page
            return(random.choice(self.pages))
        else:
            # Return best performing page
            return(self._getBestPage())
            