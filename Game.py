import Users


uname = input("Hi, what is your name? ")
<<<<<<< HEAD
uemail = input("What is your email?")
ubalance = input("Set your balance")

user = Users.Users(uname,uemail,ubalance)
print(f"hello ",user.username," your email id id",user.email," your account balanace is",user.balance)
print("Do you want to buy stocks Y/N")
=======
ubalance = input("Set your balance: ")
>>>>>>> 94d80a7323b528edd3fa98ed3463604490118854

user = Users.Users(uname, ubalance)
