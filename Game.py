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

price_IBM: float = 10  # fill with price function
print(f"The price for one stock is {price_IBM}.")

amount = int(input("How many stocks do you want to buy? "))
totalprice = price_IBM * amount
print(f"The total for your order will be {totalprice}.")

# Write something to show the budget that is left (Class? Function?)
