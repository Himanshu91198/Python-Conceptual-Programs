import random

marks = int(input("Enter your marks ="))
rank = int(input("Enter your rank ="))
college = input("Enter your group =")

if (marks>=60 and marks<= 100) and (rank<=100 and rank>=1) and college == "pcm": 
    print("You are eligible for admission")
else:
    print("You are not eligible for admission")
