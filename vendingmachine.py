num = int(input("How many toffee you want "))
av = 20
i = 1
while i <= num:
    if i<= av:
        print(i, "Please collect toffee")
    else:
        print("Out of Stock")
        break
    i = i + 1
else:
    print("thank you visit again")