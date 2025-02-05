import sqlite3

# Connect to SQLite (or create the database file if it doesn’t exist)
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Create a table to store emails
cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        subject TEXT,
        body TEXT
    )
''')

# Save changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully!")

