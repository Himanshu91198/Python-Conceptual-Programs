abc = [66, 77, 54, 34, 55]
result = []
for i in abc:
    result.append(i)
print(result)

abc = [66, 77, 54, 34, 55]
result = ["Hello" for i in abc]
print(result)

a = [i for i in range(0, 11)]
print(a)

my_list = [i for i in range(0, 31) if i % 7 == 0]
print(my_list)

my_list = [i for i in range(0, 31) if i % 2 == 0 & i % 3 == 0]
print(my_list)

my_list = ["anirudh", "khurana", "sagar", "bhanu", "ankit", "himanshu"]

my_list2 = [i.upper() for i in my_list]
print(my_list2)

my_list = [58, 74, 71, 41, 42, 58, 97, 85, 84, 81]
my_list2 = ["even" if i % 2 == 0 else "odd" for i in my_list]
print(my_list2)

my_list = [85, 74, 24, 52, 13]
my_list2 = ["pass" if i > 33 else "fail" for i in my_list]
print(my_list2)

my_list = [85, 74, 24, 52, 13]
my_list2 = len([i for i in my_list if i > 33])
print(my_list2)

my_list = ["anirudh", "khurana", "sagar", "bhanu", "ankit", "himanshu"]
my_list2 = [i[-1::-1] for i in my_list]
print(my_list2)

a = {
    "anirudh": 77,
    "sanjay": 22,
    "sagar": 88,
    "xyz": 11,
}
result = [k for k, v in a.items() if v > 33]
print(result)

a = ["anirudh", "khurana", "sagar", "bhanu", "ankit", "himanshu"]
my_list = [i for i in a if i.count("i") > 0]
print(my_list)
