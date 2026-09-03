def calculate_bill(prices, quantities):
    total = sum(price * quantity for price, quantity in zip(prices, quantities))

    if total >= 5000:
        discount = total * 0.20   
    elif total >= 2000:
        discount = total * 0.10   
    else:
        discount = 0

    final_bill = total - discount

    return final_bill



prices = [1000, 500, 2000]
quantities = [2, 1, 1]

print("Total Bill: ₹", calculate_bill(prices, quantities))
