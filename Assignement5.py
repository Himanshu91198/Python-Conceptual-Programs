# a = [25, 12, 15, 84, 64, 32, 45]
# print(a[-1::-1])

# a = [25, 45, 65, "Himanshu", 25.21]
# b = [45, "Shashikant", 42.25, 12]
# c = [96, 36, "Auti", 65.1]
# d = a + b + c
# print(d)

# a = [25, 12, 15, 84, 64, 32, 45]
# b = len(a)
# if b % 2 == 0:
#     print("list is even")
# else:
#     print("list is odd")

# sum = 0
# a = [25, 12, 15, 84, 64, 32, 45]
# for i in range(0, 7):
#     if a[i] % 3 == 0:
#         sum += a[i]
# print(sum)

a = [23, -15, 36, -1, 98, 54, 35, -65, 78, 12, -32]
count1 = 0
count2 = 0

for i in range(0, len(a)):
    if a[i] >= 0:
        count1 += 1
    else:
        count2 += 1
print(f"Total count of positive numbers is {count1}")
print(f"Total count of negative numbers is {count2}")
