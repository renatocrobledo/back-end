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

def parse_to_integer(str_number):
    try:
      return float(str_number)
    except ValueError:
      return print('ups! solo numeros son admitidos!')

class Account():
  def __init__(self, balance = 0):
      self.balance = balance
  def deposit(self, quantity):
    value = parse_to_integer(quantity)
    if value:
      self.balance += value
  def withdraw(self, quantity):
    value = parse_to_integer(quantity)
    if value:
      if value > self.balance:
        return print('metase a chambear machin!')
      self.balance -= value
  def show_balance(self):
    print(f"Tienes ${self.balance} en tu cuenta")

def menu():
  return input(' [d] Depositar \n [r] Retirar \n [m] Mostrar Balance \n [s] Salir \n')

account_1 = Account()

while True:
  option = menu()
  if option == 's':
     print('Bye!')
     break
  elif option == 'd':
    account_1.deposit(input('how much? '))
  elif option == 'r':
    account_1.withdraw(input('how much? '))
  elif option == 'm':
    account_1.show_balance()










