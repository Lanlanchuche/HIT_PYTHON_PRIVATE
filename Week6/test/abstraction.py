from abc import ABC as j, abstractmethod #co dinh
class Shape(j):

    @abstractmethod
    def dienTich(self):
        pass

    @abstractmethod
    def chuVi(self):
        pass

    def inTT(self):
        print("Dien tich:", self.dienTich())
        print("Chu vi:", self.chuVi())

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def dienTich(self):
        return self.__width * self.__height

    def chuVi(self):
        return 2*(self.__width + self.__height)

h1 = Rectangle(3, 4)
h1.inTT()


