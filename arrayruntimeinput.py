from array import *
marks = array('i', [])
n = int(input("Enter the number of student in your class"))
print("number of student=", n)

for i in range(n):
    x = int(input("Enter the marks of next student"))
    marks.append(x)

print(marks)
for k in marks:
    print(k)
search = int(input("Enter the marks you want to find"))

i = 0
for find in marks:
    if find == search:
        print("Element you found at position=",i)
        break
    i += 1
else:
    print("Element not found")
print(marks.index(search))