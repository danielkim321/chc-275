print("welcome to the bank")
print("Deposit:")
print("Withdraw:")
print("Balance:")
print("list accounts:")
print("new account:")
print("exit")
balance = [127, 919, 42]
accounts = []
names  = ["James", "Alice", "Bob"] 
while True:
    action = input("what would you like to do? ")
    if action == "deposit":
        account = input("which account would you like to deposit to? James, Alice, Bob:")
        amount = float(input("how much would you like to deposit? "))
        index = accounts.index(account)
        balance [index] = [index balance + amount] 
        print(f"your new balance is {balance}")
    elif action == "withdraw":
        account = input("which account would you like to withdraw from? (James, Alice, Bob:)")
        amount = float(input("how much would you like to withdraw? "))
        if amount > balance:
            print("insufficient funds")
        else: 
            balance = balance - amount
            print(f"your new balance is {balance}")
    elif action == "balance":
        action= input("which account would you like to check the balance of? James, Alice, Bob:")
        print(f"your balance is {balance}")
        
    elif action == "list accounts":
        print("your accounts are:")
        print(f"{names[0]}, {names[1]}, {names[2]}")
        for i in range(len(names)):
            print(f"balance for {names[i]}: {balance[i]}")
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


