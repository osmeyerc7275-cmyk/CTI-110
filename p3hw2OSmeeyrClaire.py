#Claire Osmeyer
#10/13/2026
#P3HW2
#Salary calculator 

 #request employee info 
name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40:
    overtime_hours = hours - 40
    #calculate overtime pay
    overtime_pay = overtime_hours * (rate * 1.5)
    #calculate regular pay
    regular_pay = 40 * rate
    #calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    gross_pay = hours * rate

    #Display results
print("-----------------------------")
print("Employee Name:", name)
print(f'{"Hours Worked":<15}{"pay Rate":<12}{"Overtime pay":<12}{"Regular Pay":<15}{"Gross Pay":<12}')
print("-----------------------------")
print(f'{hours:<15}{rate:<12.2f}{overtime_pay:<12.2f}{regular_pay:<15.2f}{gross_pay:<12.2f}')


