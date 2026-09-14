# Claire Osmeyer
# September 13, 2026
# P1HW2 - Travel Expense
# This program calculates travel expenses and displays the remaining budget.

# Pseudocode:
# Ask the user to enter their budget
# Ask the user to enter their travel destination
# Ask the user how much they will spend on gas
# Ask the user how much they will spend on accommodation
# Ask the user how much they will spend on food
# Add gas, accommodation, and food to calculate total expenses
# Subtract total expenses from the budget
# Display the travel destination, expenses, and remaining balance

print("This program calculates and displays travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

expenses = gas + accommodation + food
remaining_balance = budget - expenses

print()
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)