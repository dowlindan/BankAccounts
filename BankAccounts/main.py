# Purpose: Uses BankAccount objects to simulate transactions
# Author: Dan Dowlin
# Purpose: 4/30/2023

from bank import *

# Uses input validation for a positive float value
def promptForPosFloat():
    while True:
        try:
            user_input = float(input())
            if user_input < 0:
                print("Enter a greater than or equal to zero: ")
                continue
            return user_input
        except:
            print("Invalid input: an float value was expected. Try again: ")

# Uses input validation for a positive int value
def promptForPosInt():
    while True:
        try:
            user_input = int(input())
            if user_input < 0:
                print("Enter a greater than or equal to zero: ")
                continue
            return user_input
        except:
            print("Invalid input: an integer value was expected. Try again: ")

if __name__ == "__main__":
    # Create empty list of bank accounts
    bankAccounts = [] 

    while True:
        # Prompts for number 1-9 from user
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Perform End of Month Operations")
        print("6. Display Savings Accounts")
        print("7. Display Checking Accounts")
        print("8. Display All Accounts")
        print("9. Exit")
        print("Enter your choice: ")
        user_input = input()

        # Create Savings Acc from User Input and adds it to the list of bank accounts
        if user_input == '1':
            print("Savings Account")
            name = input("Enter owner's name: ")
            print("Enter initial balance: ", end = '')
            bal = promptForPosFloat()

            newSavingsAcc = Savings(name, bal)
            bankAccounts.append(newSavingsAcc)
            print("Account added")
        #Creates Checking Account from User Input and adds it to the list of bank accounts
        elif user_input == '2':
            print("Checking Account")
            name = input("Enter owner's name: ")
            print("Enter initial balance: ", end = '')
            bal = promptForPosFloat()

            newCheckingAcc = Checking(name, bal)
            bankAccounts.append(newCheckingAcc)
            print("Account added")
        # Deposit into a bank account
        elif user_input == '3':
            print("Deposit")
            print("Enter account number: ", end = '')
            # Prompts an integer for potential account number between 0 and max int limit
            accNum = promptForPosInt()
            accFound = False
            # Iterates through each acc
            for acc in bankAccounts:
                if acc.getAccountNumber() == accNum:
                    accFound = True
                    print("Enter amount to deposit: ", end = '')
                    amount = promptForPosFloat()
                    acc.deposit(amount)

            if not accFound:
                print("That account number does not exist")
        # Withdraw from bank account
        elif user_input == '4':
            print("Withdraw")
            print("Enter account number: ", end = '')
            accNum = promptForPosInt()
            accFound = False

            for acc in bankAccounts:
                if acc.getAccountNumber() == accNum:
                    accFound = True
                    print("Enter amount to withdraw: ", end = '')
                    amount = promptForPosFloat()
                    # Do not withdraw if amount is greater than balance or if it would result in a negative balance
                    if amount > acc.getBalance():
                        print("You do not have enough funds")
                    else:
                        acc.withdraw(amount)
 
            if not accFound:
                print("That account number does not exist")
        # Performs all end of month operations
        elif user_input == '5':
            for bank in bankAccounts:
                bank.endOfMonth()
            print("End of month operations have been performed")
        # Prints all savings
        elif user_input == '6':
            for bank in bankAccounts:
                if isinstance(bank, Savings): # if the account is a savings account, print it
                    print(bank)
        # Prints all checking
        elif user_input == '7':
            for bank in bankAccounts:
                if isinstance(bank, Checking):
                    print(bank)
        # Prints all banks
        elif user_input == '8':
            for bank in bankAccounts:
                print(bank)
        # Breaks out of input loop
        elif user_input == '9':
            break
        else:
            print("Invalid choice. Try again.")

    print("Good-Bye!")
                    


