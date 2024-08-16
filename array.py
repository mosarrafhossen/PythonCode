"""
x = [4, 2, 7, 0, -1]
print (x)
x.append(10)
x.append(3)
print("After append: ", x)

x.sort()
print("After sort", x)

x.reverse()
print("After sort", x)
x.remove(4)
print("After sort", x)

x.append(10)
print(x.count(10))

x.clear()
print("After clear", x)




import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end
"""


# import array as arr
# numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
#
# # changing first element
# numbers[0] = 0
# print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])
#
# # changing 3rd to 5th element
# numbers[2:5] = arr.array('i', [4, 6, 8])
# print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])


import numpy as np
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in x:
    print(i, end='')
print('\n', x)
print(i)

for i in x:
    for j in i:
        print(j, end=' ')
xx = np.array([[[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]]])
print("\n")
for i in np.nditer(xx):
    print(i, end=' ')
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
y = np.median(speed)
z = np.mod(speed)
print(x)
print(y)
print(z)

for x in range(2, 5):
    print("Weired")