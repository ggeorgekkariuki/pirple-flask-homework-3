import sqlite3

# Create a connection - link to the database
connection = sqlite3.connect('homework3.db',check_same_thread=False)

# Create a Curson object - Executes SQL statements
user_cursor = connection.cursor()
lists_cursor = connection.cursor()


# Create the Users Table
user_cursor.execute(
    """
    CREATE TABLE users (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(255),
        username VARCHAR(32),
        password VARCHAR(32)
    );
    """
)

# Create the To Do Lists Table
lists_cursor.execute(
    """
    CREATE TABLE toDoList (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        date_created TEXT,
        title TEXT,
        body TEXT,
        user VARCHAR(32),
        date_modified TEXT
    );
    """
)

# Close the connection and cursor
connection.commit()
user_cursor.close()
lists_cursor.close()
connection.close()