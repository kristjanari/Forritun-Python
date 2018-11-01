def print_accounts(accounts):
    for account in accounts:
        print(account)

def update_accounts(accounts):
    for account in accounts:
        account.update()

class BankAccount:
    
    interest_rate = 0.0
    bonus_rate = 0.0

    def __init__(self, funds):
        self.funds = funds

    def update_balance(self):
        self.funds = self.funds*(1 + self.interest_rate + self.bonus_rate)

    def __str__(self):
        return "Balance: {:.2f}".format(self.funds)

class SavingsAccount(BankAccount):
    interest_rate = 0.05
    bonus_rate = 0.10

class DebitAccount(BankAccount):
    interest_rate = 0.02
    bonus_rate = 0
