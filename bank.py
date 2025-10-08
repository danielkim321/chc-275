print("welcome to the bank")
print("Deposit:")
print("Withdraw:")
print("transfer:")
print("Balance:")
print("list accounts:")
print("new account:")
print("remove account:")
print("exit")

balance = [127, 919, 42]
accounts = []
names  = ["James", "Alice", "Bob"] 
while True:
   

    action = input("what would you like to do? ")
    if action == "deposit":
        account = input("which account would you like to deposit to? ")
        print(names)
        amount = float(input("how much would you like to deposit? "))
        index = names.index(account)
        balance[index] = balance[index] + amount
        print(f"your new balance is {balance[index]}")
    elif action == "transfer":
        from_account = input("which account would you like to transfer from? ")
        to_account = input("which account would you like to transfer to? ")
        print(names)
        amount = float(input("how much would you like to transfer? "))
        from_index = names.index(from_account)
        to_index = names.index(to_account)
        if amount > balance[from_index]:
            print("insufficient funds")
        else:
            balance[from_index] = balance[from_index] - amount
            balance[to_index] = balance[to_index] + amount
            print(f"your new balance for {from_account} is {balance[from_index]}")
            print(f"your new balance for {to_account} is {balance[to_index]}")
    elif action == "withdraw":
        account = input("which account would you like to withdraw from?")
        print(names)
        amount = float(input("how much would you like to withdraw? "))
        index = names.index(account)
        balance = balance[index]
        if amount > balance:
            print("insufficient funds")
        else: 
            balance = balance - amount
            print(f"your new balance is {balance}")
    elif action == "balance":
        action= input("which account would you like to check the balance of? James, Alice, Bob:")
        index = names.index(action)
        balance = balance[index]
        print(f"your balance is {balance}")
        
    elif action == "list accounts":
        print("your accounts are:")
        
        for i in range(len(names)):
            print(f"balance for {names[i]}: {balance[i]}")
        
    elif action == "new account":
        account_name = input("what is the name of the new account? ")
        balance.append(0)
        names.append(account_name)
        print(f"account {account_name} created")
    elif action == "remove account":
        account_name = input("what is the name of the account to remove? ")
        if account_name in names:
            index = names.index(account_name)
            names.pop(index)
            balance.pop(index)
            print(f"account {account_name} removed")
        else:
            print("account not found")
    elif action == "exit":
        print("thank you for banking with us")
        break
    else:
        print("invalid action, please try again")



