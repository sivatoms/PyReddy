import psycopg2


# Open Connetion
conn = psycopg2.connect(
        host = "localhost",
        database = "Register",
        user = "postgres",
        password = "1234"
)

# Open Cursor
cur = conn.cursor()

# Insert data into table
cur.execute("insert into Registration(Id,Name,Username,Password) values(%s, %s, %s, %s)", (2,'Reddy','Reddy123', '1234'))

# Select data from a database
cur.execute("Select id, Name, Username from Registration")

# accesss all the data of table into rows
rows = cur.fetchall()

# fetching the data and printing using rows
for i in rows:
    print(f" id {i[0]} name {i[1]} Username {i[2]} ")
# Commit transaction -- wil insert data into data into table registration
conn.commit()
#Close Cursor
cur.close()
# Close Connection
conn.close()