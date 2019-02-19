from connect import getconnection

username = input('Enter username whom u want to deactivate : ')

query = 'delete from users where username=%s'

with getconnection() as cursor:
  rowsaffected = cursor.execute(query, (username,))
  if rowsaffected:
    print('Delete successful')
  else:
    print('Nothing deleted. did u enter the right username?')