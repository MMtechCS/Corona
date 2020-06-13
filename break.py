import random

num = random.randint(40,100)

# print(num)

count = 0

while count < 5:
    a = int(input("Enter any number between 40 and 100 "))
    if num == a:
        print("You Guessed  and win")
        break
    else:
        count = count + 1

if not count < 5:
    print("You Lose")
