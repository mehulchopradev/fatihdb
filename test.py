import pymysql

con = pymysql.connect(host='localhost', user='root', password='root', db='fatih_db')
with con:
  print('Connection acquired')
  print(con)