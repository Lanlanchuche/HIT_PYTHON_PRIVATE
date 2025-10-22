print("Chao mung den CLB Tin Hoc HIT")
print('CLB Tin Hoc HIT truc thuoc truong CNTT - "10 diem"')
str = "CLB Tin Hoc HIT truc thuoc truong CNTT"
strcpy = ""
for i in str:
    if i.isupper():
        strcpy += i
print(strcpy)

strcpy2 =""
for i in str:
    if i.islower():
        strcpy2 += i
print(strcpy2)
if "CNTT" in str:
    print("Yes")
else:
    print("No")
    
#swapcase k thay di chuoi goc ma tra ve chuoi moi
newstr = str.swapcase()
print(newstr)