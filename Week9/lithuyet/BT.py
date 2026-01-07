import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu
# Mô tả: Load file CSV từ Kaggle: heart.csv vào DataFrame df.
df = pd.read_csv('heart.csv')

print(df.head()) # Chỉ lấy 5 hàng đầu
# print(df)

# In ra tất cả hàng, cột và giá trị từng ô
pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.max_rows', None)  # Hiển thị tất cả các hàng
pd.set_option('display.max_colwidth', None)  # Không rút gọn chuỗi trong ô
# print(df)

# Khôi phục về mặc định ban đầu
pd.reset_option('display.max_columns')
pd.reset_option('display.max_colwidth')
pd.reset_option('display.max_rows')

# Kiểm tra cấu trúc
# print(df.info())      # entries là số hàng, total là số cột, (số thứ tự cột, tên cột, số giá trị, kiểu dữ liệu)

# print(df.head())
Sex_map = {"M": 1, "F": 2}
ChestPainType_map = {"ATA" : 1, "NAP" : 2, "ASY" : 3, "TA" : 4}
RestingECG_map = {"Normal" : 1, "ST" : 2, "LVH" : 3}
ExerciseAngina_map = {"N": 1, "Y" : 2}
ST_Slope_map = {"Up" : 1, "Flat" : 2, "Down" : 3}

df["Sex_num"] = df["Sex"].map(Sex_map)
df["ChestPainType_num"] = df["ChestPainType"].map(ChestPainType_map)
df["RestingECG_num"] = df["RestingECG"].map(RestingECG_map)
df["ExerciseAngina_num"] = df["ExerciseAngina"].map(ExerciseAngina_map)
df["ST_Slope"] = df["ST_Slope"].map(ST_Slope_map)
# print (df.head())

# print(df.info())

# print(df.shape)     #Hiển thị (số_dòng, số_cột)

# print(df.describe())
# count → số giá trị không thiếu
# mean → trung bình cộng
# std → độ lệch chuẩn (biểu thị độ phân tán)
# min / max → giá trị nhỏ nhất / lớn nhất
# 25%, 50%, 75% → các phần trăm phân vị (quartiles)

cnt_Cholesterol = (df["Cholesterol"] == 0).sum()
print ("Số dòng Cholesterol = 0:", cnt_Cholesterol)

cnt_RestingBP = (df["RestingBP"] == 0).sum()
print("Số dòng RestingBP = 0:", cnt_RestingBP)

df_RestingBP_0_ver1 = df[df["RestingBP"] == 0]
print(df_RestingBP_0_ver1)
df_RestingBP_0_ver2 = df.loc[df["RestingBP"] == 0]
print(df_RestingBP_0_ver2)

# .loc[hàng, cột]
df_RestingBP_0_ver3 = df.loc[df["RestingBP"] == 0, ["Age", "Sex"]]
print(df_RestingBP_0_ver3)

pd.set_option('display.max_columns', None)
print(df)
df_new = df.drop("Cholesterol", axis=1)     #axis = 1 là xóa cột, 0 là xóa hàng
print(df_new.head())

pd.reset_option('display.max_columns')

df_new = df.drop(4)     #Tương đương .drop(4, axis=0)
print (df_new.head())
print (df.head())

print(df_new.shape)
print(df.shape)

print(df.isnull().sum())

numeric_cols = df.select_dtypes(include='number').columns       #Lấy danh sách các cột có kiểu số (number)

plt.close()
fig = plt.figure(figsize=(20,5))

axes = []
for i in range (len(numeric_cols)):
    ax = fig.add_subplot(1, len(numeric_cols), i+1)
    #ax là 1 ô nhỏ trên biểu đồ (số hàng, số cột, số thứ tự)
    #Số hàng: sẽ ảnh hưởng đến tỷ lệ chiều cao của biểu đồ, 2 thì biểu đồ sẽ cao 1/2
    #Số cột: giúp các cột đều có đủ chỗ để biểu diễn
    #Số thứ tự: trong figure bắt đầu từ 1, ảnh hưởng đến thứ tự khi biểu diễn
    axes.append(ax)

for i, col in enumerate(numeric_cols):
    axes[i].hist(df[col], bins=5, color='skyblue', edgecolor='black', alpha=1)
    # bin : số cột, color : màu cột, edgecolor : màu viền cột, alpha : độ trong suốt của cột (0-1)
    axes[i].set_title(col)  #Gán nhãn cho các biểu đồ
    plt.tight_layout()      #Điều chỉnh để các biểu đồ không bị đè lên nhau
plt.show()

cnt = df.isnull().sum()
print(cnt)

print(df["HeartDisease"].value_counts())        #giá trị duy nhất   :    số lượng

counts = df['HeartDisease'].value_counts().sort_index()     # sort_index() để đảm bảo 0 trước, 1 sau
values = counts.values                                      # trả về 1 list chứa số lượng các giá trị duy nhất

# Gán nhãn
labels = ['Do not have heart disease', 'Have heart disease']

# Gán màu tương ứng
colors = ['skyblue', 'salmon']

# Vẽ biểu đồ tròn
plt.close()     #plt.close("all")       Đóng figure hiện tại hoặc tất cả
plt.figure(figsize=(6,6))
plt.pie(
    values,               # số lượng từng nhóm
    labels=labels,        # nhãn hiển thị
    colors=colors,        # màu từng nhóm
    autopct='%1.1f%%',    # hiển thị phần trăm trên từng miếng  ([tổng số ký tự, thiếu thì tự thêm khoảng trắng bên trái], [số chữ số sau dấu phẩy])
    startangle=90         # xoay biểu đồ để miếng đầu tiên bắt đầu từ trên
)
plt.title("Distribution of Heart Disease")  # Tên biểu đồ
plt.show()

count = df["Sex"].value_counts()
label = ["Male", "Female"]
colors = ['skyblue', 'salmon']
values = count.values

plt.close()

plt.figure(figsize=(10,10))

plt.bar(
    label,              # Nhãn trục x
    values,             # Chiều cao của cột
    color=colors,       # Màu của cột
    edgecolor='black',  # Màu viền của cột
    width = 0.3,        # Độ rộng của cột
)
plt.xlabel("Giới tiính")
plt.ylabel("Số lượng")
plt.title("Biểu đồ giới tính")
plt.show()

fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.2, 0.2, 0.3, 0.6])

# plt.figure(figsize=(10,10))
ax.bar(
    label,              # Nhãn trục x
    values,             # Chiều cao của cột
    color=colors,       # Màu của cột
    edgecolor='black',  # Màu viền của cột
    width = 0.1,        # Độ rộng của cột
)
ax.set_xlabel("Giới tiính")
ax.set_ylabel("Số lượng")
ax.set_title("Biểu đồ giới tính")
plt.show()
