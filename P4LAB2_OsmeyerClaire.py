# Claire Osmeyer
# October 27, 2026
# P4LAB2
# Display a multiplication table and allow the user to run again.

'''
Get interger from user
Determine if interger is positive or negative
if number is postive, display multiplication table
if number is negative, tell user program cannot accept it
Ask user to run again?
If yes, run program again
If no, exit program
''' 

run_again = "yes"

while run_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values.")

    run_again = input("Would you like to run the program again? ")

# Loop has ended. User entered "no".
print("Program is ending... Goodbye!")