# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 7 - i):
#         print(j, end=" ")
#     print()

# a = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(a, end=" ")
#         a += 1

#     print()

# a = 1
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(a, end=" ")
#         a += 2
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         if j % 2 == 0:
#             print("2", end=" ")
#         else:
#             print("1", end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")
#     for k in range(1, i + 1):
#         print("*", end=" ")
#     print()
a = 1
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(a, end=" ")
    a += 1
    print()
