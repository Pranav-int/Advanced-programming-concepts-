cart = {}
def add_product(name, price, quantity):
    cart[name] = [price, quantity]
def remove_product(name):
    if name in cart:
        del cart[name]
def calculate_subtotal():
    total = 0
    for price, quantity in cart.values():
        total += price * quantity
    return total
def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.10
    elif coupon == "SAVE20":
        return subtotal * 0.20
    return 0
def calculate_gst(amount):
    return amount * 0.18   # 18% GST


def generate_invoice(coupon):
    subtotal = calculate_subtotal()
    discount = apply_coupon(subtotal, coupon)
    amount = subtotal - discount
    gst = calculate_gst(amount)
    final_amount = amount + gst

    print("Subtotal: ₹", subtotal)
    print("Discount: ₹", discount)
    print("GST: ₹", gst)
    print("Final Amount: ₹", final_amount)

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)

remove_product("Mouse")

generate_invoice("SAVE10")
