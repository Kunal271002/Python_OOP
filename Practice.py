class Account: 
     
    #Parametrizes Constructor
    def __init__(self,balance,Account):
        self.balance = balance
        self.Account = Account

    #Methods
    def Credit(self,salary):
        self.balance = self.balance+salary
        return self.balance

    def Debit(self,expenses):
        self.balance = self.balance-expenses
        return self.balance

    def Balance(self):
        print(self.balance)

Account1 = Account(20000, 1970)
Account1.Credit(50000)
Account1.Debit(50000)
print(Account1.Balance())
