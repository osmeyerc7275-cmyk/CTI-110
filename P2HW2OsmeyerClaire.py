#Claire Osmeyer
#September 25, 2026
#P2HW2
#Enter six module grades and display the lowest, highest, sum, and average.

"""
Pseudocode:
1. Ask the user to enter each of the six module grades separately.
2. Convert each grade to a float so decimal grades are allowed.
3. Store all six grades in a descriptive list called module_grades.
4. Find the lowest grade, highest grade, and sum using the list.
5. Divide the sum by the number of grades to calculate the average.
6. Display aligned results with the average formatted to two decimal places.
"""

module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("----------------------------------------")