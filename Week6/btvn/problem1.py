
class Manufacturer:
    def __init__(self, identity : int, location : str):
        self.__identity = identity
        self.__location = location

    @property
    def identity(self):
        return self.__identity

    @identity.setter
    def identity(self, identity):
        self.__identity = identity

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def describe(self):
        print(f"Manufacturer (identity = {self.__identity}, location = {self.__location}")

class Device:
    def __init__(self, name : str, price:float, identity:int, location:str):
        self.__name = name
        self.__price = price
        self.__manufacturer = Manufacturer(identity, location)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def describe(self):
        print(f"Name : {self.__name} - Price : {self.__price} - Identity : {self.__manufacturer.identity} - Location : {self.__manufacturer.location}")


device1 = Device("Mouse", 2.5, 9725, "Vietnam")
device1.describe()
device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()