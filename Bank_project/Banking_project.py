amount = int(input())
amount_1 = int(input())
amount_2 = int(input())

class BankAmount:
    def __init__(self,account_number):
        self.account_number = account_number
        self.balance = 0
    
    def get_balance_details(self):
        return self.balance
    
    def withdraw_amount(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        
        else:

            raise ValueError("Insuficent Fund")
    
    def deposit(self,amount):
        self.balance += amount

def transaction_amount(acc_1,acc_2,amount):
    try:
        acc_1.withdraw_amount(amount)
        acc_2.deposit(amount)
        return
    except:

        print(False)

User_1 = BankAmount('00001')
User_2 = BankAmount('00002')
User_1.deposit(amount)
User_2.deposit(amount_1)
print('User_1 Bank Balance: {}'.format(User_1.get_balance_details()))
print('User_2 Bank Balance: {}'.format(User_2.get_balance_details()))

transaction_amount(User_1,User_2,amount_2)

print(" ")
print('Your Transcation has been Successfull completed from User_1 to User_2')
print(" ")
print('User_1 Bank Balance: {}'.format(User_1.get_balance_details()))
print('User_2 Bank Balance: {}'.format(User_2.get_balance_details()))
