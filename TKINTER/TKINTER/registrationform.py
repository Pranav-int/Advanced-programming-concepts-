
import tkinter as tk
from tkinter import ttk, messagebox

# Main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("550x650")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="USER REGISTRATION FORM",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
title.pack(pady=15)

# Form frame
frame = tk.Frame(root, bg="white", padx=25, pady=20)
frame.pack(padx=20, pady=5, fill="both", expand=True)

# Input fields
entries = {}

def add_field(label_text, row):
    label = tk.Label(
        frame, text=label_text,
        font=("Arial", 10), bg="white"
    )
    label.grid(row=row, column=0, sticky="w", pady=7)

    entry = tk.Entry(frame, font=("Arial", 10), width=28)
    entry.grid(row=row, column=1, pady=7, padx=10)
    entries[label_text] = entry

add_field("Full Name", 0)
add_field("Middle Name", 1)
add_field("Last Name", 2)
add_field("Mobile Number", 3)

# State dropdown
tk.Label(frame, text="State", bg="white").grid(
    row=4, column=0, sticky="w", pady=7
)

state_var = tk.StringVar()
state_box = ttk.Combobox(
    frame, textvariable=state_var,
    values=["Maharashtra", "Goa", "Gujarat", "Karnataka"],
    state="readonly", width=26
)
state_box.grid(row=4, column=1, pady=7, padx=10)

# District dropdown
tk.Label(frame, text="District", bg="white").grid(
    row=5, column=0, sticky="w", pady=7
)

district_var = tk.StringVar()
district_box = ttk.Combobox(
    frame, textvariable=district_var,
    values=["Pune", "Mumbai", "Satara", "Nashik",
            "Kolhapur", "Nagpur"],
    state="readonly", width=26
)
district_box.grid(row=5, column=1, pady=7, padx=10)

# Taluka
add_field("Taluka", 6)

# Address
tk.Label(frame, text="Address", bg="white").grid(
    row=7, column=0, sticky="nw", pady=7
)

address_text = tk.Text(frame, width=27, height=3, font=("Arial", 10))
address_text.grid(row=7, column=1, pady=7, padx=10)

# PIN Code
add_field("PIN Code", 8)

# Registration function
def register():
    full_name = entries["Full Name"].get().strip()
    middle_name = entries["Middle Name"].get().strip()
    last_name = entries["Last Name"].get().strip()
    mobile = entries["Mobile Number"].get().strip()
    taluka = entries["Taluka"].get().strip()
    pin = entries["PIN Code"].get().strip()
    address = address_text.get("1.0", "end-1c").strip()

    if not all([
        full_name, middle_name, last_name, mobile,
        state_var.get(), district_var.get(),
        taluka, address, pin
    ]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if not full_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid full name.")
        return

    if not middle_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid middle name.")
        return

    if not last_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid last name.")
        return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror(
            "Error", "Mobile number must contain 10 digits."
        )
        return

    if not pin.isdigit() or len(pin) != 6:
        messagebox.showerror(
            "Error", "PIN code must contain 6 digits."
        )
        return

    messagebox.showinfo(
        "Success",
        "Registration Successful!\n"
        f"Name: {full_name} {middle_name} {last_name}\n"
        f"Mobile: {mobile}\n"
        f"State: {state_var.get()}\n"
        f"District: {district_var.get()}"
    )

# Buttons
button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=12)

tk.Button(
    button_frame, text="Register",
    command=register, bg="#2471a3",
    fg="white", font=("Arial", 11, "bold"),
    width=12
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame, text="Clear",
    command=lambda: clear_form(),
    bg="#7f8c8d", fg="white",
    font=("Arial", 11), width=12
).grid(row=0, column=1, padx=8)

def clear_form():
    for entry in entries.values():
        entry.delete(0, tk.END)
    state_box.set("")
    district_box.set("")
    address_text.delete("1.0", tk.END)

# Run application
root.mainloop()
