#Claire Osmeyer
#10/12/2026 
#P3lab

#get vaule from user
change =   float(input("Eneter the amount of money: $"))

print(f"Change Amount: {change}")

#converting the vaule to an interger
change = int(change * 100)

print(f"Change Amount: {change}")

#Determine how many dollars are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5) 

num_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else:
        print(f"{num_dollars} dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else:
        print(f"{num_quarters} quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else:
        print(f"{num_dimes} dimes")

if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    else:
        print(f"{num_nickels} nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} pennies")
