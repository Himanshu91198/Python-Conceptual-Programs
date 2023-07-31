# FOR LOOP

# for i in range(1, 11):
#     print(i)

# for i in range(20, 31):
#     print(i)

# for h in range(1, 21, 3):
#     print(h)
# for i in range(10, 0, -1):
#     print(i)
# for i in range(10, -11, -1):
#     print(i)
# for x in range(1, 16):
#     if x % 2 == 0:
#         print(x)
# product = 1
# for i in range(1, 11):
#     product *= i

# print(product)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start, end):
    print(i)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start, end):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
total = 0
for i in range(start, end):
    if i % 4 == 0:
        total += i
    i += 1
print(total)

product = 1
for a in range(1, 11):
    product *= a
    a += 1
print(product)

a = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{a} X {i} = {a*i}")
    i += 1

count = 0
for i in range(20, 71):
    if i % 4 == 0:
        count += 1
print(count)

num = int(input("Enter a number: "))
count = 0
i = 1
for j in range(num, 0, -1):
    if num % i == 0:
        count += 1
    i += 1

if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")
