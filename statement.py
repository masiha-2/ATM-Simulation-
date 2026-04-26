import account_data 

def show_statement():
    print("\n Transaction Statement: ")
    if not account_data.transaction:
        print("Not Transaction Yet !!")
    else:
        for t in account_data.transaction:
            print(t)