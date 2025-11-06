# Tạo list cơ bản
fruits = ["apple", "banana", "cherry"]
print(fruits)
#chen vao cuoi
fruits.append('orange'); print(fruits)
#xoa phan tu dau tien tim thay co gia tri bang tham so
fruits.remove('banana'); print(fruits)
#xoa va lay ra gia tri
removed = fruits.pop(0); print('Removed:', removed); print(fruits)
#xoa het list
nums = [1,2,3]; nums.clear(); print(nums)
#lay ra chi so cua gia tri truyen vao
nums = [10,20,30, 20]; print(nums.index(20))
#sap xep tang dan voi so, doi voi chu sap xep theo ma ASCII
nums = [3,1,4,2]; nums.sort(); print(nums)
#sap xep giam dan
nums.sort(reverse=True)
print(nums)
# List comprehension tạo danh sách bình phương số chẵn
squares = [x*x for x in range(10) if x%2==0]
print(squares)
#Slicing list -> lay list con
list1 = [1, 2, 3, 4, 5]
list2 = list1[0: 3:1]
print(list1, list2)
