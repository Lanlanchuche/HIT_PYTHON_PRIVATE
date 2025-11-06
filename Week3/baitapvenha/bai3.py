chuoi = input("Nhap vao 1 chuoi: ")
chuoi = chuoi.lower()
list = chuoi.split()
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
#dem so lan xuat hien cua tung tu
countmax = 0
word = ''
for i in unique_list:
    print(f"Chu {i} xuat hien {list.count(i)} lan")
    if list.count(i) > countmax:
        countmax = list.count(i)
        word = i
print("Tu co tan suat xuat hien cao nhat la", word)
#tim tu dai nhat
length = 0
longword = ''

for i in unique_list:
    print(f"So ki tu cua {i} la: {len(i)}")
    if len(i) > length:
        length = len(i)
        longword = i

print("Tu dai nhat la: ", longword)
#sap xep do dai giam dan
for i in range(len(unique_list) - 1):
    for j in range(i + 1, len(unique_list)):
        if(len(unique_list[i]) < len(unique_list[j])):
            unique_list[i], unique_list[j] = unique_list[j], unique_list[i]
print("Danh sach tu sap xep theo do dai giam dan la: ", unique_list)