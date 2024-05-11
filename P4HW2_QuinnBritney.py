#Britney Quinn
#05/04/2024
#P4HW2 
#Create a program that calculates gross pay for multiple employees determined by user.




#ask the user to enter name of employee, hours worked, and pay rate

total_emp = 0
total_ot = 0
total_reghrs = 0
total_gross = 0

name = input("Enter employee's name or \"Done\" to terminate: ")

while name != 'Done':

    total_emp += 1

    hours = float(input("How many hours did " + name + " work? "))
    pay = float(input("What is " + name + "'s pay rate? "))

#calculate hours, overtime, regular and overtime pay
    if hours > 40:
        ot = hours - 40
        ot_pay = pay * 1.5 * ot
        reg_pay = 40 * pay
        gross = ot_pay + reg_pay
    else:
        ot = 0.0
        ot_pay = 0.0
        reg_pay = hours * pay
        gross = reg_pay

    total_ot += ot_pay
    total_reghrs += reg_pay
    total_gross += gross

#display user input results
    
    print (f'{"Hours Worked":<16}{"Pay Rate":<13}{"OverTime":<13}{"OverTime Pay":<16}{"RegHour Pay":<15}{"Gross Pay"}')

    print ("-----------------------------------------------------------------------------------------------")

    print (f'{hours:<16}{pay:<13}{ot:<13}{ot_pay:<16}${reg_pay:<15}${gross}')

    name = input("Enter employee's name or \"Done\" to terminate: ")


print('\n')

#display total number of employees and their combined overtime, regular hours, and gross.

print("Total number of employees entered: ", total_emp)
print(f"Total amount paid for overtime: ${total_ot:.2f}")
print(f"Total amount paid for regular hours: ${total_reghrs:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")



        




