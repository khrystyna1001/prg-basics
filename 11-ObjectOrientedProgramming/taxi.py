class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f'Rate: {self.rate_per_km}  |  Distance: {self.distance}  |  Fare: {self.fare}')


def main():
    taxi1 = TaxiRide(4)
    taxi1.distance = 100
    taxi2 = TaxiRide(2)
    taxi2.distance = 102

    taxi1.calculate_fare(taxi1.distance)
    taxi2.calculate_fare(taxi2.distance)

    taxi1.print_receipt()
    taxi2.print_receipt()

if __name__ == "__main__":
    main()