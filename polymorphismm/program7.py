# Q7. Create BankAccount with calculate_interest().
# Derive SavingsAccount, CurrentAccount, and FixedDepositAccount.
# Override the method for different interest rates.

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.05


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))