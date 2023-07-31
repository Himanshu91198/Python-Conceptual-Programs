"""
OOPs concept
1) Class:
It is a blueprint
Person -> age, gender, name

2) Objects
"""


class Abc:
    # Properties/Members
    a = 5
    b = 10

    # Methods
    def greet(self):
        print("This is a greet function")


x = Abc()  # Creating an object
print(x.a)
x.greet()
y = Abc()
print(y.a)
print(y.b)
y.greet()


# class Person:
#     name = ""
#     age = 0
#     gender = ""

#     def DisplayInfo(self):
#         print(f"My name is {self.name}")
#         print(f"My age is {self.age}")
#         print(f"My gender is {self.gender}")

#     def SetInfo(self):
#         self.name = input("Enter name: ")
#         self.age = int(input("Enter age: "))
#         self.gender = input("Enter gender: ")

#     def UpdatedAge(self):
#         self.age = int(input("Enter age: "))


# x = Person()
# x.SetInfo()
# x.DisplayInfo()
# x.UpdatedAge()
# x.DisplayInfo()

# from random import randint


# class Bank:
#     acc_no = randint(10000, 19999)
#     balance = 0
#     name = ""

#     def SetInfo(self):
#         self.name = input("Enter your name: ")

#     def DisplayInfo(self):
#         print(f"Your account number is {self.acc_no}")
#         print(f"Your Name is {self.name}")
#         print(f"Your Balance is {self.balance}")

#     def Deposit(self):
#         amt = int(input("Enter amount you want to deposit: "))
#         self.balance += amt

#     def DisplayBalance(self):
#         print(f"Your account balance is {self.balance}")

#     def Withdraw(self):
#         cash_out = int(input("Enter withdrawal amount: "))
#         if cash_out > self.balance:
#             print("Transaction Unsuccessful due to insufficient funds")
#         else:
#             self.balance -= cash_out
#             print(f"Remaining balance is {self.balance}")


# x = Bank()
# x.SetInfo()
# x.DisplayInfo()
# x.Deposit()
# x.Withdraw()


"""
1) Create account
2) View all accounts
3) Search account
4) Withdraw
5) Deposit
6) Exit
"""
from random import randint
import pickle


class Bank:
    acc_no = 0
    balance = 0
    name = ""

    def __init__(self):
        self.name = input("Enter your name: ")
        self.acc_no = randint(10000, 19999)

    def DisplayInfo(self):
        print(f"Your account number is {self.acc_no}")
        print(f"Your Name is {self.name}")
        print(f"Your Balance is {self.balance}")

    def Deposit(self):
        amt = int(input("Enter amount you want to deposit: "))
        self.balance += amt

    def DisplayBalance(self):
        print(f"Your account balance is {self.balance}")

    def Withdraw(self):
        cash_out = int(input("Enter withdrawal amount: "))
        if cash_out > self.balance:
            print("Transaction Unsuccessful due to insufficient funds")
        else:
            self.balance -= cash_out
            print(f"Remaining balance is {self.balance}")


def DumpData():
    with open("Banking.txt", "wb") as f:
        pickle.dump(accounts, f)


try:
    with open("Banking.txt", "rb") as f:
        accounts = pickle.load(f)
except:
    accounts = []


while True:
    print("1) Create account")
    print("2) View all accounts")
    print("3) Search account")
    print("4) Withdraw")
    print("5) Deposit")
    print("6) Exit")
    choice = int(input("Enter your option: "))
    if choice == 1:
        x = Bank()
        accounts.append(x)
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts present")
        else:
            for obj in accounts:
                obj.DisplayInfo()
    elif choice == 3:
        if len(accounts) == 0:
            print("No accounts present")
        else:
            search_acc_no = int(input("Enter a account you want to search: "))
            for obj in accounts:
                if obj.acc_no == search_acc_no:
                    obj.DisplayInfo()
    elif choice == 4:
        if len(accounts) == 0:
            print("No accounts Found")
        else:
            search_acc_no = int(
                input("Enter account no where you want to withdraw from: ")
            )
            for obj in accounts:
                if obj.acc_no == search_acc_no:
                    obj.Withdraw()
                    obj.DisplayBalance()
    elif choice == 5:
        if len(accounts) == 0:
            print("No Accounts found")
        else:
            search_acc_no = int(
                input("Enter account no where you want to Deposit into: ")
            )
            for obj in accounts:
                if obj.acc_no == search_acc_no:
                    obj.Deposit()
    if choice == 6:
        break
