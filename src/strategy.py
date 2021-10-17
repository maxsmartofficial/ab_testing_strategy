from abc import ABC, abstractmethod

class Strategy(ABC):

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
        
        
