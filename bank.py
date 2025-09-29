print("welcome to the bank")
print("Deposit:")
print("Withdraw:")
print("Balance:")
print("list accounts:")
print("new account:")
print("exit")
balance = 0
accounts = []
while True:
    action = input("what would you like to do? ").lower()
    if action == "deposit":
        amount = float(input("how much would you like to deposit? "))
        balance = balance + amount
        print(f"your new balance is {balance}")
    elif action == "withdraw":
        amount = float(input("how much would you like to withdraw? "))
        if amount > balance:
            print("insufficient funds")
        else:
            balance = balance - amount
            print(f"your new balance is {balance}")
    elif action == "balance":
        print(f"your balance is {balance}")
    elif action == "list accounts":
        print("your accounts are:")
        for account in accounts:
            print(account)
    elif action == "new account":
        account_name = input("what is the name of the new account? ")
        accounts.append(account_name)
        print(f"account {account_name} created")
    elif action == "exit":
        print("thank you for banking with us")
        break
    else:
        print("invalid action, please try again")


