chuoi = input(">>")
count = 0
for i in range(len(chuoi)):
    if chuoi[i] == 'u' or chuoi[i] == 'e' or chuoi[i] == 'o' or chuoi[i] == 'a' or chuoi[i] == 'i':
        count += 1
print("So nguyen am la: ", count)
print(chuoi[::-1])
if (chuoi == chuoi[::-1]):
    print("La chuoi palindrome")
else:
    print("Khong phai chuoi palindrome")