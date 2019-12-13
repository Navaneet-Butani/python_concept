import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="college"
)

my_curs = mydb.cursor()

# INNER JOIN
my_curs.execute("SELECT student.name, student.branch, teacher.t_name FROM student INNER JOIN teacher ON student.branch = teacher.branch")

result_inner = my_curs.fetchall()

print("Inner join result:")
for record in result_inner:
    print(record)


# LEFT JOIN
my_curs.execute("SELECT student.name, student.branch, teacher.t_name FROM student LEFT JOIN teacher ON student.branch = teacher.branch")
result_left = my_curs.fetchall()

print("LEFT join result:")
for record in result_left:
    print(record)


# RIGHT JOIN
my_curs.execute("SELECT student.name, student.branch, teacher.t_name FROM student RIGHT JOIN teacher ON student.branch = teacher.branch")
result_left = my_curs.fetchall()

print("LEFT join result:")
for record in result_left:
    print(record)


# FULL JOIN
# We can't directly do FULL JOIN in MySQL
# But we can do that by the UNION of LEFT JOIN and RIGHT
my_curs.execute("SELECT student.name, student.branch, teacher.t_name FROM student LEFT JOIN teacher ON student.branch = teacher.branch \
                UNION \
                SELECT student.name, student.branch, teacher.t_name FROM student RIGHT JOIN teacher ON student.branch = teacher.branch")

result_full = my_curs.fetchall()

print("FULL JOIN result:")
for record in result_full:
    print(record)
