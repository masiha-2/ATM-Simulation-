import account_data 
def credit_money():
    amount = float(input("Enter amount to credit: "))
    account_data.balance += amount 
    account_data.transaction.append(f"Deposited: ₹{amount}")
    print("Credit Successful!!")