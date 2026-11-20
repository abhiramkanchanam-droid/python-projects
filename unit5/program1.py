class SavingsAccount:
  def __init__(self, holder_name, initial_balance):
    self.holder_name = holder_name
    self.initial_balance = initial_balance
  def deposit(self, amount):
    self.initial_balance += amount
    print("Amount Deposited:", amount)
  def withdraw(self, amount):
    if amount <= self.initial_balance:
      self.initial_balance -= amount
      print("Amount Withdrawn:", amount)
    else:
      print("Insufficient Balance")
  def display(self):
    print("Account Holder:", self.holder_name)
    print("Balance:", self.initial_balance)
user_account = SavingsAccount("abhiram", 5000)
user_account.deposit(200)
user_account.withdraw(10)
user_account.display()