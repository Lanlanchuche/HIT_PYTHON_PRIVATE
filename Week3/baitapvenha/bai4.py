listinput = input("Nhap ten:diem ")
listinput = listinput.split(',')
ds = []
for i in listinput:
    ten, diem = i.strip().split(':')
    ds.append((ten, int(diem)))#append() chi nhan 1 tham so -> dua no thanh 1 tuple

print(ds)

setname = set()
for ten, diem in ds:
    setname.add(ten)
print(setname)
#tinh diem tb
average = []
for name in setname:
    count = 0
    sum = 0
    for ten, diem in ds:
        if ten == name:
            count += 1
            sum += diem
    tb = sum/count
    average.append((name, tb))

print("Danh sach diem trung binh: ", average)

