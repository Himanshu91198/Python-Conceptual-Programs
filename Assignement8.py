"""Q1"""

# a = {
#     "maths": 87,
#     "science": 77,
#     "english": 98,
#     "history": 86,
#     "computer": 88,
# }
# total = 0
# for i in a.values():
#     total += i
# print(f"total of all the values is {total}")

"""Q2"""
# student = {
#     "Himanshu": [65, 89, 96, 45, 78],
#     "Rohan": [78, 85, 68, 98, 47],
#     "Aditya": [85, 98, 65, 47, 58],
#     "Sagar": [87, 85, 65, 86, 54],
#     "Anirudh": [98, 65, 78, 58, 75],
# }

# for k, v in student.items():
#     print(f"sum and percentage of marks are {sum(v)} & {(sum(v)/500)*100} respectively")


# result = {}


# for i in range(0, 5):
#     name = input("Enter a name: ")
#     marks = []
#     for j in range(0, 5):
#         value = int(input("Enter marks: "))
#         marks.append(value)
#     result[name] = marks
# print(result)

"""Q3"""

# marks = {
#     "English": 88,
#     "Maths": 87,
#     "History": 78,
#     "Physics": 89,
#     "Chemistry": 85,
# }
# a = []
# for v in marks.values():
#     a.append(v)
#     a.sort()
# print(f"Second highest marks is {a[-2]}")

"""Q4"""

# marks = {
#     "English": 88,
#     "Maths": 87,
#     "History": 78,
#     "Physics": 89,
#     "Chemistry": 85,
# }
# a = []
# for v in marks.values():
#     a.append(v)
#     a.sort()
# print(a)

"""Q5"""

# marks = {
#     "English": 88,
#     "Maths": 87,
#     "History": 78,
#     "Physics": 89,
#     "Chemistry": 85,
# }
# user = input("Enter name of subject: ")
# for k, v in marks.items():
#     if k == user:
#         print(v)
#     else:
#         print("Invalid")
