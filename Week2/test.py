a = ["hello", 1, 65, "thank you", [2,3]]
for value in a:
    print(value)

list_of_tuples = [(1, 2), (3, 4)]
for a, b in list_of_tuples:
    print("a: ", a, "b: ", b)
for character in ["p", "y", "h", "o", "n"]:
    print("Give me a '{}'!".format(character))
    print("Give me a '",character,"'!")

for i in range(10):
    print (i)
for i in range(4, 10, 2):
    print(i)

#while
#secret_keyword = "Python"
#user_input = input("Please enter the secret keyword: ").capitalize()

#while user_input != secret_keyword:
 #   user_input = input("Please enter the secret keyword: ").capitalize()
fruits = ["apples", "oranges", "babanas", "melons"]
prices = [20, 10, 5, 15]
quantities = [5, 7, 3, 4]
for fruit, price, quantity in zip(fruits, prices, quantities):
    print(f"You bought {quantity} {fruit} for ${price*quantity}")

L1 = [1, 2, 3, 4, 5]
L2 = ['A', 'b', 'c', 'd']
zip_L1L2 = zip(L1, L2)
print(list(zip_L1L2))#ep doi tuong zip thanh cac tuple de in ra, neu k thi phai dung vong lap in ra

#enumerate(giatri, chimuc)-> chi muc bat dau bang tham so truyen vao
#enumerate(giatri) -> chi muc mac dinh la 0
names = ["John", "Jane", "Doe"]
enumNames = enumerate(names,start = 10)
for item in enumNames:
    print(item)#dung vong for nhu the nay hoac dung print(list(enumNames))
num = 5
while num < 20:
    print('Current number : ', num)
    num += 1
    if num == 9:
        break
for letter in "Jessica":
    if letter == 'i':
        continue
    print(letter)

for x in [0,1, 2]:
    pass
