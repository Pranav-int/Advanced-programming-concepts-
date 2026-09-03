balance = 0
history = []


def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited: ₹" + str(amount))


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        history.append("Withdrawn: ₹" + str(amount))
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Current Balance: ₹", balance)


def transaction_history():
    print("Transaction History:")
    for transaction in history:
        print(transaction)



deposit(5000)
withdrawal(1500)
deposit(2000)
withdrawal(7000)

balance_enquiry()
transaction_history()
