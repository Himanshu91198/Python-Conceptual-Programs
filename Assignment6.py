""" Q1"""

# a = []
# for i in range(1, 11):
#     num = int(input("Enter a number: "))
#     a.append(num)
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

"""Q2"""

# a = []
# if len(a) == 0:
#     print("list is empty")
# else:
#     print("list is not empty")

"""Q3"""

# a = [2, 4, 5, 6, 8, 9]
# b = [3, 45, 8, 10, 7, 11]
# count = 0
# for i in a:
#     for j in b:
#         if j == i:
#             count = count + 1
# if count >= 1:
#     print("Yes")
# else:
#     print("No")

"""Q4"""

# a = []
# for i in range(1, 6):
#     num = int(input("Enter a  number: "))
#     a.append(num)
# for i in a:
#     if i % 2 != 0:
#         a.remove(i)
# print(a)


"""Q5"""

# a = [45, 4, 6, 8, 12, 7, 9, 15, 3, 5]
# for i in range(0, len(a)):
#     a.sort()
# print(f"{a[1]}")

"""Q6"""

# a = [45, 4, 6, 8, 12, 7, 9, 15, 3, 5]
# for i in range(0, len(a)):
#     a.sort()
#     a.reverse()
# print(f"{a[1]}")

"""Q7"""
# a = []
# b = []
# for i in range(0, 15):
#     num = int(input("Enter a number: "))
#     a.append(num)
# for i in a:
#     if a.count(i) > 3:
#         if i not in b:
#             print(f"Values count greater than 3 is {i}")
#             b.append(i)

"""Q8"""

# a = (24, 45, 32, "Himanshu", True)
# b = list(a)
# b.append(2.3)
# a = tuple(b)
# print(a)

"""Q9"""

# a = (1, 2, 3, 4, 2, 3, 5)
# b = []
# for i in a:
#     if a.count(i) > 1:
#         if i not in b:
#             print("Repeated number: ", i)
#             b.append(i)

"""Q10"""

# a = []
# b = []

# for i in range(0, 10):
#     num = int(input("Enter a number: "))
#     a.append(num)
# print(a)
# a.reverse()
# b = a.copy()
# print(b)

"""Q11"""

# a = []

# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     a.append(num)

# b = sum(a) / len(a)
# print(b)

"""Q12"""

# a = []
# b = []
# c = []

# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     a.append(num)
# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     b.append(num)
# print(a)
# print(b)
# merge = a + b
# c.extend(merge)
# print(c)

"""Q13"""

# a = []
# b = []
# c = []
# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     a.append(num)
# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     b.append(num)
# for i in a:
#     for j in b:
#         if j == i:
#             c.append(i)
# print(c)

"""Q14"""

# a = []
# for i in range(1, 6):
#     num = int(input(f"Enter a number {i}: "))
#     a.append(num)
# print(a[1] + a[-2])

"""Q15"""

# Append adds the element into the list at the last position by default.
# Extend adds the element and a list and makes a new list sort of merged list & extend also add the elements to the last position by default.
# Insert adds the element to the specified position only, as it needs two arguments position and the element.

a = [44, 32, 14, 56, 55, 11, 66, 47, 12]
count = 0
n1 = int(input("Enter number: "))
n2 = int(input("Enter number: "))

for i in range(0, len(a)):
    if a[i] > n1 and a[i] < n2:
        count += 1

if count > 0:
    print("yes")
else:
    print("no")


# a.sort()
# print(a[-2])
# a[0], a[-1] = a[-1], a[0]
# print(a)
