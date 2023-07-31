"""Q1"""

student = {
    "Himanshu": [65, 89, 96, 45, 78],
    "Rohan": [78, 85, 68, 98, 47],
    "Aditya": [85, 98, 65, 47, 58],
    "Sagar": [87, 85, 65, 86, 54],
    "Anirudh": [98, 65, 78, 58, 75],
}
for k, v in student.items():
    print(f"{sum(v)} and {(sum(v)/500)*100} are total marks and percentage of {k}")

"""Q2"""

student = {
    "Himanshu": [65, 89, 96, 45, 78],
    "Rohan": [78, 85, 68, 98, 47],
    "Aditya": [85, 98, 65, 47, 58],
    "Sagar": [87, 85, 65, 86, 54],
    "Anirudh": [98, 65, 78, 58, 75],
}
a = []
for v in student.values():
    a.append(sum(v))
    a.sort()
print(a[-1])

"""Q3"""

student = {
    "Himanshu": [65, 89, 96, 45, 78],
    "Rohan": [78, 85, 68, 98, 47],
    "Aditya": [85, 98, 65, 47, 58],
    "Sagar": [87, 85, 65, 86, 54],
    "Anirudh": [98, 65, 78, 58, 75],
}
a = []
for v in student.values():
    a.append(sum(v))
    a.sort()
print(a)

"""Q4"""

student = {
    "Himanshu": [65, 89, 96, 45, 78],
    "Rohan": [78, 85, 68, 98, 47],
    "Aditya": [85, 98, 65, 47, 58],
    "Sagar": [87, 85, 65, 86, 54],
    "Anirudh": [98, 65, 78, 58, 75],
}
for v in student.values():
    v.sort()
    print(v[-1])
