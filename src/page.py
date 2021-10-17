from abc import ABC, abstractmethod
import random


def getBernoulliPageList(probabilities):
    lst = []
    for i in range(len(probabilities)):
        lst.append(BernoulliPage(probabilities[i]))
    return(lst)

class Page(ABC):
    """
    Implements a test() method that returns success 
    """
    
    @abstractmethod
    def test():
        pass



class BernoulliPage(Page):

    def __init__(self, probability):
        
        if type(probability) != int and type(probability) != float:
            raise Exception("Probability must be a number")
        if not 0 <= probability <= 1:
            raise Exception("Probability must be between 0 and 1")
        self.probability = probability

    def test(self):
        return(random.random() < self.probability)
        
        
