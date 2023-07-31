# without parameter and with return


# def xyz():
#     a = 10
#     b = 20
#     return a + b


# print(xyz())

# with parameter and with return


# def multiply(a, b, c):
#     return a * b * c


# x = multiply(4, 5, 6)
# print(x)
# y = multiply(10, 10, 10)
# print(y)


# a function to add 5 numbers
# addition is even or odd


# def add(a, b, c, d, e):
#     return a + b + c + d + e


# def check(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# total = add(45, 98, 65, 15, 32)
# print(total)
# check(total)

# # Write a python program to return the even numbers from a given list


# def allEven(a):
#     b = [i for i in a if i % 2 == 0]
#     return b


# x = allEven([66, 54, 12, 34, 44, 44, 41])
# print(x)

# # Make a function which accepts a string and return a string in uppercase


# def up(string):
#     string = string.upper()
#     return string


# a = input("Enter a string: ")
# x = up(a)
# print(x)


# Make a function that accepts a list
# Return the sum of list
# b = []
# for i in range(0, 5):
#     a = int(input("Enter a number: "))
#     b.append(a)


# def accept(list):
#     a = sum(list)
#     return a


# x = accept(b)
# print(x)

# Return the sum of even numbers in the list

b = []
for i in range(0, 5):
    a = int(input("Enter a number: "))
    b.append(a)


def accept(list):
    c = [i for i in list if i % 2 == 0]
    return c


def Addition(c):
    d = sum(c)
    return d


x = accept(b)
print(x)
y = Addition(x)
print(y)
