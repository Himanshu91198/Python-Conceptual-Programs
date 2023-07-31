"""Q1"""

a = {"Name": "Himanshu"}
if len(a) == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")

"""Q2"""


def list(dict):
    a = [(k, v) for k, v in dict.items()]
    print(a)


my_dict = {
    "name": "Elon musk",
    "age": 66,
    "gender": "Male",
    "cars": 8,
    "married": True,
}
list(my_dict)

"""Q3"""

mystring = "This is a string"
mystring = mystring.split(" ")
mystring = "-".join(mystring)
print(mystring)


"""Q4"""

balls = int(input("Enter no.of balls bowled:  "))


def check(balls):
    if balls % 6 == 0:
        return balls / 6
    return balls % 6 / 10 + balls // 6


over = check(balls)
print(f"Total overs({balls} --> {over})")


"""Q5"""


def top_note(Dictionary):
    return {"name": Dictionary["name"], "top_note": max(Dictionary["notes"])}


x = top_note({"name": "John", "notes": [3, 4, 5]})
y = top_note({"name": "Max", "notes": [1, 4, 6]})
z = top_note({"name": "Zygmund", "notes": [1, 2, 3]})
print(x)
print(y)
print(z)
