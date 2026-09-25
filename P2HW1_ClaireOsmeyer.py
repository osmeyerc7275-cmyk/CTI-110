# Claire Osmeyer
# 9/25/2023
# P2HW1 - Travel Expenses
# Calculate travel expenses and display aligned currency amounts.

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - gas - hotel - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${hotel:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':<20}${remaining_balance:.2f}")