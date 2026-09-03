def consultation_charge():
    return 500
def laboratory_charge():
    return 1000
def medicine_charge():
    return 1500
def room_charge(days):
    return days * 1000
def discount(category, total):
    if category == "senior":
        return total * 0.10
    elif category == "child":
        return total * 0.05
    else:
        return 0
def final_bill(category, days):
    consultation = consultation_charge()
    laboratory = laboratory_charge()
    medicine = medicine_charge()
    room = room_charge(days)

    total = consultation + laboratory + medicine + room
    discount_amount = discount(category, total)
    final = total - discount_amount

    print("Consultation:", consultation)
    print("Laboratory:", laboratory)
    print("Medicine:", medicine)
    print("Room:", room)
    print("Discount:", discount_amount)
    print("Final Bill: ₹", final)



final_bill("senior", 3)
