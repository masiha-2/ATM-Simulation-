import account_data 


def withdraw():
    amount= float(input("Enter amount to withdraw: "))
    if amount> account_data.balance:
        print("Insufficient Amount 😔")
    else:
        account_data.balance -= amount
        account_data.transaction.append(f"Withdrawn amount: ₹{amount}")
        print("Withdraw Successful 🤑🤑")