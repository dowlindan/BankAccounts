# Purpose: Bank Account Objects to simulate real world accounts
# Author: Dan Dowlin
# Version 4/30/2023

from abc import ABC, abstractmethod


class BankAccount(ABC):
    __nextAccountNumber = 1000

    def __init__(self, owner, balance = 0.0):
        self.__owner = owner
        self.__balance = balance
        self.__accountNumber = BankAccount.getNextAccountNumber()

    def getOwner(self):
        return self.__owner

    def getBalance(self):
        return self.__balance

    def getAccountNumber(self):
        return self.__accountNumber

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __eq__(self, other):
        return self.getOwner() == other.getOwner() and self.getBalance() == other.getBalance() and self.getAccountNumber() == other.getAccountNumber()

    def __str__(self):
        string = "Account Number: " + str(self.__accountNumber)
        string += "\nAccount Owner: " + self.__owner
        string += "\nAccount Balance: ${:.2f}".format(self.__balance) 
        return string

    def getNextAccountNumber():
        thisAccountNumber = BankAccount.__nextAccountNumber
        BankAccount.__nextAccountNumber += 1
        return thisAccountNumber

    @abstractmethod
    def endOfMonth():
        pass

class Savings(BankAccount):
    def __init__(self, owner, balance = 0.0, interestRate = 3.25):
        BankAccount.__init__(self, owner, balance)
        self.__interestRate = interestRate

    def getInterestRate(self):
        return self.__interestRate

    def setInterestRate(self, newRate):
        self.__interestRate = newRate

    def __eq__(self, other):
        return BankAccount.__eq__(self, other) and self.getInterestRate() == other.getInterestRate()

    def __str__(self):
        string = BankAccount.__str__(self)
        string += "\nAnnual Interest Rate: {:.2f}%".format(self.__interestRate)
        return string

    '''
        At the end of the month, add money to account based on interest rate
    '''
    def endOfMonth(self):
        self.deposit(BankAccount.getBalance(self) * (self.getInterestRate() / 1200))

class Checking(BankAccount):
    TRANSACTION_FEE = 5.00

    def __init__(self, owner, balance = 0.0):
        BankAccount.__init__(self, owner, balance)
        self.__transactions = 0

    def getTransactionsNum(self):
        return self.__transactions

    def deposit(self, amount):
        BankAccount.deposit(self, amount)
        self.__transactions += 1

    def withdraw(self, amount):
        BankAccount.withdraw(self, amount)
        self.__transactions += 1

    def __eq__(self, other):
        return BankAccount.__eq__(self, other) and self.getTransactionsNum() == other.getTransactionsNum()

    def __str__(self):
        string = BankAccount.__str__(self)
        string += "\nTransactions this month: " + str(self.__transactions)
        return string

    '''
        At the end of the month, check to see if more than 7 transactions have been made. If so, withdraw the transaction fee (default $5.00)
    '''
    def endOfMonth(self):
        if self.__transactions > 7:
            BankAccount.withdraw(self, Checking.TRANSACTION_FEE)
        self.__transactions = 0