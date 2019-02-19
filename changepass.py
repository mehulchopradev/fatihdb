from connect import getconnection

username = input('Enter username whose password u want to change : ')
password = input('Enter the new password')

query = 'update users set password=%s where username=%s'

with getconnection() as cursor:
  rowsaffected = cursor.execute(query, (password, username))
  if rowsaffected:
    print('Update successful')
  else:
    print('Nothing updated. did u enter the right username?')