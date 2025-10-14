print("Deposit:")
print("Withdraw:")
print("transfer:")
print("exit")

option = input("desposit squence: ")
if option.strip == "deposit":
    print("deposit sequence")
elif option.strip == "withdraw":
    print("withdraw sequence")
elif option.strip == "transfer":
    print("transfer sequence")
elif option.strip == "exit":
    print("exit sequence")
    
myster = "      hello"
print(myster)



option = input("desposit squence: ").strip()
if option == "deposit":
    print("deposit sequence")
elif option == "withdraw":
    print("withdraw sequence")
elif option == "transfer":
    print("transfer sequence")
elif option == "exit":
    print("exit sequence")


myster = "      hello"
print(myster)
myster = myster.strip().lower()
print(myster)



money = "10a"
if money.isnumeric():
    money = int(money)
    val = money + 5
    print(val)
else:
    print("thats not a number")
