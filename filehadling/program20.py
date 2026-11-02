file = open("transactions.txt", "r")

total_deposits = 0
total_withdrawals = 0
balance = 0
largest = 0

for line in file:
    transaction, amount = line.strip().split(",")

    amount = float(amount)

    if transaction == "D":
        total_deposits += amount
        balance += amount

    elif transaction == "W":
        total_withdrawals += amount
        balance -= amount

    if amount > largest:
        largest = amount

file.close()

print("Total Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)
print("Final Balance:", balance)
print("Largest Transaction:", largest)