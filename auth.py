from connect import getconnection

username = input('Enter username : ')
password = input('Enter password : ')

query = 'select id from users where username=%s and password=%s'

with getconnection() as cursor:
  cursor.execute(query, (username, password))

  row = cursor.fetchone()
  if row is not None:
    print('Valid user')
  else:
    print('Invalid username or password')