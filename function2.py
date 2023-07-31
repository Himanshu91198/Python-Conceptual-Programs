# def addition():
#     # Local scope
#     a = 10
#     b = 20
#     print(a + b)


# addition()
# print(a)


def greet(name, age, gender, p, c, b):
    print(f"Hello {name}")
    print(f"Your {age}")
    print(f"Your {gender}")
    print(b + c + p)


greet(age=24, p=68, gender="male", c=85, name="Himanshu", b=65)


def addition(num1, num2, num3):

    print(num1 + num2 + num3)


# Named Arguments
addition(num3=54, num1=87, num2=65)


def addition(num3, num1=0, num2=0):
    print(num1 + num2 + num3)


addition(num3=21)
