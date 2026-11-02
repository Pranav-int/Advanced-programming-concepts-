# Q10. Create abstract Appointment with book_appointment()
# and calculate_fee().
# Derive GeneralAppointment, SpecialistAppointment,
# and EmergencyAppointment.

from abc import ABC, abstractmethod


class Appointment(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked.")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked.")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked.")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Fee:", appointment.calculate_fee())