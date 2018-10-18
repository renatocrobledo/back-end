'''
Se busca definir la representación de una cuenta de banco en una Clase... es decir, usando herramientas de Programación orientada a objetos.

La cuenta de banco solo llevará el tracking del balance del usuario: depósitos y retiros (como si se tratara de un cajero )
No nos preocuparemos por mas de un usuario ni mas de una cuenta. ( por el momento )

Entonces el reto en si es:

Definir un menú que simbolice la cuenta de banco con opciones:

[d] Depositar
[r] Retirar
[m] Mostrar Balance
[s] Salir

Y obviamente hacer que funcione :)
'''

def parse_to_float(str_number):
    try:
      return float(str_number)
    except ValueError:
      return print('ups! only numbers are alowed!')

accounts_list = []
def menu():
  return input(' [d] Deposit \n [r] withdraw \n [s] Show Balance \n [t] Transfer \n [e] Exit \n')
def get_account_option():
  return input(' [a] Add account \n [v] View or select account \n [e] Exit \n')
def show_accounts():
  print("========Account List======")
  for account in accounts_list:
    print(account)
  print("==========================")

class Account():
  def __init__(self, balance = 0.0):
    self.balance = float(balance)
    self.id = len(accounts_list)
  def __str__(self):
    return f"[{self.id}] ${self.balance}"
  def deposit(self, quantity):
    value = parse_to_float(quantity)
    if value:
      self.balance += value
    return True
  def withdraw(self, quantity):
    value = parse_to_float(quantity)
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

while True:
  account_option = get_account_option()
  selected_card = None
  if account_option == 'e':
    print('Bye!')
    break
  elif account_option == 'a':
    try:
      balance = float(input('How much balance ? ') or "0.0")
      new_account = Account(balance)
      accounts_list.append(new_account)   
      show_accounts()
    except Exception as error:
      print('Eeehm something wrong!', error)
    continue 
  elif account_option == 'v':
    show_accounts()
    try:
      card_id = input("Select id? ")
      if card_id == '':
        continue
      selected_card = accounts_list[int(card_id)]
    except Exception:
      print('ups, this Id is not valid...')
      continue
  else:
    print('Hey that option is not valid :(')
    continue
  while True:
    option = menu()
    if option == 'e':
      print('Bye!')
      break
    elif option == 'd':
      selected_card.deposit(input('How much? '))
    elif option == 'r':
      selected_card.withdraw(input('How much? '))
    elif option == 's':
      selected_card.show_balance()
    elif option == 't':
      show_accounts()
      receiver_card_id = int(input("what's the id of the receiver? "))
      amount = input('How much? ')
      selected_card.transfer(amount, receiver_card_id)










