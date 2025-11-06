student = {"name": "Nam", "grade": "A", "year": 2025}

# pop(key) - xóa và trả về giá trị
student.pop("grade")

# popitem() - xóa cặp cuối cùng (Python 3.7+)
student.popitem()

# del - xóa theo key
del student["name"]

# clear() - xóa toàn bộ
student.clear()

print(student)

scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Duyệt key
for name in scores:
    print(name)

# Duyệt value
for score in scores.values():
    print(score)

# Duyệt cả key và value
for name, score in scores.items():
    print(name, ":", score)
info = {"name": "Lan", "age": 19}

# copy()
clone = info.copy()# dung clone = info thi tro chung 1 o nho

# update() - gộp dict khác
info.update({"city": "Hue"})#k tra ve

# keys(), values(), items()
print(info.keys()) # trích xuất và trả về các khóa của các mục trong từ điển
print(info.values()) # trích xuất và trả về các giá trị của các mục trong từ điển
print(info.items()) # trích xuất và trả về các cặp (key, value) của các mục trong từ điển