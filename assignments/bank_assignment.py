# class BankAccount:
#  def __init__(self, Acc_name, Acc_number, Acc_balance):
#   self.Acc_name = Acc_name
#   self.Acc_number = Acc_number
#   self.Acc_balance = Acc_balance
#  def deposit(self, amount):
#   self.Acc_balance += amount
#   print(F"deposit is successful, the new balance is {self.Acc_balance}")
#  def withdraw(self, amount):
#   if amount <= self.Acc_balance:
#    self.Acc_balance -= amount
#    print(f"{amount} withdraw successful, New Balance is {self.Acc_balance}")
#   else:
#    print(f"insufficient Balance")
#  def Balance(self):
#   print (f"Balance in the account is {self.Acc_balance}")
#   return self.Acc_balance

# Acc = BankAccount("khadijah", "01202230", 7500)
# Acc.deposit(2500)
# Acc.withdraw(1700)
# Acc.Balance()

class Person:
    def __init__(self, name, age, state_of_origin):
        self.name = name
        self.age


 