import random

temperature = random.uniform(34.0, 42.0)

class Thermometer:
    def __init__ (self, temperature):
        self.temperature = round(temperature, 1)
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def measure(self):
        if self.is_on:
            if self.temperature >= 41.0:
                print(f'Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)')
            elif self.temperature >= 37.0:
                print(f'Temperature: {self.temperature}C (fever)')
            else:
                print(f'Temperature: {self.temperature}C')
        else:
            print('Thermometer is off')