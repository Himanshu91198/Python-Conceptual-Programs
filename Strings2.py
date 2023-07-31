"""
Mutable vs Immutable
"""

# a = "HEllo World"
# a = a.replace("o", "z")
# print(a)

# a = str(input("Type a Sentence: "))
# b = str(input("Type a letter: "))
# c = a.count(b)
# print(c)

a = "xxxyyyhimanshuauti98@gamil.com"
# # a = a.strip("xy")
a = a.index("a")
# # a = a.rindex("a")
print(a)
# a = list(a)
# print(a)

# a = "himanshuauti98@gamil.com"
# a = list(a)
# a.sort()
# print("".join(a))

# a = "himanshuauti98@gamil.com"
# a = list(a)
# a.sort()
# a.reverse()
# print("".join(a))

a = "Good Morning India is great"
a = a.split()
print(a)

# a = "Good Morning India is great good bye"
# a = a.split()
# b = a.reverse()
# print("".join(a))

a = "Good Morning India is great good bye"
b = a.split()
for i in b:
    c = i[-1::-1]
    print(c, end=" ")

# a = "Good Morning India is great good bye"
# a = list(a)
# b = {}

# for i in a:
#     for j in b:
#         if j == i:
