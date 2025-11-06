coded_str = input("Nhap chuoi: ")
number = "123456789"
result = ''
for i in coded_str:
    if i in number:
        for j in range(int(i)):
            pass
    else:
        result += i