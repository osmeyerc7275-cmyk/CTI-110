# Claire Osmeyer
# 10/27/2026
# P3HW2
# Salary calculator with loops

# Create accumulator variables.
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

# Request the first employee's name.
name = input("Enter employee's name or 'done' to finish: ")

while name != 'done':
    # Add one to the employee count.
    employee_count += 1

    # Ask for employee information.
    hours = float(input("How many hours did " + name + " work this week? "))
    rate = float(input("What is " + name + "'s hourly pay rate? "))

    # Calculate overtime and regular pay.
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate

    # Calculate gross pay.
    gross_pay = regular_pay + overtime_pay

    # Add this employee's pay to the totals.
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display this employee's results.
    print("-----------------------------")
    print("Employee Name:", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("-----------------------------")
    print(f'{hours:<15}{rate:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<12.2f}')

    # Ask for the next employee or "done" before repeating.
    name = input("\nEnter employee's name or 'done' to finish: ")

# Display totals after the user enters "done".
print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime pay: $", format(overtimepay_total, '.2f'))
print("Total amount paid for regular pay: $", format(regularpay_total, '.2f'))
print("Total amount paid for gross pay: $", format(grosspay_total, '.2f'))