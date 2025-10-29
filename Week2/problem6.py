totalPrice = 0
count = 0
while True:
    dish = input("Nhap ten mon: ")
    if (dish == "pass"):
        pass
    elif dish == "skip":
        continue
    elif dish == "x":
        break;
    else:
        price = input("Nhap gia tien: ")
        if price.isalpha():
            continue
        else:
            price = int(price)
            totalPrice += price
            count += 1

print(f"So mon: {count}")
if totalPrice > 200000:
    discount = totalPrice * 0.1
    print(f"Tong tien truoc giam gia: {totalPrice}")
    print(f"Giam gia 10%: {discount}")
    print("Tong tien phai tra: ", totalPrice - discount)
else:
    print(f"Tong tien phai tra: {totalPrice}")