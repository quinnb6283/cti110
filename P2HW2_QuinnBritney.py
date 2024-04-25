#Britney Quinn
#04/19/2024
#P2HW2 
#Design a program that take user inputs and display results.


#user enters grades for each module

mod_list = [float(input('Enter grade for Module 1: ')),
            float(input('Enter grade for Module 2: ')),
            float(input('Enter grade for Module 3: ')),
            float(input('Enter grade for Module 4: ')),
            float(input('Enter grade for Module 5: ')),
            float(input('Enter grade for Module 6: '))
            ]


print ('-------------Results-------------')


#results displaying lowest and highest grades. results also display sum and average of grades

print (f'Lowest Grade:   {min(mod_list):.2f}')

print (f'Highest Grade:  {max(mod_list):.2f}')  

print (f'Sum of Grades:  {sum(mod_list):.2f}')

avg = sum(mod_list)/len(mod_list)

print (f'Average:        {avg:.2f}')



print ('----------------------------------')

