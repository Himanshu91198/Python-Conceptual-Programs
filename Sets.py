"""
SET
"""

# a = {32, 23, "Himanshu", 2.23, True, 23, 32, "Himanshu"}
# a.add("Auti")
# a.update(["Chair", 23.56, 32])
# a.remove("Himanshu")  # if element does not exist error will come
# a.discard(32)  # if element does not exist error will not come
# a.pop()  ## removes random numbers
# a.clear()
# print(a)
# print(type(a))

# a = [32, 56, 3, 15, 3, 56, 23, 23]
# c = list(set(a))
# print(c)

# a = {32, 23, "Himanshu", 2.23, True, 23, 32, "Himanshu"}
# b = {32, 56, 78, "Himanshu", 2.23}
# for i in a:
#     print(i, end=" ")

a = {32, 23, "Himanshu", 2.23, True, 23, 32, "Himanshu"}
b = {32, 56, 78, "Himanshu", 2.23}

# c = a.union(b)
# print(c)
# d = a.intersection(b)
# print(d)
# e = b - a
# print(e)
# e = a.symmetric_difference(b)
# print(e)

c = a.intersection(b)
print(len(c))
