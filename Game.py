from Users import Users


uname: str = input("Hi, what is your name? ")
ubalance: int = int(input("Set your balance: "))

user = Users(uname, ubalance)

print(f"Hello {user.username} your account balanace is {user.balance}.")

ans = input("Do you want to buy IBM stocks? (Y/N) ")
while ans == "N":
    print("Ok, bye!")
    ans = input("Do you want to buy IBM stocks now? (Y/N) ")
    if ans == "Y":
        continue

print("The price for one stock is x.")  # fill x with price
amount = int(input("How many stocks do you want to buy? "))
