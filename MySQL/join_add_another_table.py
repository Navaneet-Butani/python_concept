import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()


# Create table
query = ("CREATE TABLE teacher (t_name VARCHAR(25), branch VARCHAR(25))")
my_curs.execute(query)


# Insert into table 
query_ins = ("INSERT INTO teacher (t_name, branch) VALUES (%s, %s)")
values = (
    ('Mr. Joshi', 'CE'),
    ('Mr. Desai', 'ME'),
    ('Mr. Patel', 'EE'),
    ('Mr. Sikhavat', 'ME'),
    ('Mr. Malik', 'EE')
)
my_curs.executemany(query_ins, values)

# Save the changes
mydb.commit()


# Select all records
my_curs.execute('SELECT * FROM teacher')
result = my_curs.fetchall()

for record in result:
    print(record)
