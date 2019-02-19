from connect import getconnection

query = 'select * from books'

with getconnection() as cursor:
  cursor.execute(query)

  '''row = cursor.fetchone() # does not fetch all the rows at once from db to memory
  while row is not None:
    # print(row) # tuple
    print(f'Title : {row[1]}')
    print(f'Price : {row[2]}')

    row = cursor.fetchone()'''

  #rows = cursor.fetchall() # fetches all the rows at once from db to memory
  # use it carefully. Do not use it on tables with large number of rows
  '''for row in rows:
    print(f'Title : {row[1]}')
    print(f'Price : {row[2]}')'''

  firstbatch = cursor.fetchmany(2) # fetch 2 rows at once from db into memory
  # get data (rows) in batches
  print(firstbatch)

  secondbatch = cursor.fetchmany(2)
  print(secondbatch)