from array import *


# arr = array('i', [1, 2, 3, 4, 5])
# print(arr.buffer_info())

# for i in range(5):
#     print(arr[i]," " ,end='')
# for j in range(5):
#     print()
# arrch= array('u', ['a','b','c'])
# print(arrch)


arr = array('i', [])


n = int(input("Enter your lenght value : "))

for i in range(n):
    x=int(input("Enter your value : "))
    arr.append(x)
print(arr)


search = int(input("Enter search value : "))

print(arr.index(search))

