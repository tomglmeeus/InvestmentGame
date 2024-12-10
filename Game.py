from Users import Users
from Stock import Stock


uname: str = input("Hi, what is your name? ")
if uname not in Users.userlist:
    ubalance: int = int(input("Set your balance: "))
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

price_IBM: float = Stock().GetPrice()
print(f"The price for one stock is {price_IBM}.")

amount = int(input("How many stocks do you want to buy? "))
totalprice = price_IBM * amount
if totalprice > ubalance:
    print("{}, you have insufficient balance".format(uname))
else:
    print(f"The total for your order will be {totalprice}.")
    ubalance -= totalprice
    print(f"You remaining balance is {ubalance}.")

# Write something to show the balance that is left (Class? Function?)
