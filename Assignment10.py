"""Q1"""

my_list = ["anirudh", "khurana", "sagar", "bhanu", "ankit", "himanshu"]
my_list2 = [58, 74, 71, 41, 42, 58]
result = {}
result[my_list] = [my_list2]    #####
print(result)

"""Q2"""

# a = {
#     "physics": 88,
#     "chemistry": 78,
#     "maths": 80,
#     "english": 68,
#     "science": 65,
# }
# student = {
#     "Himanshu": [65, 89, 96, 45, 78],
#     "Rohan": [78, 85, 68, 98, 47],
#     "Aditya": [85, 98, 65, 47, 58],
#     "Sagar": [87, 85, 65, 86, 54],
#     "Anirudh": [98, 65, 78, 58, 75],
# }
# a.update(student)
# print(a)

"""Q3"""

# a = {
#     "physics": 88,
#     "chemistry": 78,
#     "maths": 80,
#     "english": 68,
#     "science": 65,
# }
# total = 0
# user = input("Enter a key: ")
# for k in a.keys():
#     if k == user:
#         total += 1
# if total > 0:
#     print("Key Exists")
# else:
#     print("Key Does Not Exist")

"""Q4"""

# result = {}
# a = []
# for i in range(0, 5):
#     name = input("Enter a name: ")
#     age = int(input("Enter a value: "))
#     result[name] = age
# for v in result.values():
#     a.append(v)
#     a.sort()
# print(f"maximum value is {a[-1]} and minimum value is {a[0]}")

"""Q5"""

# vehicles = {
#     "car": 2000,
#     "Bike": 200,
#     "Truck": 5500,
#     "Bus": 4000,
#     "Rickshaw": 1500,
#     "Train": 10000,
#     "Aeroplane": 20000,
# }
# v = [k.upper() for k, v in vehicles.items() if v < 5000]
# print(v)

"""Q6"""

# It will print a list of each letter in HELLO all in lowercase.
