from statement import show_statement
from deposit_money import credit_money
from display_balance import show_balance
from withdraw_money import withdraw


def menu():
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice.isdigit():
        choice= int(choice)
        if choice == "1": show_balance()
            

        elif choice == "2": credit_money()

        elif choice == "3": withdraw()

        elif choice == "4": show_statement()

        elif choice == "5":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice! Try again.") 