"""Q1"""
# 1 Variable used inside a function becomes its
# a) Local variable

"""Q2"""


# def is_leap(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False


# year = int(input("Enter a year: "))
# x = is_leap(year)
# print(x)

"""Q3"""


# def palindrome(num):
#     a = num
#     b = 0
#     while num != 0:
#         dig = num % 10
#         b = b * 10 + dig
#         num = num // 10
#     if a == b:
#         print("The number is palindrome")
#     else:
#         print("The number is not palindrome")


# num = int(input("Enter a number: "))
# palindrome(num)

"""Q4"""


# def even_odd(num):
#     if num % 2 == 0:
#         return f"{num} is even"
#     else:
#         return f"{num} is odd"


# num = int(input("Enter a number: "))
# x = even_odd(num)
# print(x)
# print(type(x))


"""Q5"""


def check(string):
    count = 0
    for i in string:
        if (
            i == "a"
            or i == "i"
            or i == "o"
            or i == "e"
            or i == "u"
            or i == "A"
            or i == "I"
            or i == "O"
            or i == "E"
            or i == "U"
        ):
            count += 1
    print(
        f"Total numbers of vowels and consonants in {string} are {count} and {len(string)-count}"
    )


string = input("Enter a string: ")
check(string)
