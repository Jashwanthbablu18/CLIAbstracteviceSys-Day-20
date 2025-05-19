# Day 20 - Abstraction & super(): Device System

# Importing Abstract Base Classes(ABC) to implement abstraction
from abc import ABC, abstractmethod

# This Device class inherits from Abstract Base Class and defines templates for other classes.
class Device(ABC):

    # This initializes a brand attr for device
    def __init__(self, brand):
        self.brand = brand

    # The turn_on() and specs() are abstract methods.
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def specs(self):
        pass

    # The intro() is a concrete/normal method.
    def intro(self):
        print(f"📱 Device Brand: {self.brand}")


# Phone subclass is a subclass of Device class
class Phone(Device):
    # This calls the base class's constructor using super() to initialize the brand and also initializes the os, sim_slots attrs
    def __init__(self, brand, os, sim_slots): 
        super().__init__(brand)
        self.os = os
        self.sim_slots = sim_slots

    # This provides turn_on() implementation specific to phones
    def turn_on(self):
        print(f"🔋 Booting up {self.brand} Phone... Welcome!")

    # This provides info about phone.
    def specs(self):
        print(f"📞 OS: {self.os}, SIM Slots: {self.sim_slots}")


# Laptop subclass is a subclass of Device class
class Laptop(Device):
    # This calls the base class's constructor using super() to initialize the brand and also initializes the processor, ram attrs
    def __init__(self, brand, processor, ram):
        super().__init__(brand)
        self.processor = processor
        self.ram = ram

    # This provides turn_on() implementation specific to laptops
    def turn_on(self):
        print(f"🔌 Powering on {self.brand} Laptop... Hello!")

     # This provides info about laptop.
    def specs(self):
        print(f"💻 Processor: {self.processor}, RAM: {self.ram}GB")

# main
def main():
    print("💡 Day 20 - Abstraction + super(): Device System\n")

    # Phone demo: takes brand name, OS and SIM Slots as parameters.
    phone = Phone("Samsung", "Android 14", 2)
    # calls some methods
    phone.intro()
    phone.turn_on()
    phone.specs()

    print("\n---\n")

    # Laptop demo: takes brand name, processor and ram as parameters
    laptop = Laptop("Dell", "Intel i7", 16)
    # calls some methods
    laptop.intro()
    laptop.turn_on()
    laptop.specs()


# calling main() to starting execution of program
if __name__ == "__main__":
    main()
