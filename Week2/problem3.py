n = int(input("Nhap so luong hoc vien: "))

for i in range (n) :
    stt = int(input("Nhap so thu tu: "))
    name = input("Nhap ten: ")
    mark1 = int(input("Nhap diem bai 1: "))
    mark2 = int(input("Nhap diem bai 2: "))
    mark = mark1 + mark2
    if mark >= 200:
        grade = "Xuat Sac"
    elif mark >= 150 and mark < 200:
        grade = "Gioi"
    elif mark >= 100 and mark < 150:
        grade = "Kha"
    else:
        grade = "Yeu"
    print(f"{stt} {name} {mark} {grade}")