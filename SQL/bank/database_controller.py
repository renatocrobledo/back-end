from sqlite3 import connect
from account_class import Account
connection = connect("accounts.db")
cursor = connection.cursor()
accounts_list = []

sql_command = """
                CREATE TABLE IF NOT EXISTS accounts(
                  id INTEGER PRIMARY KEY,
                  balance FLOAT,
                  account_number VARCHAR(20)
                );
                """

cursor.execute(sql_command)

def get_accounts_from_disk():
  sql_command = 'SELECT * FROM accounts;'
  cursor.execute(sql_command)
  result = cursor.fetchall()

  for register in result:
      (id, balance, account_number) = register
      new_account = Account(balance, account_number)
      accounts_list.append(new_account) 

def save_accounts():
  sql_command = 'DELETE FROM accounts;'
  cursor.execute(sql_command)

  for account in accounts_list:
    sql_command = f'INSERT INTO accounts(id, balance, account_number) VALUES (NULL, "{account.balance}", "{account.account_number}");'
    cursor.execute(sql_command)
    connection.commit()

def save_and_exit():
    print('Bye!')
    save_accounts()
    connection.close()

get_accounts_from_disk()