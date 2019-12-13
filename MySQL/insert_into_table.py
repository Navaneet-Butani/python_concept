import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

# Insert into the table with one column
# my_curs.execute("INSERT INTO student (name, branch) VALUES ('Jay', 'CE')")


# Let's insert many rows together

query = "INSERT INTO student (name, branch) VALUES (%s, %s)"

row_val = [
    ('Kevin', 'ME'),
    ('Sachin', 'EE'),
    ('Rahul', 'EC'),
    ('Rohit', 'CE'),
    ('Jatin', 'ME')
]

my_curs.executemany(query, row_val)

# Save the changes in databse
mydb.commit()

# No. of rows affected
print("Inserted no of rows:", my_curs.rowcount)