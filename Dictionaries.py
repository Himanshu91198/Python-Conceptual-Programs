"""
Dictionary (Mutable,Changeable) On-ordered
Key-Value
Fetch
"""
a = {
    "name": "Himanshu",
    "age": 24,
    "gender": "male",
    "physics": 88,
    "chemistry": 88,
    "adult": True,
    "maths": 56,
    "parents": ["xyz", "abc"],
}
b = a.get("name")
print(b)

if a.get("name") == None:
    print("No")
else:
    print("Yes")


# print(a)
# # print(type(a))

b = a["physics"]
c = a["chemistry"]
d = a["maths"]
e = b + c + d
print(e)


my_dictionary = {
    True: "Himanshu",
    10: "Auti",
    "age": 24,
}
print(my_dictionary)


a = dict(name="Himanshu", age=24, gender="Male")
print(a)

a = {"name": "Himanshu", "marks": [56, 68, 89, 54, 75]}
b = a.get("marks")
c = a.get("name")
print(f"{c} has got {sum(b)}")

a = {
    "physics": 88,
    "chemistry": 78,
    "maths": 80,
    "english": 68,
    "science": 65,
}

# print(a.keys())
# print(a.values())
# print(a.items())

# total = 0
# for i in a.values():
#     total += i
# print(total)

# for i in a.items():
#     print("->".join(i))

for k, v in a.items():
    print(f"{k} -> {v}")
