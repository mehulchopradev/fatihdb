from pymysql import connect

def getconnection():
  return connect(host='localhost', user='root', password='root', db='fatih_db')