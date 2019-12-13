import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='college'
)

cursor = mydb.cursor()

# Here we call the 'get-std' procedure and passing the parameter to procedure
cursor.callproc('get_std', [4, ])
print("Printing student details")

print("Type of the cursor:", type(cursor))

print("Type of the result of calling procedure", type(cursor.stored_results()))
# Getting result of the stored procedure
for result in cursor.stored_results():
    print(result.fetchall())

# Close the cursor and database connection.
if (mydb.is_connected()):
        cursor.close()
        mydb.close()
        print("MySQL connection is closed")