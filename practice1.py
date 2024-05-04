class Account():
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)


account1 = Account('dotun', 1023558902, 500)
account2 = Account('temitope', 2234897100, 500)
account3 = Account('ezekiel', 3091267825, 500)
account4 = Account('josh', 1045609821, 500)
account5 = Account('ope', 3908124568, 500)
global_amount = 500

accounts = [account1, account2, account3, account4, account5]

account_numbers = [account1.account_number, 
                   account2.account_number, 
                   account3.account_number, 
                   account4.account_number, 
                   account5.account_number
                   ]


def add_money(account_number):
    while account_number not in account_numbers:
        input('this account number does not exist on our system. Please try again ')
    else:
        amount = float(input('enter the amount you want to transfer: '))
        for account in accounts:
            if account_number == account.account_number:
                while amount <= 50:
                    input('you cannot send less than 50 naira! enter an higher amount')
                else:
                    account.balance += amount
                    return f"you sent {amount} to {account.name}, his account balance is now {account.balance}"
            

account_number = input('enter the account number you want to transfer to: ')
print(add_money(account_number))






