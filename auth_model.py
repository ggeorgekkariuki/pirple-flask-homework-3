import sqlite3
from sqlite3.dbapi2 import connect

# This method is for new sign ins
def signup(username, email, password):

    data = (username, email, password)
    # Create a connection
    connection = sqlite3.connect('homework3.db', check_same_thread=False)

    # Create a Cursor
    cursor = connection.cursor()

    # Execute SQL Commands
    #  This is to check if the email address already exists
    cursor.execute(
        """
        SELECT email FROM users WHERE email="{email}" OR username="{username}";
        """
        .format(email=email, username=username)
    )

    exists = cursor.fetchone()

    # If the email does not exist, add the user to the db and return a message
    if exists is None:
        sql = """INSERT INTO users (username, email, password) VALUES (?, ?, ?);"""
        cursor.execute(sql, data)

        last_id = cursor.lastrowid

        # Close the cursor/ connection
        connection.commit()
        cursor.close()
        connection.close()

        # Add a SUCCESS message
        return last_id
    else:
        error_message = "Credentials are already taken"
        return error_message

def find_username(id):

    # Create a connection
    connection = sqlite3.connect('homework3.db', check_same_thread=False)

    # Create a Cursor
    cursor = connection.cursor()

    # Execute SQL Commands
    #  This is to check if the email address already exists
    cursor.execute(
        """
        SELECT username FROM users WHERE id="{user_id}";
        """
        .format(user_id=id)
    )

    username = cursor.fetchone()[0]