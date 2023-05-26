import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="",
    database ="db_tp9_customers"
)

# insert
dbcursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
dbcursor.execute(sql,val)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

# Select
dbcursor = mydb.cursor()

dbcursor.execute("SELECT * FROM customers")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)
    
# Delete
dbcursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Highway 21'"

dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, "record(s) deleted")