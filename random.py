import random

user = int(input("Enter your number (1,2,3,4,5)"))
comp = random.choice([1,2,3,4,5])

print(user,comp)

if user == comp:
    print("The Number entered are same")
else:
    print("The Number entered are different")