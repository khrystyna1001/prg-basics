import queue

customer_queue = queue.Queue()

ticket_number = 1

def add_customer():
    global ticket_number
    customer_queue.put(ticket_number)
    print(f"Customer with ticket number {ticket_number} added to the queue.")
    ticket_number += 1

def serve_customer():
    if not customer_queue.empty():
        served_customer = customer_queue.get()
        print(f"Customer with ticket number {served_customer} is being served.")
    else:
        print("No customers in the queue to serve.")

while True:
    print("\nCustomer Service Menu")
    print("1. Add new customer")
    print("2. Serve next customer")
    print("0. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        add_customer()
    elif choice == '2':
        serve_customer()
    elif choice == '0':
        print("Exiting the program. Thank you for using the service!")
        break
    else:
        print("Invalid option. Please select again.")