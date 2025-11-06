arr = input("Nhap chuoi so nguyen: ").split()

result = []
cpy = []
print(arr)
for i in range(len(arr)):
    cpy.append(arr[i])
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            break
        else :
            if arr[j] not in cpy:
                cpy.append(arr[j])
            else:
                break
    if len(cpy) > len(result):
        result = cpy.copy()
        cpy.clear()
    else :
        cpy.clear()


print("Doan con dai nhat: ", result)
print("Do dai: ", len(result))