# a = (23, 56, 45, "Himanshu", "Auti", True)
# print(a)
# print(type(a))
# print(a.index(56))
# print(a.count(45))
# print(a.sort())
# print(a.reverse())

# a = (23, 56, 45) * 5
# b = (23, 56, 45)
# c = a + b
# print(c)
# print(a)

# a = (55, 33, 22, 11, 56, 89, 54, 54)
# for i in range(0, len(a)):
#     print(a[i])

# a = (55, 33, 22, 11, 56, 89, 54, 54)
# b = list(a)
# b.sort()
# print(b)
# print(type(b))
# a = tuple(b)
# print(a)

# a = (55, 33, 22, 11, 56, 89, 54, 54)
# b = list(a)
# b.sort()
# b.reverse()
# print(b)

a = (55, 33, 22, 11, 56, 89, 54, 54)
b = list(a)
for i in range(0, len(b)):
    b[i] += 10
a = tuple(b)
print(a)
print(type(a))
