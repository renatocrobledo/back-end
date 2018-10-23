from database_controller import cursor, accounts_list, connection, save_accounts, save_and_exit, Account

def menu():
  return input(' [d] Deposit \n [r] withdraw \n [s] Show Balance \n [t] Transfer \n [delete] delete_account \n [e] Exit \n')

def get_account_option():
  return input(' [a] Add account \n [v] View or select account \n [e] Exit \n')

def show_accounts():
  print("========Account List======")
  for position, account in enumerate(accounts_list):
    print(f"[{position}]", account)
  print("==========================")

def add_account():
    try:
      account_number = input('account number? ')
      balance = float(input('How much balance ? ') or "0.0")
      new_account = Account(balance, account_number)
      accounts_list.append(new_account)   
      show_accounts()
    except Exception as error:
      print('Eeehm something wrong!', error)

def card_logic(selected_card):
  while True:
      option = menu()
      if option == 'e':
        print('Bye!')
        break
      elif option == 'delete':
        selected_card.remove_this_account()
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


while True:
  account_option = get_account_option()
  selected_card = None
  if account_option == 'e':
    save_and_exit()
    break
  elif account_option == 'a':
    add_account()
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
  card_logic(selected_card)


