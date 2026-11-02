# Q3. Create abstract BankAccount with deposit() and withdraw().
# Derive SavingsAccount and CurrentAccount and implement operations.

from abc import ABC, abstractmethod


class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)


account = SavingsAccount(10000)

account.deposit(2000)
account.withdraw(3000)

print("Balance:", account.balance)