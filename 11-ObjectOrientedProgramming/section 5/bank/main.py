from account import BankAccount

# Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
# Display account balance
# Deposit PLN 25,30
# Display account balance
# Withdraw PLN 31,70
# Display account balance
# Withdraw PLN 14
# Display account balance

def main():
    BA1 = BankAccount('12 3456 5555 9090 1111 0000 7722')
    BA1.display_info()
    BA1.deposit(250.30)
    BA1.display_info()
    BA1.withdraw(310.70)
    BA1.display_info()
    BA1.withdraw(140)
    BA1.display_info()

if __name__ == "__main__":
    main()