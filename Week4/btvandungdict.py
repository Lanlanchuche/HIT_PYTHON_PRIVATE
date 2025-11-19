students = {}

while True:
    code = input("ID: ")
    if code == "":
        break;
    code1 = input("Ho ten: ")
    students[code] = code1

#tim xem co sinh vien co id 2020601001
maSV = input("Nhap ma sinh vien muon tim: ")
for id in students.keys():
    if(id == maSV):
        print("Co ton tai sinh vien")
        print(f"Ho va ten sinh vien la: {students[id]}")
        break

newdict = {}
for id, name in students.items():
    if int(id) % 2 == 0:
        newdict[id] = name
print("Danh sach sinh vien co ma sinh vien chan la:")
print(newdict)