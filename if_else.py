# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are a adult")
# else:
#     print("You are a child")
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is less than {b}")
# else:
#     print("Both are equal")

# physics = 67
# chemistry = 44

# if physics > 33 and chemistry > 33:
#     print("pass")
# else:
#     print("fail")

age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult")
elif age > 14 and age < 17:
    print("You are a teen")
elif age > 1 and age < 13:
    print("You are a child")
else:
    print("Invalid age")
