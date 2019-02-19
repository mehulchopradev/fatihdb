from connect import getconnection

title = input('Enter title: ')
price = float(input('Enter price: '))
pages = int(input('Enter pages: '))

query = 'insert into books (title, price, pages) values(%s, %s, %s)' # Prepared statements
# fast and secure

with getconnection() as cursor:
  # query = f'insert into books (title, price, pages) values(\'{title}\', {price}, {pages})'
  cursor.execute(query, (title, price, pages))

