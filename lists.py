"""
lists
store multiple values in 1 variable
"""

# a = [55, 92, 545, 7, 5, 96, 455]
# c = [55, 92, 545, 7, 5, 45, 85]
# d = c + a
# print(d)
# b = [32, "himanshu", 445.465]
# print(b[4])
# print(type(a))

# a = [55, "abc", 54]
# b = a * 4
# print(b)

# a = [55, 784, 55, 14, 12]
# for i in range(0, 5):
#     print(a[i])

# a = [89, 74, 52, 93, 75, 43, 24, 55]
# for i in range(0, 8):
#     if a[i] % 2 == 0:
#         print(a[i])
# b = 0
# a = [89, 74, 52, 93, 75, 11, 11]

# for i in range(0, 7):
#     b += a[i]
# print(b)

# a = [89, 74, 52, 93, 75, 11, 11]
# # for i in range(0, 7):
# #     if a[i] >= a:
# #         print(a[i])
# print(max(a))

# a = [89, 74, 52, 93, 75, 11, 11]
# m = 0
# for i in range(0, 7):
#     if a[i] >= m:
#         m += a[i]
# print(m)

# Slicing in list

# a = [89, 74, 52, 93, 75, 11, 11]
# print(a[4:7])
# print(a[3:])
# print(a[0::2])
# print(a[0::3])
# print(a[-1:-5, -1])
# print(a[-1::-1])

# a = [89, 74, 52, 93, 75, 11, 11]

# for i in a:
#     if i % 2 == 0:
#         print(i)

# a = [89, 74, 52, 93, 75, 11, 11]
# num = int(input("Enter a number: "))
# for i in range(0, len(a)):
#     if num == a[i]:
#         print(f"Position: {i}")

"""
Methods:
Add at last
Update
Insert
Delete
Sort
Count
"""

# a = [89, 74, 12.2, 52, 93, 75, "Himanshu", 11, 11, "Himanshu", 12.2]
"""Adds element in the last position"""
# a.append("Himanshu")
# a.append(14.25)
# print(a)
"""Adds the element to the specified position"""
# a[3] = 12.2
# print(a)
"""inserts the element to the specified position"""
# a.insert(1, 55)
# print(a)
"""Removes last element by default or if specified then from its position"""
# a.pop(5)
# print(a)
"""Removes the specified element from the start of the list and only removes one element if similar"""
# a.remove(12.2)
# print(a)
"""Gives the position of the specified element"""
# pos = a.index("Himanshu")
# print(pos)
# pos = a.index(100)
# print(pos)
"""Counts the number of times the element is repeated"""
# b = a.count(12.2)
# print(b)
"""Sorts the element in the ascending order"""
# a.sort()
"""Reverses the list of elements"""
# a.reverse()
# print(a)
"""Clears the list"""
# a.clear()
# print(a)
"""Extends the list with another list or a string"""
# b = [12, "Himanshu", 23.45]
# a.extend(b)
# print(a)
"""Copys the list of integers"""
# b = a.copy()
# print(a)

"""
Ask 5 numbers from user

"""
# myList = []
# a = int(input("Enter how many numbers you want to add in a list: "))
# for a in range(0, a):
#     n = int(input("Enter a number: "))
#     myList.append(n)

# b = int(input("Enter the number you want to count: "))
# c = myList.count(b)
# print(c)

"""
Even numbers in another list
"""
# a = [55, 44, 26, 75, 23, 29, 22, 87]
# b = []
# for i in range(0, 8):
#     if a[i] % 2 == 0:
#         b.append(a[i])
# print(b)

# a = [55, 44, 55, 75, 23, 29, 55, 87]
# num = int(input("Enter a number to remove: "))
# for i in range(0, 8):
#     if num == a[i]:
#         a.remove(a[i])


# print(a)

# a = [55, 44, 55, 75, 23, 29, 55, 87]
# num = int(input("Enter a number: "))

# print(num in a)

# a = [55, 44, 55, 75, 23, 29, 55, 87]
# num = int(input("Enter a number: "))

# while True:
#     if num in a:
#         a.remove(num)
#     else:
#         break
# print(a)

# a = [55, 44, 55, 75, 23, 29, 55, 87]
# b = []

# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
