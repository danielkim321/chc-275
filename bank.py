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
        index = names.index(account)
        balance[index] = balance[index] + amount
        print(f"your new balance is {balance[index]}")
    elif action == "withdraw":
        account = input("which account would you like to withdraw from? James, Alice, Bob:")
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
        accounts.append(account_name)
        print(f"account {account_name} created")
    elif action == "exit":
        print("thank you for banking with us")
        break
    else:
        print("invalid action, please try again")



