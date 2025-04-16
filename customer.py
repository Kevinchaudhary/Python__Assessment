
from main import main

def customer_menu():
    while True:
        print("\n=== Customer Menu ===")
        print("1) Withdraw Amount")
        print("2) Deposite Amount")
        print("3) View Balance")
        print("4) Back to main menu")
        choice = input("Choose an option: ")

        if choice == '1':
            withdraw()
        elif choice == '2':
            deposit()
        elif choice == '3':
            view_balance()
        elif choice == '4':
            main()
            break
        else:
            print(" Invalid choice, try again.")

file = "passbook.txt"


def data_customer():
    customer = {}
    try:
        with open(file , 'r') as f:
            for data in f:
                data = data.strip().split(',')
                if len(data) == 3:
                    acc_no, name, balance = data
                    customer[acc_no] = {'name':name,'balance': float(balance)}

    except FileNotFoundError:
        pass
    return customer

def data_add(customer):
    with open(file, 'w') as f:
        for acc_no, data in customer.items():
            line = f"{acc_no}, {data['name']}, {data['balance']}\n"
            f.write(line)

def withdraw():
    customers = data_customer()
    acc_no = input("Enter your Account Number: ").strip()
    if acc_no in customers:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            if amount > customers[acc_no]['balance']:
                print("Insufficient balance.")
                return
            customers[acc_no]['balance'] -= amount
            data_add(customers)
            print(f"{amount} withdrawn successfully.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No customer found.")


def deposit():
    customers = data_customer()
    acc_no = input("Enter your Account Number: ").strip()

    if acc_no in customers:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            customers[acc_no]['balance'] += amount
            data_add(customers)
            print(f"{amount} deposited successfully.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No customer found.")

def view_balance():
    customers = data_customer()
    acc_no= input("Enter your Account Number: ").strip()

    if acc_no in customers:
        c = customers[acc_no]
        print("\nCustomer Details")
        print(f"Balance: {c['balance']}")
    else:
        print("No customer found.")

# def view_balance():
#     customers = data_customer()  # Assuming this function fetches the customers
#     acc_no = input("Enter your Account Number: ").strip()

#     if acc_no in customers:
#         c = customers[acc_no]
#         print("\nCustomer Details")
#         print(f"Account Number: {acc_no}")
#         print(f"Balance: ₹{c['balance']:.2f}")  # Formatting the balance to 2 decimal places for currency
#     else:
#         print("❌ No customer found with the given account number.")

