
class Account:
    def __init__(self, full_name, acc_num, phone, balance):#method,function,constructor--->set up info
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} has been deposited to {self.acc_num}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds.Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount {amount} has been withdrawn from {self.acc_num}")

    def check_balance(self):
        print(f"Balance for account {self.acc_num} is: {self.balance}")

#data and methods manipulate the data
kevo_acc=Account("Kevin Maina","0001","0771896721",10000)
sara_acc=Account("Sara Maina","0002","0978674356",20000)
willy_acc=Account(balance=3400,acc_num="0005",phone="0725760430",full_name="Willy James")

kevo_acc.deposit(3500)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()

sara_acc.deposit(5000)
sara_acc.check_balance()