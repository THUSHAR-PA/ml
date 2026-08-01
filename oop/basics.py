class Microwave:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        self.turned_on: bool = False 
    def turn_on(self) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is already on.")
        else:
            self.turned_on = True
            print(f"{self.brand} microwave is now on.")
    def turn_off(self) -> None:
        if  self.turned_on:
            self.turned_on = False
            print(f"{self.brand} microwave is now off.")
        else:
            print(f"{self.brand} microwave is already off.")
    def run(self, time: int) -> None:
        if self.turned_on:
            print(f"{self.brand} microwave is running for {time} seconds at {self.power} watts.")
        else:
            print(f"{self.brand} microwave is off. Please turn it on first.")
        


smeg: Microwave = Microwave("Smeg", 800)
smeg.turn_on()  # Output: Smeg microwave is now on.
# smeg.turn_on()  # Output: Smeg microwave is already on.
smeg.run(30)  # Output: Smeg microwave is running for 30 seconds at 800 watts.
smeg.turn_off()  # Output: Smeg microwave is now off.
smeg.run(30)  # Output: Smeg microwave is off. Please turn it on first.








# print(smeg.brand)  # Output: Smeg
# print(smeg.power)  # Output: 800
# print(smeg)  # Output: <__main__.Microwave object at 0x...>

# bosch: Microwave = Microwave("Bosch", 1000)
# print(bosch.brand)  # Output: Bosch
# print(bosch.power)  # Output: 1000


