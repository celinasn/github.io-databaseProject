import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Akira0330!",
  database="menagerie"
)
x = mydb.cursor()
'''
x.execute("DESCRIBE pet")
results = x.fetchall()
print("| Field      | Type        | Null | Key | Default | Extra |")
for row in results:
    formatted_row = "| {:<10} | {:<11} | {:<4} | {:<3} | {:<7} | {:<5} |".format(
    *(str(col) if col is not None else 'NULL' for col in row)
            )
    print(formatted_row)
x.close()
mydb.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
'''
x.execute("SELECT * FROM pet")
spam = x.fetchall()
for record in spam:
  print(record)
x.close()
mydb.close()
'''
''' 
x.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';")
spam = x.fetchall()
for record in spam:
  print(record)
x.close()
mydb.close()
'''
'''
x.execute("SELECT name, birth FROM pet;")
spam = x.fetchall()
for record in spam:
  print(record)
x.close()
mydb.close()
'''
'''
x.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner;")
spam = x.fetchall()
for record in spam:
  print(record)
x.close()
mydb.close()
'''
'''
x.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner;")
spam = x.fetchall()
for record in spam:
  print(record)
x.close()
mydb.close()
'''
x.execute("SELECT name, birth, MONTH(birth) FROM pet;")
spam = x.fetchall()
print("| name       | birth       | MONTH(birth)|")
print("+_______________________________________+")
for row in spam:
    formatted_row = "| {:<10} | {:<11} |       {:<4} |".format(
    *(str(col) if col is not None else 'NULL' for col in row)
            )
    print(formatted_row)

x.close()
mydb.close()
