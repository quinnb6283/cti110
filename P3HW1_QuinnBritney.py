#Britney Quinn
#04/19/2024
#P3HW1
#Correct the program and complete it.


# I was supposed to put a comment here
# My Last Name

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest , sum and average for grades


print ('-------------Results-------------')


low = min(grades)
high = max(grades)
add = sum(grades)
avg = sum(grades)/len(grades)


print (f'Lowest Grade:  {low :.2f}')

print (f'Highest Grade: {high :.2f}')  

print (f'Sum of Grades: {add :.2f}')

print (f'Average:       {avg :.2f}')

 
# determine letter grade for average

print ('----------------------------------')



if avg >= 90:
    print('Your grade is: A')

elif avg > 80:
    print('Your grade is: B')
              
else:
    print('Your grade is: F') 





