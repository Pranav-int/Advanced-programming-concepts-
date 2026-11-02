# Q8. Create abstract Authentication with authenticate().
# Implement Password, OTP, and Biometric authentication.

from abc import ABC, abstractmethod


class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()