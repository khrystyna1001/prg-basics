class BankAccount:
    def __init__(self, number):
        self.number = number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds on the account')
    
    def display_info(self):
        print(f'Bank Account No: {self.number}')
        print(f'Balance: UAH {self.balance:.1f}')