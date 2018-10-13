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
      return print('ups! solo numeros son admitidos!')

ACCOUNT_ID = 0

account_0 = None
account_1 = None

class Account():
  def __init__(self, balance = 0):
      self.balance = balance

  def deposit(self, quantity):
    value = parse_to_float(quantity)
    if value:
      self.balance += value
    return True
  def withdraw(self, quantity):
    value = parse_to_float(quantity)
    if value:
      if value > self.balance:
        return print('metase a chambear machin!')
      self.balance -= value
      return True
  def show_balance(self):
    print(f"Tienes ${self.balance} en tu cuenta")
  def transfer(self, quantity):
      if self.id == '0':
        if account_0.withdraw(quantity):
          account_1.deposit(quantity)
      else:
        if account_1.withdraw(quantity):
          account_0.deposit(quantity)

account_0 = Account()
account_1 = Account()

def menu():
  return input(' [d] Depositar \n [r] Retirar \n [m] Mostrar Balance \n [t] Transferir \n [s] Salir \n')

def select_card():
   return input(' [0] account_0 \n [1] account_1 [s] Salir')

while True:

  card_id = select_card()

  if card_id == 's':
    print('Bye!')
    break

  if card_id != '0' or card_id != '1':
    print('Ups no existe esa tarjeta')
    continue
  selected_card = account_0 if  card_id == '0' else account_1

  while True:
    option = menu()
    if option == 's':
      print('Bye!')
      break
    elif option == 'd':
      selected_card.deposit(input('how much? '))
    elif option == 'r':
      selected_card.withdraw(input('how much? '))
    elif option == 'm':
      selected_card.show_balance()
    elif option == 't':
      selected_card.transfer(input('how much? '))










