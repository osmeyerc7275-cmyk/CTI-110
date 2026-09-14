#Claire Osmeyer
#September 11 2026
#P1hW1
#Calculating exponents and adding and subtracting

#Calculates exponent

print ("--------Exponent Calculator--------")
print()

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

#Calculates addition and subtraction
print(("--------Addition and Subtraction Calculator--------"))
print()

num1 = int(input("Enter the starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")