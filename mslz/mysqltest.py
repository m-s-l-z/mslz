import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="superuser",
  passwd="YES"
)

print(mydb)
