# View vs Copy
import numpy as np
print("\n--- View vs Copy ---")
arr = np.array([1, 2, 3, 4, 5])
view_arr = arr[1:4]      # Tạo view (không copy dữ liệu)
copy_arr = arr[1:4].copy() # Tạo bản copy

view_arr[0] = 999        # Thay đổi view sẽ thay đổi array gốc
print("Original after view modification:", arr)

copy_arr[0] = 777        # Thay đổi copy không ảnh hưởng gốc
print("Original after copy modification:", arr)
print("Copy array:", copy_arr)