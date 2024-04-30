#Britney Quinn
#04/16/2024
#P3HW2_SALARY
#Create a program that calculates emplyee's gross pay.


#ask the user to enter name of employee, hours worked, and play rate

name = input("Enter employee's name: ")

hours = float (input("Enter number of hours worked: "))

pay = float (input("Enter employee's pay rate: "))
 
print ("-------------------------------------------")

print ('Employee name:',name,'\n')


if hours > 40:

    ot = hours - 40

    ot_pay = pay * 1.5 * ot

    reg_pay = 40 * pay

    gross = ot_pay + reg_pay

else:

    ot =  ('0.0')
    ot_pay = ('0.0')

    reg_pay = 40 * pay

    gross = reg_pay

    

print ('Hours Worked   Pay Rate     OverTime      OverTime Pay      RegHour Pay          Gross Pay')

print ("-----------------------------------------------------------------------------------------------")
        
print (f'{hours}      {pay:10}      {ot:^10}       {ot_pay:^10}       {reg_pay:<10}         {gross:10}')


