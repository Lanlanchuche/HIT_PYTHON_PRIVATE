string = input("Nhap chuoi >>  ")

result = ''
for i in string:
    if i.isalpha() or i.isspace():
        result += i

print("Chuoi sau khi chuan hoa: ", result)
result = result.lower()
print("Chuyen ve chu thuong: ", result )
count = 0#dem nguyen am
count1 = 0 #dem phu am
for i in result:
    if i == "a" or i == 'u' or i == 'e' or i == 'o' or i == 'i':
        count += 1
    else:
        count1 += 1
print(f"Nguyen am: {count}, Phu am: {count1}")

list = result.split()
for i in range(len(list)):
    list[i] = list[i][::-1]

print(list)
reversed_result = result[::-1]
check = reversed_result == result
print("Palindrome: ", check)