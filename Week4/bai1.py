
marks = {"An": 8.5, "Bình": 7.2, "Chi": 9.0, "Dũng": 6.8, "Hà": 8.0}

while True:
    print("1. In danh sach hoc sinh")
    print("2. Tim hoc sinh co diem tb cao nhat va thap nhat")
    print("3. Tinh diem tb cua ca lop")
    print("4.Tao dict moi luu xep loai")
    print("5. Sap xep danh sach giam dan")
    print("0. Thoat")

    choice = int(input("Nhap: "))
    if choice == 0:
        break
    if choice == 1:
        for name, score in marks.items():
            print(name ,":", score)
    if choice == 2:
        maxscore = 0
        minscore = 10
        for name, score in marks.items():
            if score > maxscore:
                maxscore = score
                maxperson = name

            if score < minscore:
                minscore = score
                minperson = name

        print("Nguoi diem cao nhat la :", maxperson, ", diem: ", maxscore)
        print("Nguoi diem thap nhat la :", minperson, ", diem: ", minscore)

    if choice == 3:
        total = 0
        count = 0
        for score in marks.values():
            total += score
            count += 1
        print("Diem trung binh cua ca lop la: ", total/count)

    if choice == 4:
        new = {}
        for name, score in marks.item():
            if score >= 8:
                new[name] = "Gioi"
            if score >= 6.5 and score < 8:
                new[name] = "Kha"
            if score < 6.5:
                new[name] = "Trung binh"
        #in dsach moi
        for name, grade in new.item():
            print(name, ":", grade)