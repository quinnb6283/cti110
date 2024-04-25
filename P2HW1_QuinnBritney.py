#Britney Quinn
#04/16/2024
#P2HW1
#Change how results are displayed.




print ("This program calculates and displays travel expenses \n")


bud = int (input("Enter Budget: "))

print ('')

des = (input("Enter your travel destination: "))

print ('')

gas = int (input("How much do you think you will spend on gas? "))

print ('')

hotel = int (input("Approximately, how much will you need for accomodation/hotel? "))

print ('')

food = int (input("Last, how much do you need for food? "))


print ("----------Travel Expenses----------")

print ('Location:         ',des)
print (f'Initial Budget:    ${bud:.2f}')
print (f'Fuel:              ${gas :.2f}')
print (f'Accomodation:      ${hotel :.2f}')
print (f'Food:              ${food :.2f}')

print ("-----------------------------------")

sub = bud - gas - hotel - food

print (f"Remaining Balance: ${sub:.2f}")
