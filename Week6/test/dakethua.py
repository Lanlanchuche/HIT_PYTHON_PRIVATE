class ClassA:
    def inTT(self):
        print("Xin chao moi nguoi")

class ClassB:
    def inTT(self):
        print("Hello everyone")

class ClassC(ClassB, ClassA):
    def inTT(self):
        super().inTT()
class ClassD(ClassC, ClassA):#doi cho K bi loi
    def inTT(self):
        super().inTT()

d = ClassD()#uu tien ke thua lop cha dau tien
print(ClassD.mro())
d.inTT()




