"""
Change/Update
Delete/ Remove
"""


# my_dictionary = {
#     "name": "Himanshu",
#     "age": 24,
#     "gender": "male",
# }
# abc = my_dictionary.copy()
# my_dictionary.pop("name")
# print(abc)
# print(id(abc))
# print(id(my_dictionary))

# print(my_dictionary)
# # my_dictionary.pop("gender")
# # del my_dictionary["name"]
# my_dictionary.clear()
# print(my_dictionary)


# my_dictionary["gender"] = "female"
# my_dictionary.update({"name": "Aditi"})
# my_dictionary["marks"] = 44

result = {}
for i in range(0, 5):
    a = input("Enter subject name: ")
    b = int(input("Enter subject marks: "))
    result[a] = b
print(result)

# result = {}
# for i in range(1, 6):
#     a = i
#     b = i**3
#     result[a] = b
# print(result)

# result = {
#     "Himanshu": [54, 65, 95, 45, 78, 12],
#     "Aditi": [65, 89, 78, 45, 32, 45],
#     "Anirudh": [65, 87, 54, 87, 65, 87],
#     "Sagar": [45, 68, 45, 78, 52, 45],
#     "Nilima": [65, 94, 74, 46, 54, 69],
# }
# for k, v in result.items():
#     a = sum(v)
#     print(f"{k} = {a}")

# result = {
#     "Ani": "Orange",
#     "Chintu": "Orange",
#     "Nishant": "Pink",
#     "Ashu": "Black",
#     "Tom": "Green",
# }
# count = 0
# color = input("Enter a color: ")
# for k, v in result.items():
#     if v == color:
#         print(k)
#         count += 1
# print(count)


# result = {
#     "Ani": "Orange",
#     "Chintu": "Orange",
#     "Nishant": "Pink",
#     "Ashu": "Black",
#     "Tom": "Green",
#     "Sagar": "Violet",
#     "Srikant": "Purple",
#     "Harry": "Green",
# }
# a = []
# for v in result.values():
#     a.append(v)
#     b = set(a)
# print(b)
