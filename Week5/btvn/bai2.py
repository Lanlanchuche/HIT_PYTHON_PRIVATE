students = [
    {"id": 1, "name": "An", "score": 8.5},
    {"id": 2, "name": "Bình", "score": 7.2},
    {"id": 3, "name": "Chi", "score": 9.0}
]

def find_by_id(data:list, id:int):
    for student in data:
        if student['id'] == id:
            return student
    return None

def filter_by_score(data:list, min_score:float):
    result = []
    for student in data:
        if student["score"] >= min_score:
            result.append(student)
    return result

def sort_by_score(data:list, reverse = False):
    if reverse == False:
        data = sorted(data, key = lambda x: x["score"])
        return data
    else:
        data = sorted(data, key = lambda x: x["score"], reverse = True)
        return data

def add_student(data:list, student_dict:dict):
    data.append(student_dict)

def remove_student(data:list, id:int):
    for student in data:
        if student["id"] == id:
            data.remove(student)

def statistics(data:list):
    max_score = 0
    min_score = 10
    mean_score = 0
    highest_score_student = {}
    lowest_score_student = {}
    for student in data:
        if student["score"] > max_score:
            max_score = student["score"]
            highest_score_student = student
        if student["score"] < min_score:
            min_score = student["score"]
            lowest_score_student = student
        mean_score += student["score"]

    mean_score = mean_score/len(data)
    return (mean_score, highest_score_student, lowest_score_student)

id = int(input("Nhap id sinh vien muon tim: "))
if find_by_id(students, id) == None:
    print("Khong tim thay")
else:
    print(find_by_id(students, id))

score = float(input("Nhap diem: "))
print(f"Sinh vien co diem >= {score} la: {filter_by_score(students, score)}")

print("Danh sach sinh vien sau khi sap xep la:")
print(sort_by_score(students))

addition = {"id":4,"name":"Dũng","score":6.8}

add_student(students, addition)
print("Danh sach sinh vien sau khi them la:" )
print(students)

mean, highest, lowest = statistics(students)
print(f"Diem trung binh: {mean}")
print("Sinh vien co diem cao nhat:", highest)
print("Sinh vien co diem thap nhat:", lowest)
