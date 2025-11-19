chuoi = input("Nhap chuoi >>")
list = chuoi.split(",")
list = set(list)
list = tuple(list)
print(list)
count = len(list)
print("So loai hang hoa la:", count)

popularitem = {"Phone", "Laptop", "Smartwatch"}
popular = []
notpopular = []
# for item in list:
#     if item in popularitem:
#         popular.append(item)
#     else:
#         notpopular.append(item)
print("Danh sach san pham co trong kho va ban chay la:")
print(popular)
print("Danh sach san pham co trong kho nhung khong ban chay la:")
print(notpopular)



