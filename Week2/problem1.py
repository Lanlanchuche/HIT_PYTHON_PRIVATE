import math
n = int(input("n = "))
x = int(input('x = '))
sum = 1


for i in range (1, n + 1):
    ms = 1
    for j in range (1, i + 1):
        ms *= j
    sum += (x**i)/ms

print(f"e^x = {round(sum, 3)}")

sum = 0

for i in range (1, n + 1):
    ms = 1
    for j in range (1, i + 1):
        ms*= j
    sum += 1/ms

print(f"S = {round(sum, 4)}")
