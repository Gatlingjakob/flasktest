import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="flaskapp"
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO scores (ht_score, at_score) VALUES (%s, %s)"
val = (3, 1)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")