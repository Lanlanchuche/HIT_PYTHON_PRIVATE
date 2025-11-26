class Person:
    def __init__(self, name = "No Name", age = 0, city = "No City"):
        self.__name = name
        self.__age = age
        self.__city = city

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Ten k de trong")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if len(city) > 0:
            return self.__city
        else:
            print("Ten city k duoc de trong")

    def printInfo(self):
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("City:", self.__city)

class Student(Person):
    __gender = 'female'
    def __init__(self, name, age, city , school = 'No school'):
        super().__init__(name, age, city)
        self.__school = school

    def printInfor(self):
        super().printInfo()
        print("Gender:", self.__gender)
        print("School: ", self.__school)

p1 = Person()
# p1.printInfo()
# p2 = Student("ABCD", 19, "dfg City","X School")
# p2.printInfor()
p1.set_name("Lan")
print(p1.get_name())
p1.age = 19
print(p1.age)
p1.city = ""
print(p1.city)

