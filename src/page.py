from abc import ABC, abstractmethod
import random


def getBernoulliPageList(probabilities):
    """
    Return a list of BernoulliPages with specified probabilities
    """
    lst = []
    for i in range(len(probabilities)):
        name = "Page " + str(i + 1) + "(" + str(probabilities[i]*100) + "%)"
        lst.append(BernoulliPage(probabilities[i], name=name))
    return(lst)



class Page(ABC):
    """
    Simulates whether people convert or not
    Implements a test() method that returns success or failure
    """
    
    @abstractmethod
    def test(self):
        """
        Test whether a conversion occurs
        """
        pass



class BernoulliPage(Page):
    """
    A simple page that represents a Bernoulli Trial
    i.e. people either convert or don't convert, with a given probability
    """

    def __init__(self, probability, name=""):
    
        self.name = name
        
        if type(probability) != int and type(probability) != float:
            raise Exception("Probability must be a number")
        if not 0 <= probability <= 1:
            raise Exception("Probability must be between 0 and 1")
        self.probability = probability

    def test(self):
        return(random.random() < self.probability)
        
        
