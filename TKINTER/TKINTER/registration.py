
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("User Registration")
root.geometry("760x700")
root.configure(bg="#F3F0FF")
root.resizable(False, False)

# Colors
BG = "#F3F0FF"
PURPLE = "#6C4AB6"
DARK = "#29234A"
WHITE = "#FFFFFF"
GREY = "#77738B"
LIGHT = "#EAE4FA"
GREEN = "#16866B"

# Variables
data = {}
current_page = 0

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=DARK, height=125)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header, text="CREATE YOUR ACCOUNT",
    font=("Arial", 22, "bold"),
    bg=DARK, fg=WHITE
).pack(pady=(22, 5))

tk.Label(
    header, text="Complete all details to register",
    font=("Arial", 11),
    bg=DARK, fg="#D5C9F5"
).pack()

# Progress indicator
progress_frame = tk.Frame(root, bg=BG)
progress_frame.pack(pady=18)

progress_label = tk.Label(
    progress_frame, text="STEP 1 OF 3",
    font=("Arial", 10, "bold"),
    bg=BG, fg=PURPLE
)
progress_label.pack()

progress_bar = ttk.Progressbar(
    progress_frame, length=400, maximum=3,
    value=1, mode="determinate"
)
progress_bar.pack(pady=7)

# ---------------- CONTENT AREA ----------------
card = tk.Frame(root, bg=WHITE, padx=35, pady=22)
card.pack(fill="both", expand=True, padx=35, pady=(0, 12))

page_title = tk.Label(
    card, text="", font=("Arial", 17, "bold"),
    bg=WHITE, fg=DARK
)
page_title.pack(anchor="w")

page_subtitle = tk.Label(
    card, text="", font=("Arial", 10),
    bg=WHITE, fg=GREY
)
page_subtitle.pack(anchor="w", pady=(4, 15))

form_area = tk.Frame(card, bg=WHITE)
form_area.pack(fill="both", expand=True)

# ---------------- FORM HELPERS ----------------
def make_entry(parent, label, key, row, col):
    box = tk.Frame(parent, bg=WHITE)
    box.grid(row=row, column=col, sticky="ew",
             padx=8, pady=9)

    tk.Label(
        box, text=label + " *",
        font=("Arial", 10, "bold"),
        bg=WHITE, fg=DARK
    ).pack(anchor="w", pady=(0, 6))

    entry = tk.Entry(
        box, font=("Arial", 11),
        bg="#F8F7FC", fg=DARK,
        relief="flat", bd=0,
        highlightthickness=1,
        highlightbackground="#DAD4EB",
        highlightcolor=PURPLE
    )
    entry.pack(fill="x", ipady=9, padx=2)
    data[key] = entry
    return entry


def make_combo(parent, label, key, values, row, col):
    box = tk.Frame(parent, bg=WHITE)
    box.grid(row=row, column=col, sticky="ew",
             padx=8, pady=9)

    tk.Label(
        box, text=label + " *",
        font=("Arial", 10, "bold"),
        bg=WHITE, fg=DARK
    ).pack(anchor="w", pady=(0, 6))

    combo = ttk.Combobox(
        box, values=values,
        state="readonly", font=("Arial", 10)
    )
    combo.pack(fill="x", ipady=5)
    data[key] = combo
    return combo


# ---------------- PAGE 1 ----------------
def show_page1():
    global current_page
    current_page = 0
    clear_area()

    page_title.config(text="Personal Information")
    page_subtitle.config(
        text="Enter your name and contact details."
    )
    progress_label.config(text="STEP 1 OF 3")
    progress_bar.config(value=1)

    form_area.columnconfigure(0, weight=1)
    form_area.columnconfigure(1, weight=1)

    make_entry(form_area, "First Name", "first", 0, 0)
    make_entry(form_area, "Middle Name", "middle", 0, 1)
    make_entry(form_area, "Last Name", "last", 1, 0)
    make_entry(form_area, "Mobile Number", "mobile", 1, 1)

    add_navigation("Next  →", validate_page1)


# ---------------- PAGE 2 ----------------
def show_page2():
    global current_page
    current_page = 1
    clear_area()

    page_title.config(text="Address Information")
    page_subtitle.config(
        text="Provide your complete residential address."
    )
    progress_label.config(text="STEP 2 OF 3")
    progress_bar.config(value=2)

    form_area.columnconfigure(0, weight=1)
    form_area.columnconfigure(1, weight=1)

    state = make_combo(
        form_area, "State", "state",
        ["Maharashtra", "Goa", "Gujarat",
         "Karnataka", "Madhya Pradesh"], 0, 0
    )

    district = make_combo(
        form_area, "District", "district",
        ["Pune", "Mumbai", "Satara", "Nashik",
         "Kolhapur", "Nagpur", "Thane",
         "Sangli", "Solapur"], 0, 1
    )

    make_entry(form_area, "Taluka", "taluka", 1, 0)
    make_entry(form_area, "PIN Code", "pin", 1, 1)

    address_box = tk.Frame(form_area, bg=WHITE)
    address_box.grid(row=2, column=0, columnspan=2,
                     sticky="ew", padx=8, pady=9)

    tk.Label(
        address_box, text="Full Address *",
        font=("Arial", 10, "bold"),
        bg=WHITE, fg=DARK
    ).pack(anchor="w", pady=(0, 6))

    address = tk.Text(
        address_box, height=3,
        font=("Arial", 11),
        bg="#F8F7FC", fg=DARK,
        relief="flat", bd=0,
        highlightthickness=1,
        highlightbackground="#DAD4EB",
        highlightcolor=PURPLE,
        wrap="word"
    )
    address.pack(fill="x", padx=2)
    data["address"] = address

    # Update district options according to state
    districts_by_state = {
        "Maharashtra": [
            "Pune", "Mumbai", "Satara", "Nashik",
            "Kolhapur", "Nagpur", "Thane",
            "Sangli", "Solapur"
        ],
        "Goa": ["North Goa", "South Goa"],
        "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
        "Karnataka": ["Bengaluru Urban", "Mysuru", "Belagavi"],
        "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur"]
    }

    def update_districts(event=None):
        district["values"] = districts_by_state.get(
            state.get(), []
        )
        district.set("")

    state.bind("<<ComboboxSelected>>", update_districts)

    add_navigation("← Back", show_page1,
                   next_label="Review Details  →",
                   next_command=validate_page2)


