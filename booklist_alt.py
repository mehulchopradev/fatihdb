from pymysql import connect
from pymysql.cursors import DictCursor

con = connect(host='localhost', user='root', password='root', db='fatih_db', cursorclass=DictCursor)

with con:
  cursor = con.cursor()
  query = 'select title, price from books where price > 500 order by price desc'

  cursor.execute(query)

  rows = cursor.fetchall()
  for row in rows:
    print(f'Title : {row["title"]}')
    print(f'Price : {row["price"]}')