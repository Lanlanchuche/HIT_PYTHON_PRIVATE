import numpy as np

#tao mang voi gia tri dac biet
zeros_arr = np.zeros((3,4)) #truyen vao kich thuoc mang
print("Zero array: \n", zeros_arr)

#tao ma tran 2x3 toan so 1, ep kieu int32
ones_arr = np.ones((2,3), dtype = np.int32)

#tao ma tran 2x2 toan so 7
full_arr = np.full((2,2),7)

#tao day so
range_arr = np.arange(1,10,2)
print("\nArrange array:", range_arr)#tuong tu range(0,10,2)

linspace_arr = np.linspace(0, 1, 5)  # 5 số từ 0 đến 1 cách đều
print("Linspace array:", linspace_arr)

# Ma trận đơn vị
identity_matrix = np.eye(3)
print("\nMa trận đơn vị 3x3:\n", identity_matrix)

# Mảng ngẫu nhiên
random_arr = np.random.rand(2, 3)  # Số ngẫu nhiên từ [0, 1)
print("\nRandom array:\n", random_arr)



int_random = np.random.randint(1, 100, (3, 4))  # Số nguyên từ 1-99
print("\nRandom integers:\n", int_random)
