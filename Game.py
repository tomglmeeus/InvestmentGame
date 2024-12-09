from Users import Users


uname = input("Hi, what is your name? ")
ubalance = int(input("Set your balance: "))

user = Users(uname, ubalance)

print(f"Hello {user.username} your account balanace is {user.balance}.")

ans = input("Do you want to buy stocks? (Y/N) ")
while ans == "N":
    print("Ok, bye!")
    ans = input("Do you want to buy stocks now? (Y/N) ")
    if ans == "Y":
        continue

print("Select stocks to view the details and prices:")
choice = input("- Apple (AAPL) \n- Google (GOOG) ")

if choice == "AAPL":
    # fetch price for Apple stock
    print("Price for AAPL is x.")
elif choice == "GOOG":
    # fetch price for Google stock
    print("Price for AAPL is x.")
