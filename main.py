import bank as b
import customer as c


def main():
    while True:
        print("\n===== Bank Management System =====")
        print("1. Banker Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            b.Bank_menu()
        elif choice == '2':
            c.customer_menu()
        elif choice == '3':
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid input. Please try again.")

main()
