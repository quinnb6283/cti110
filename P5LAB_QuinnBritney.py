#Britney Quinn
#05/10/2024
#P5LAB
#This program will simulate a customer using a self-checkout machine.





import random

def main():

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    print("You owe $"+str(amount_owed))
    
    cash = int(input("How much cash will you put in the self-checkout? "))
    
    change = cash - amount_owed
    
    print(f'Change is: ${change:.2f}')

    disperse_change(change)

    
 

def disperse_change(change):
    dollar = int(change)
    change -= dollar

    quarter = int(change / 0.25)
    change -= quarter * 0.25

    dime = int(change / 0.10)
    change -= dime * 0.10

    nickel = int(change / 0.05)
    change -= nickel * 0.05

    penny = round(change * 100)

    if dollar:
        print(dollar, end='')
        if dollar == 1:
            print(' Dollar')
        else:
            print(' Dollars')

    if quarter:
        print(quarter, end='')
        if quarter == 1:
            print(' Quarter')
        else:
            print(' Quarters')

    if dime:
        print(dime, end='')
        if dime == 1:
            print(' Dime')
        else:
            print(' Dimes')

    if nickel:
        print(nickel, end='')
        if nickel == 1:
            print(' Nickel')
        else:
            print(' Nickels')

    if penny:
        print(penny, end='')
        if penny == 1:
            print(' Penny')
        else:
            print(' Pennies')

if __name__ == "__main__":
    main()
