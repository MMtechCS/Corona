from array import *

marks = array('i', [1, 2, 3, 45, 6, 7, 7, 8])
print(marks)
print(marks.typecode)
print(marks.buffer_info())
marks.reverse()
print(marks)
# for i in marks:
#     print(marks[i])

for i in range(6):
    print(marks[i])

print("output of  another for loop")

for i in range (len(marks)):
    print(marks[i])


print("output of  while loop")

j=0
while j<(len(marks)):
    print(marks[j])
    j=j+1

print("output of another for loop")


for k in marks:
    print(k)

vowel = array('U', ['a', 'e', 'i', 'o', 'u'])
print(vowel)
