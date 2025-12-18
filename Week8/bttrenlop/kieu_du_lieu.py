import numpy as np
# Các kiểu dữ liệu cơ bản
arr_int8 = np.array([1, 2, 3], dtype=np.int8)
arr_float64 = np.array([1.1, 2.2, 3.3], dtype=np.float64)
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex128)
arr_bool = np.array([True, False, True], dtype=np.bool_)

print("int8 array:", arr_int8, "dtype:", arr_int8.dtype)
print("float64 array:", arr_float64, "dtype:", arr_float64.dtype)
print("Complex array:", arr_complex, "dtype:", arr_complex.dtype)
print("Bool array:", arr_bool, "dtype:", arr_bool.dtype)

# Ép kiểu
arr = np.array([1.5, 2.7, 3.1])
print("\nOriginal array:", arr, "dtype:", arr.dtype)

# Ép sang int (mất phần thập phân)
arr_int = arr.astype(np.int32)
print("After astype(int32):", arr_int, "dtype:", arr_int.dtype)

# Ép sang float khác độ chính xác
arr_float32 = arr.astype(np.float32)
print("After astype(float32):", arr_float32, "dtype:", arr_float32.dtype)

# Kiểm tra kích thước bộ nhớ
print("\nMemory size comparison:")
print(f"float64: {np.array([1.0], dtype=np.float64).nbytes} bytes")
print(f"float32: {np.array([1.0], dtype=np.float32).nbytes} bytes")
print(f"int8: {np.array([1], dtype=np.int8).nbytes} bytes")