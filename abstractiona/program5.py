# Q5. Create abstract Patient with calculate_bill() and treatment().
# Derive InPatient, OutPatient, and EmergencyPatient.

from abc import ABC, abstractmethod


class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        return "Hospital Admission"


class OutPatient(Patient):
    def calculate_bill(self):
        return 2000

    def treatment(self):
        return "Regular Checkup"


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 15000

    def treatment(self):
        return "Emergency Treatment"


patients = [
    InPatient(),
    OutPatient(),
    EmergencyPatient()
]

for patient in patients:
    print("Treatment:", patient.treatment())
    print("Bill:", patient.calculate_bill())