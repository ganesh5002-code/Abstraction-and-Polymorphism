from abc import ABC, abstractmethod

class Abclass(ABC):

    def number(self, x):
        self.n = x
        print(self.n)
    
    @abstractmethod
    def print(self):
        print("We are printing an Abclass")
    
class test_class(Abclass):

    def print(self):
        print("We are printing a test class")
    

obj = test_class()
obj.print()
obj.number(1000)