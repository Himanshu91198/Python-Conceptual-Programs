import random

user_choice = input("Enter your choice (Rock , Papper, Scissor) = ")
comp_choice = random.choice(["Rock", "Papper", "Scissor"])

print(user_choice,comp_choice)

if user_choice == comp_choice:
    print("Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Scissor":
        print("Rock smashes Scissor You won!")
    else:
        print("Paper covers rock Comp won!")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers rock You won!")
    else:
        print("Scissor cuts Paper Comp won!")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper You won!")
    else:
        print("Rock smashes Scissor Comp won!")
