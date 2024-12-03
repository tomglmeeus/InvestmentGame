import Users


uname = input("Hi, what is your name? ")
ubalance = input("Set your balance: ")

user = Users.Users(uname, ubalance)

print(f"Hello {user.username} your account balanace is {user.balance}.")
print("Do you want to buy stocks? (Y/N)")
