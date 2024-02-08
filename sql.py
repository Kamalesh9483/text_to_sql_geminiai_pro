import sqlite3

#Connect to Sql
connection=sqlite3.connect("Employee.db")

# Cursor to insert record, create table, retrieve
cursor=connection.cursor()

# Create table
table="""
CREATE TABLE EMPLOYEE(NAME VARCHAR(25),
                      DEPARTMENT VARCHAR(25),
                      SECTION VARCHAR(25),
                      SALARY INT);
"""

cursor.execute(table)

# insert records
cursor.execute('''INSERT INTO EMPLOYEE values('Kamalesh','Data Science', 'A', 369)''')
cursor.execute('''INSERT INTO EMPLOYEE values('Einstein','Physics', 'A', 999)''')
cursor.execute('''INSERT INTO EMPLOYEE values('Tesla','Elecrical', 'B', 5490)''')
cursor.execute('''INSERT INTO EMPLOYEE values('Elon','Business', 'C', 9999)''')

print("Records: ")

data=cursor.execute('''SELECT * FROM EMPLOYEE''')

for row in data:
    print(row)

# close connection
connection.commit()
connection.close()

