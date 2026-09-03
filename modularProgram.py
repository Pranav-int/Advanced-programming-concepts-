def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    return charge
def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    fixed_charge = 100
    tax = energy_charge * 0.05       
    discount = energy_charge * 0.10  

    total_bill = energy_charge + fixed_charge + tax - discount

    return total_bill

units = 250

bill = calculate_bill(units)

print("Units Consumed:", units)
print("Electricity Bill: ₹", bill)
