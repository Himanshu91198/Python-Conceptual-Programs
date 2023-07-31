"""
FILE HANDLING
3 Modes:
Read (r)
Write(w)
Append(a)
"""
# try:
#     f = open("hello.txt", "r")
#     r = f.readlines()
#     a = len(r)
#     print(r)
#     print(a)
#     f.close
# except FileNotFoundError:
#     print("File does not exist")
# except:
#     print("Someother error occured")


# try:
#     f = open("hello.txt", "r")
#     r = f.readline()
#     print(r)
#     r = f.readline()
#     print(r)
#     f.close
# except FileNotFoundError:
#     print("File does not exist")
# except:
#     print("Someother error occured")


# try:
#     f = open("hello.txt", "r")
#     r = f.read()
#     result = r.split()
#     print(result)
#     print(f"No. of words {len(result)}")
#     f.close
# except FileNotFoundError:
#     print("File does not exist")
# except:
#     print("Someother error occured")


# f = open("hello.txt", "r")
# r = f.read()
# print(r.count("a"))

"""
Write (w)
"""
f = open("hello.txt", "w")
f.write("Himanshu Auti\n")
f.write("Good Morning")
f.close()


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# details = open("hello.txt", "a")
# details.write(f"My name is {name}\n")
# details.write(f"My age is {age}\n")
# details.write(f"Your gender is {gender}\n")
# details.close()

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")

# with open("hello.txt", "w") as details:
#     details.write(f"My name is {name}\n")
#     details.write(f"My age is {age}\n")
#     details.write(f"Your gender is {gender}\n")


# f = open("hello.txt", "r")
# read = f.read()
# details = open("hello1.txt", "w")
# details.write(read)
# details.close()

"""OR"""
# file1 = input("Enter your file name: ")
# file2 = input("Enter your file to paste in it: ")
# with open(file1, "r") as f:
#     data = f.read()

# with open(file2, "w") as details:
#     details.write(data)
"""""" ""

# my_dict = {"Anirudh": 89, "Sagar": 99, "Elon": 41, "xyz": 57}

# with open("Hello4.txt", "w") as f:
#     for k, v in my_dict.items():
#         f.write(f"{k} -> {v}\n")

"""""" ""

# my_dict = {
#     "Anirudh": [87, 98, 65, 32, 45],
#     "Sagar": [87, 91, 54, 32, 87],
#     "Elon": [78, 66, 30, 42, 87],
#     "XYZ": [77, 23, 65, 12, 78],
# }

# with open("Hello5.txt", "w") as f:
#     for k, v in my_dict.items():
#         a = " ".join(str(i) for i in v)
#         f.write(f"{k} -> {a} {sum(v)}\n")
"""""" ""


# my_dict = {
#     "Anirudh": [87, 98, 65, 32, 45],
#     "Sagar": [87, 91, 54, 32, 87],
#     "Elon": [78, 66, 30, 42, 87],
#     "XYZ": [77, 23, 65, 12, 78],
# }

# with open("Hello5.txt","w") as f:
#     for
