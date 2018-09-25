class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner: {} \n Account balance: {}".format(self.owner, self.balance)

    def deposit(self, deposit_value):
        self.balance = self.balance + deposit_value
        return "Deposit Accepted"

    def withdraw(self, withdraw_value):
        if withdraw_value > self.balance:
            print("Funds Unavailable")
        else:
            self.balance = self.balance - withdraw_value
            print("Withdraw Accepted")

acct1 = Account('Jose', 100)

str(acct1)
acct1.owner
acct1.balance
acct1.deposit(200)
acct1.withdraw(400)
