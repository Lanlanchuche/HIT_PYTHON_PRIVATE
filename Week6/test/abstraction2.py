from abc import ABC, abstractmethod
class Animal(ABC):
     @abstractmethod
     def Move(self):
         pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

