while True:
    #nhap den khi hop le
    while True:
        day = int(input("Nhap ngay sinh: "))
        month = int(input("Nhap thang sinh: "))

        if month in {1, 3, 5, 7, 8, 10, 12}:
            if day > 0 and day <= 31:
                break
        elif month in {4, 6, 9, 11}:
            if day > 0 and day <= 30:
                break
        elif month == 2:
            if day > 0 and day <= 29:
                break
        else:
            print("Ngay thang khong hop le!")
    #tinh toan
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Cung Bao Binh")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 20):
        print("Cung Bach Duong")
    elif (month == 4 and day >= 21) or (month == 5 and day <= 20):
        print("Cung Kim Nguu")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        print("Cung Song Tu")
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        print("Cung Cu Giai")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Cung Su Tu")
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        print("Cung Bo Cap")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Cung Xu Nu")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        print("Cung Thien Binh")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        print("Cung Song Ngu")
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        print("Cung Nhan Ma")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Cung Ma Ket")

    #tiep tuc chuong trinh
    print("Ban co muon tiep tuc khong? (y/n): ")
    goon = input().lower()
    if(goon == 'n'):
        break


