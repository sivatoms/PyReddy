import mysql.connector

# Connecting to a database
con = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = '1234',
    database = 'Shiva',
    port = 3306

)

print("Hey , I Think I'm connected")

# Cursor
cur = con.cursor()  # if you specify name in the () it is a server side cursor, or else it is client side cursor

# Push data 100 records
for i in range(100):
    cur.execute("insert into Student values(%s, %s)", (f'Reddy{i}', f'TU{i+10}'))  # the vlause that we are passing are tuple
#Execute the query  - Pull data
cur.execute("Select * from Student")

rows = cur.fetchall()

for i in rows:
    print(f" Name = {i[0]} College = {i[1]}")

con.commit()
# Close the cursor
cur.close()
#Close the connection
con.close()

# install mysql using - >    pip install mysql-connector-python