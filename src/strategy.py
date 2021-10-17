from abc import ABC, abstractmethod
import random

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.page

class Strategy(ABC):

    name = "DEFAULT STRATEGY"

    @abstractmethod
    def __init__(self, pages):
        """
        Initialise the agent with the choice of pages
        """
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
    
    name = "Random Strategy"
    
    def __init__(self, pages):
        
        for p in pages:
            if not issubclass(p.__class__, src.page.Page):
                raise Exception("Strategy must be given a list of Pages")
                
        self.pages = pages
        
    def choice(self):
        return(random.choice(self.pages))
        
    def update(self, page, result):
        pass