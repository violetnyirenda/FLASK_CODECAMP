import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("test.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a query to retrieve data
cursor.execute("SELECT * FROM todo")

# Fetch all rows from the result
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the connection
conn.close()
