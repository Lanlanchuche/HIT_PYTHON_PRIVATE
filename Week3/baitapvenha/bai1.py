numbers = [1, 5, -6, 7, 10, 4, 7, 1, 5]
numbers.reverse()

#loai trung
for i in numbers:
    if numbers.count(i) > 1:
        numbers.remove(i)#xoa phan tu dau tien trong dsach
numbers.reverse()#dao ngc ve thu tu ban dau
print("Danh sach sau khi loai bo so trung:")
print(numbers)
evennumbers = []
oddnumbers = []

# tinh chan le
for i in numbers:
    if i % 2 == 0:
        evennumbers.append(i**2)
    else:
        oddnumbers.append(i**3)
print("Danh sach chan: ", evennumbers)
print("Danh sach le: ", oddnumbers)

# trung binh vi tri chan
tbc = 0
count = 0
for i in numbers[::2]:
    tbc += i
    count+= 1
tbc = tbc/count
print("Trung binh cong cac so chan trong mang la: ", tbc)

#sap xep
n = len(numbers)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if abs(i) > abs(j):
            i, j = j, i
print("Danh sach sau khi sap xep la: ", numbers)