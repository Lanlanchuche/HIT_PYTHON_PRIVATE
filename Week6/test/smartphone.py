
class Smartphone:
    weight = 0.2
    Price = 2000000
    # def __init__(self, name, color):
    #     self.name = name
    #     self.color = color

    def inThongTin(self):
        print("Name of smartphone:", self.name)
        print("Color of smartphone:", self.color)
        print("Price: ", Smartphone.Price)


    def trongLuong(self):
        print('Weight of smartphone:', self.weight)

    @classmethod
    def tangCan(cls):
        cls.weight += 0.1



# newPhone = Smartphone("IPhone16", "Titan")
# newPhone.inThongTin()
# oldPhone = Smartphone("IPhoneX", "Gold")
# Smartphone.Price = 199999
# oldPhone.inThongTin()


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return self.radius**2*3.14

hl = Circle(2)
print("-------------------")
print("Dien tich hinh tron:", hl.getArea())
print("------------------")
newphone = Smartphone()
oldphone = Smartphone()
Smartphone.tangCan()#giong newphone.tangCan()
newphone.tangCan()#2 cau lenh nay giong nhau

newphone.trongLuong()

oldphone.trongLuong()



