class Account():
  def __init__(self, balance = 0.0, account_number = 'XXX'):
    self.balance = float(balance)
    self.account_number = account_number
  def __str__(self):
    return f"{self.account_number} -> ${self.balance}"
  def deposit(self, quantity):
    value = self.parse_to_float(quantity)
    if value:
      self.balance += value
    return True
  def withdraw(self, quantity):
    value = self.parse_to_float(quantity)
    if value:
      if value > self.balance:
        return print('Uff there\'s not enough balance! :( get a job!')
      self.balance -= value
      return True
  def show_balance(self):
    print("========================")
    print(f"You have ${self.balance} available in your account")
    print("========================")
  def transfer(self, quantity, receiver_id):
    try:
      receiver_card = accounts_list[receiver_id]
      if(self.withdraw(quantity)):
        receiver_card.deposit(quantity)
    except Exception as error:
      print('ups!, something went wrong maybe the id is incorrect!')
  def remove_this_account(self):
    accounts_list.remove(self)
  def parse_to_float(self, str_number):
    try:
      return float(str_number)
    except ValueError:
      return print('ups! only numbers are alowed!')  
