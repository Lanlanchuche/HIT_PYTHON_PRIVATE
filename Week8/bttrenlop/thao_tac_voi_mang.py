import numpy as np

arr = np.array([10,20,30,40,50,60,70])
print("Original array: ", arr)
print("arr[0] = ", arr[0])
print("arr[-1] = ", arr[-1])
print("arr[1:4]:", arr[1:4]) # Từ index 1 đến 3
print("arr[::2]:", arr[::2]) # Mỗi 2 phần tử
print("arr[::-1]:", arr[::-1]) # Đảo ngược mảng

# Mảng 2D
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("\n2D array:")
print(arr2d)
print("arr2d[0, 1]:", arr2d[0, 1])      # Hàng 0, cột 1
print("arr2d[1]:", arr2d[1])           # Cả hàng 1
print("arr2d[:, 1]:", arr2d[:, 1])     # Cả cột 1
print("arr2d[0:2, 1:3]:\n", arr2d[0:2, 1:3]) # Subarray
