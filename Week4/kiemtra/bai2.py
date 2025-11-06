chuoi = input("Nhap chuoi: ")
chuoi = chuoi.lower()
chuoi2 = {}
for i in chuoi:
    chuoi2[i] = chuoi.count(i)
for char, count in chuoi2.items():
    print(f"Chu {char} xuat hien {count} lan")