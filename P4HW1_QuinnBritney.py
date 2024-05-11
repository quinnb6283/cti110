#Britney Quinn
#05/04/2024
#P4HW1
# A program that takes user input, creates list, and displays results.



#user inputs number of scores they want to enter 

num_score = int (input("How many scores do you want to enter? "))

score_set = []


#a loop to collect the number of scores the user wants to enter

for x in range (num_score):
    score = float (input("Enter score #"+str(x+1)+": "))



    while score < 0 or score > 100:
        print ('INVALID Score entered!!!!')
        print ('Score must be between 0 and 100')
        score = float (input("Enter score again #"+str(x+1)+": "))

#add scores to list        

    score_set.append(score)


print ('-------------Results-------------')


#results displayed lowest score

print (f'Lowest Score: {min(score_set):.2f}')

#drop lowest score from list

score_set.remove(min(score_set))


#display results for new list, average score, and then grade

print (f'Modified List: {(score_set)}')  

avg = sum(score_set)/len(score_set)

print (f'Scores Average: {avg:.2f}')

if avg >= 90:

    print ("Grade : A")

elif avg >= 80:

    print ("Grade : B")

elif avg >= 70:

    print ("Grade : C")

else:

    print ("Grade : F")


print ('----------------------------------')


