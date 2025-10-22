a = int(input("a = "))
b = int(input("b = "))
#toan tu so hoc
print("a + b = ", a + b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a // b = ", a//b)
print("a ^ b = ", a**b)
print("a % b = ", a%b)
#toan tu so sanh
if a < b :
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a = b")
#toan tu bit
print("a AND b is " , a & b)
print("a OR b is ", a|b)
print("a XOR b is ", a^b)
print("NOT a == b is ", ~a == b)
print("a dich phai 5 bit: ", a >> 5)
print("a dich trai 6 bit: ", a << 6)

print("a o dang co so 2 dao nguoc la: ")
bin = ""
while a > 0:
    bin += str(a%2)
    a = a//2
print(bin)
