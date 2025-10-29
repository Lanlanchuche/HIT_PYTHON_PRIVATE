email = input("Enter your email: ")
mark1 = -1
mark2 = -1
for i in email:
    if i == "@":
        flag1 = True
    if i == ".":
        flag2 = True
if (not flag1) or (not flag2):
    print("Invalid")
elif mark2 - mark1 == 1:
    print("Invalid")
else:
    print("Valid")