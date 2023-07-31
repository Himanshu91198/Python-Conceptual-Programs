"""Q1"""

# a = input("Enter a sentence: ")
# b = input("Enter a letter: ")
# c = a.replace(b, "")
# print(c)

"""Q2"""

# a = input("Enter a word: ")
# a = list(a)
# b = a.reverse()
# if a == b:
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")

# a = input("Enter a word: ")

# if a[0:10] == a[-1::-1]:
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")


"""Q3"""

# # 1)
# user = input("Enter a string: ")
# a = len(user)
# print(a)

# # 2)
# user = input("Enter a string: ")
# count = 0
# for i in user:
#     count += 1

# print(count)

# # 3)
# user = input("Enter a string: ")
# count = 0
# while user[0:]:
#     count += 1
# print(count)

"""Q4"""

# user = input("Enter a string: ")

# if user.isalnum():
#     print("Yes")    ####
# else:
#     print("No")

"""Q5"""

# user = input("Enter a sentence: ")
# a = user.split()
# for word in a:
#     b = len(word)
#     if len(word) > 5:
#         print(word)

"""Q6"""

# a = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
# user = input("Enter a string: ")
# b = set(user)
# c = a.intersection(b)
# print(len(c))


"""Q7"""

# user = input("Enter a sentence: ")
# a = user.split()
# b = max(a)
# print(f"Longest word is {b} and Length is {len(b)}")

"""Q8"""

# user = input("Enter a sentence: ")
# user = user.split()
# count = 0
# for word in user:
#     count += 1
# print(count)

"""Q9"""

# user = input("Enter a comma separated sequence of words: ")
# a = user.split(",")
# a.sort()                #####
# a = ",".join(user)
# print(a)

"""Q10"""

# a = "hiMAnshu"
# count = 0
# for i in a[:4]:
#     if i.upper() == i:
#         count += 1
# if count >= 2:
#     a = a.upper()
# print(a)

"""Q11"""

# user = input("Enter a string: ")
# for letter in user:
#     print(f"Current character {letter} position at {user.index(letter)}")

"""Q12"""

user1 = input("Enter a sentence: ")
user2 = input("Enter a sentence: ")
user1 = user1.split()
user2 = user2.split()
a = set(user1)
b = set(user2)
c = a.intersection(b)
c = list(c)
print(c)
