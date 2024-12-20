# Identify at least 3 states and 3 behaviors for your smartphone. Then, for the listed states and behaviors, create a class with attributes and methods. 
# Try to use verbs in method names as they describe activities. Finally, create a smartphone object, call its methods and display object’s properties.

class Phone():
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year
    
    def set_price(self, price):
        self.price = price

    def display_info(self):
        print(f'Year: {self.year}')
        print(f'Model: {self.model}')
        print(f'Price: {self.price}$')
        print()

def main():
    phone = Phone('Samsung', 2009, 500)
    phone.display_info()
    phone.set_model('iPhone')
    phone.display_info()
    phone.set_year(2013)
    phone.display_info()
    phone.set_price(1500)
    phone.display_info()

if __name__ == '__main__':
    main()
