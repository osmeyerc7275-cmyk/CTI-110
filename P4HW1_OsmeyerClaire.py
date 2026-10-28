# Claire Osmeyer
# October 27, 2026
# P4HW1
# Collect scores, drop the lowest score, and calculate an average and grade.

# Pseudocode:
# Ask the user how many scores they want to enter.
# While the number of scores is less than two:
#     Explain that at least two scores are required.
#     Ask for the number of scores again.
# Create an empty list to store valid scores.
# Loop for the number of scores requested:
#     Ask the user to enter a score.
#     While the score is less than 0 or greater than 100:
#         Display an invalid-score message.
#         Ask the user to enter that score again.
#     Add the valid score to the list.
# Find and store the lowest score.
# Remove the lowest score from the list once.
# Calculate the average by dividing the sum of the remaining
# scores by the number of remaining scores.
# If the average is 90 or higher, assign A.
# Otherwise, if the average is 80 or higher, assign B.
# Otherwise, if the average is 70 or higher, assign C.
# Otherwise, if the average is 60 or higher, assign D.
# Otherwise, assign F.
# Display the lowest score, modified score list, average,
# and letter grade.

# Claire Osmeyer
# October 27, 2026
# P4HW1
# Collect scores, drop the lowest score, and calculate an average and grade.

# Ask the user how many scores they want to enter.
num_scores = int(input("How many scores do you want to enter? "))

# Require at least two scores so one can be dropped.
while num_scores < 2:
    print("Please enter at least two scores.")
    num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store valid scores.
score_list = []

# Repeat score entry for the number of scores requested.
for item in range(1, num_scores + 1):
    score = float(input(f"Enter score #{item}: "))

    # Reject scores outside 0 through 100 and ask again.
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{item} again: "))

    # Add the valid score to the list.
    score_list.append(score)

# Find the lowest score and remove it once from the list.
lowest_score = min(score_list)
score_list.remove(lowest_score)

# Calculate the average of the remaining scores.
average = sum(score_list) / len(score_list)

# Determine the letter grade based on the average.
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the lowest score, modified list, average, and grade.
print("\n------------Results------------")
print("Claire Osmeyer")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {letter_grade}")
print("----------------------------------")