# ---------------- PAGE 3 ----------------
def show_page3():
    global current_page
    current_page = 2
    clear_area()

    page_title.config(text="Review Your Details")
    page_subtitle.config(
        text="Check your information before submitting."
    )
    progress_label.config(text="STEP 3 OF 3")
    progress_bar.config(value=3)

    details = [
        ("First Name", data["first"].get()),
        ("Middle Name", data["middle"].get()),
        ("Last Name", data["last"].get()),
        ("Mobile Number", data["mobile"].get()),
        ("State", data["state"].get()),
        ("District", data["district"].get()),
        ("Taluka", data["taluka"].get()),
        ("PIN Code", data["pin"].get()),
        ("Full Address",
         data["address"].get("1.0", "end-1c").strip())
    ]

    for label, value in details:
        line = tk.Frame(form_area, bg=WHITE)
        line.pack(fill="x", pady=4)

        tk.Label(
            line, text=label + ":",
            font=("Arial", 10, "bold"),
            bg=WHITE, fg=GREY, width=17, anchor="w"
        ).pack(side="left", anchor="n")

        tk.Label(
            line, text=value,
            font=("Arial", 10),
            bg=WHITE, fg=DARK,
            anchor="w", justify="left",
            wraplength=350
        ).pack(side="left", fill="x", expand=True)

    add_navigation("← Back", show_page2,
                   next_label="Submit Registration",
                   next_command=submit_form)


# ---------------- NAVIGATION ----------------
button_area = tk.Frame(root, bg=BG)
button_area.pack(fill="x", padx=43, pady=(0, 15))


def clear_area():
    for widget in form_area.winfo_children():
        widget.destroy()

    for widget in button_area.winfo_children():
        widget.destroy()


def add_navigation(back_label, back_command,
                   next_label=None, next_command=None):
    if current_page > 0:
        tk.Button(
            button_area, text=back_label,
            command=back_command,
            font=("Arial", 10, "bold"),
            bg=LIGHT, fg=PURPLE,
            relief="flat", cursor="hand2",
            padx=18, pady=10
        ).pack(side="left")

    tk.Button(
        button_area, text=next_label or back_label,
        command=next_command or back_command,
        font=("Arial", 10, "bold"),
        bg=GREEN if current_page == 2 else PURPLE,
        fg=WHITE, relief="flat",
        cursor="hand2", padx=22, pady=10
    ).pack(side="right")


# ---------------- VALIDATION ----------------
def valid_name(value):
    return bool(value.strip()) and all(
        char.isalpha() or char.isspace() or char in "-'"
        for char in value
    )


def validate_page1():
    first = data["first"].get().strip()
    middle = data["middle"].get().strip()
    last = data["last"].get().strip()
    mobile = data["mobile"].get().strip()

    if not all([first, middle, last, mobile]):
        messagebox.showerror(
            "Required Fields",
            "Please fill in every field before continuing."
        )
        return

    for label, value in [
        ("First Name", first),
        ("Middle Name", middle),
        ("Last Name", last)
    ]:
        if not valid_name(value):
            messagebox.showerror(
                "Invalid Name",
                f"{label} must contain only letters."
            )
            return

    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror(
            "Invalid Mobile",
            "Enter a valid 10-digit mobile number."
        )
        return

    show_page2()


def validate_page2():
    required_keys = ["state", "district", "taluka", "pin"]

    for key in required_keys:
        if not data[key].get().strip():
            messagebox.showerror(
                "Required Fields",
                "Please fill in every field before continuing."
            )
            return

    address = data["address"].get("1.0", "end-1c").strip()

    if not address:
        messagebox.showerror(
            "Required Fields", "Please enter your full address."
        )
        return

    if not valid_name(data["taluka"].get().strip()):
        messagebox.showerror(
            "Invalid Taluka",
            "Enter a valid taluka name using letters."
        )
        return

    pin = data["pin"].get().strip()
    if not pin.isdigit() or len(pin) != 6:
        messagebox.showerror(
            "Invalid PIN Code",
            "PIN code must contain exactly 6 digits."
        )
        return

    show_page3()


# ---------------- FINAL SUBMISSION ----------------
def submit_form():
    answer = messagebox.askyesno(
        "Confirm Registration",
        "Are you sure all information is correct?"
    )

    if answer:
        messagebox.showinfo(
            "Registration Successful",
            "Your registration form has been submitted successfully!"
        )
        root.destroy()


# Start application
show_page1()
root.mainloop()
