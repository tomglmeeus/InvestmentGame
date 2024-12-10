from Users import Users
from Stock import Stock


uname: str = input("Hi, what is your name? ")
if uname not in Users.userlist:
    ubalance = int(input("Set your balance: "))
    user: Users = Users(uname, ubalance)
    Users.add_to_userlist(user)

    print(f"Hello {user.username}, your account balanace is {user.balance}.")

ans: str = input("Do you want to buy IBM stocks? (Y/N) ")
while ans not in ("N", "Y"):
    print("Did you not read the prompt correctly? Please try again.")
    ans = input("Do you want to buy IBM stocks? (Y/N) ")

    if ans == "N":
        print("Ok, bye!")
        exit(0)
    elif ans == "Y":
        continue

price_IBM = Stock().GetPrice()
print(f"The price for one stock is {price_IBM}.")

while True:
    amount = int(input("How many stocks do you want to buy? "))
    totalprice = price_IBM * amount
    if totalprice > ubalance:
        print("{}, you have insufficient balance you poor thing.".format(uname))
    else:
        print(f"The total for your order will be {totalprice}.")
        ubalance -= totalprice
        print(f"Your remaining balance is {ubalance}.")
        break

profit = Stock().GetProfitLoss()
print(f"If you would sell today, your profit/loss would be {profit} \nOk, bye!")
