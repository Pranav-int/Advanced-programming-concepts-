# Q15. Create SmartDevice with turn_on() and turn_off().
# Derive Light, Fan, AC, and TV.
# Override methods according to each device.

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()