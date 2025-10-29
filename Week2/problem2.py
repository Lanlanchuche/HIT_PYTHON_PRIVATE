n = int(input("n = "))
count = 0
for i in range(2, n):
    if n % i == 0 and i % 2 != 0:
        count+= 1

print(f"So uoc le cua n la {count}")