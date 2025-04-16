

def Bank_menu():
    while True:
        print("\t Operations Menu")
        print("\n1) Add Customer")
        print("2) View Customer")
        print("3) View All Customers")
        print("4) View Total Bank Balance")
        print("5) Back to Main Menu")

        choice = input("Choose an option: ")


        if choice == '1':
            add_customer()
        elif choice == '2':
            view_customer()
        elif choice == '3':
            view_all_customers()
        elif choice == '4':
            total_bank_balance()
        elif choice == '5':
            break
        else:
            print("Invalid choice, try again")

file = "passbook.txt"

def data_customer():
    customer = {}
    try:
        with open(file , 'r') as f:
            for i in f:
                data = i.strip().split(',')
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


def add_customer():
    customer = data_customer()
    acc_no = input("Enter Account Number: ")
    if acc_no in customer:
        print("Account already exists.")
        return
    
    name = input("Enter Name: ")
    balance = input("Enter Initial Balance: ")
    customer[acc_no] = {'name': name, 'balance': balance}
    data_add(customer)
    print(" Customer added successfully.")


def view_customer():
    customers = data_customer()
    acc_no = input("Enter Account Number: ")
    if acc_no in customers:
        data = customers[acc_no]
        print(f"acc_no: {acc_no}, Name: {data['name']}, Balance: {data['balance']}")
    else:
        print(" Customer not found.") 

def view_all_customers():
    customers = data_customer()
    if not customers:
        print("No customers found.")
        return
    print("\nAll Customers:")
    for acc_no, data in customers.items():
        print(f"acc_no: {acc_no}, Name: {data['name']},Balance: {data['balance']}")

def total_bank_balance():
    customers = data_customer()
    total = sum(data['balance'] for data in customers.values())
    print(f"Total Balance in Bank: {total}")


    




    
