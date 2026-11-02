# Q8. Create a class Patient containing patient ID, name, age,
# disease, and consultation fee.
# Define methods to display patient information and calculate total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def calculate_total_bill(self, medicine_bill):
        return self.consultation_fee + medicine_bill

    def display(self, medicine_bill):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)
        print("Medicine Bill:", medicine_bill)
        print("Total Bill:", self.calculate_total_bill(medicine_bill))


# Creating object
p = Patient(101, "Pallavi", 21, "Fever", 500)

p.display(1000)