coded_str = input("Nhap chuoi da duoc ma hoa:")

numbers = "123456789"
decoded_str = ''
newstr = ''
i = 0
while i < len(coded_str):
    if coded_str[i] in numbers:
        k = int(coded_str[i])
    else:
        if coded_str[i] != '[':
            decoded_str += coded_str[i]
        else:#i == '[
            i+=1
            while coded_str[i] != ']':
                newstr += coded_str[i]
                i+=1
            decoded_str += k * newstr
        newstr = ''
    i+=1
print(decoded_str)