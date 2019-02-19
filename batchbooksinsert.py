from connect import getconnection

books = []
while True:
  print('1. Add book')
  print('2. Exit')

  choice = int(input('Enter choice : '))
  if choice == 1:
    title = input('Enter title : ')
    price = float(input('Enter price : '))
    pages = int(input('Enter pages : '))

    books.append((title, price, pages))
  else:
    # commit all the book data in one go to the database
    query = 'insert into books(title, price, pages) values(%s, %s, %s)'

    with getconnection() as cursor:
      rowsaffected = cursor.executemany(query, books) # batch insert
      print(f'{rowsaffected} books saved!')
    break