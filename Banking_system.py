class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("rs", amount, "was debited")
        print("total amount = ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("rs", amount, "was credited")
        print("total amount = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.credit(500)
acc1.debit(1000)
    