#To calculate the total amount of electricity
unit = int(input("Enter the number of units ="))

if unit <= 50:
    print("Total amount of electricity bill is =", unit*10)

elif unit > 50 and unit <= 100:
    print("Total amount of electricity bill is =", unit*18)

elif unit > 100 and unit <= 150:
    print("Total amount of electricity bill is =", unit*25)

elif unit <150 and unit <= 200:
    print("Total amount of electricity bill is =", unit*40)

else:
    print("Total amount of electricity bill is =", unit*65)    
