class Users:
    def __init__(self, username: str, balance: int):
        self.username = username
        self.balance = balance

    userlist = {}
    def add_to_userlist(self):
        #userlist = {}
        self.userlist[self.username] = self.balance
