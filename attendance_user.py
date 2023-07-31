class_held = int(input("Enter no. of classes held : "))
class_attended = int(input("Enter no. of classes attended : "))
percentage = (class_attended / class_held) * 100
if percentage <= 75:
    print("You are not allowed to sit in the exam")
else:
    print("You are allowed to sit in the exam")
