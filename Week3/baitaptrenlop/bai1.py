n = int(input("Nhap so luong diem muon them: "))

marks = []
for i in range(n):
    mark = float(input("Nhap diem:"))
    if mark >= 5:
        marks.append(mark)
#sap xep giam dan
marks.sort(reverse=True)
print(marks)
#diem cao nhat
#print(marks[0])
maxmark = max(marks)
print(maxmark)
#diem thap nhat
#print(marks[-1]
minmark = min(marks)
print(minmark)

maxmark2 = marks[0]
print(f"Diem cao nhat: {maxmark2}")
