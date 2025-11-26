class Person:
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def yob(self):
        return self._yob

    @yob.setter
    def yob(self, yob):
        self._yob = yob

class Student(Person):
    def __init__(self, name:str, yob:int, grade:float):
        super().__init__(name, yob)
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    def describe(self):
        print(f"Student - Name : {self._name} - YoB : {self._yob} - Grade : {self.__grade}")

class Teacher(Person):
    def __init__(self, name:str, yob:int, subject:str):
        super().__init__(name, yob)
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    def describe(self):
        print(f"Teacher - Name : {self._name} - YoB : {self._yob} - Subject : {self.__subject}")

class Doctor(Person):
    def __init__(self, name:str, yob:int, specialist:str):
        super().__init__(name, yob)
        self.__specialist = specialist

    @property
    def specialist(self):
        return self.__specialist

    @specialist.setter
    def specialist(self, specialist):
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor - Name : {self._name} - YoB : {self._yob} - Specialist : {self.__specialist}")



class Ward:
    def __init__(self, name):
        self.__name = name
        self.__people = []

    def addPerson(self, person:Person):
        self.__people.append(person)

    def printAll(self):
        for person in self.__people:
            person.describe()

    def countDoctor(self):
        count = 0
        for person in self.__people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sortAge(self):
        #sap xep tuoi tang dan -> nam sinh giam dan
        self.__people = sorted(self.__people, key = lambda x: x.yob(), reverse = True)

    def aveTeacherYearOfBirth(self):
        for p in self.__people:
            total = 0
            count = 0
            if isinstance(p, Teacher):
                total += p.yob()
                count += 1
        if(count == 0):
            return 0
        else:
            return total/count

student1 = Student(name="studentA", yob=2010, grade= 7.0)
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
print("-------------------------------------")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)

ward1.printAll()


