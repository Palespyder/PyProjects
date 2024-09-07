import typer
import sqlite3
from datetime import datetime

app = typer.Typer()


"""@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")"""

@app.command()
def init():
    # Connect to SQLite database (it will create the database if it doesn't exist)
    conn = sqlite3.connect(f'todo.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # SQL query to create a new table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS todo_items (
        date TEXT,
        item TEXT,
        status TEXT
    )
    '''

    # Execute the query to create the table
    cursor.execute(create_table_query)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    print("Database and table initialized successfully.")


@app.command()
def insert(item: str):
    # Connect to the SQLite database
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Define the item to insert
    todo_item = item
    status = "open"

    # SQL query to insert a new row into the todo_items table
    insert_query = '''
    INSERT INTO todo_items (date, item, status)
    VALUES (?, ?, ?)
    '''

    # Execute the query with the values (current date, item, and status)
    cursor.execute(insert_query, (current_datetime, todo_item, status))

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    print("New to-do item inserted successfully.")


@app.command()
def list_open_todos():
    # Connect to the SQLite database
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()

    # SQL query to select all open to-do items
    select_query = '''
    SELECT date, item, status FROM todo_items WHERE status = 'open'
    '''

    # Execute the query and fetch all results
    cursor.execute(select_query)
    open_todos = cursor.fetchall()

    # Close the connection
    conn.close()

    # Check if there are any open to-do items
    if open_todos:
        typer.echo("Open To-Do Items:")
        for todo in open_todos:
            date, item, status = todo
            typer.echo(f"Date: {date}, Item: {item}, Status: {status}")
    else:
        typer.echo("No open to-do items found.")






if __name__ == "__main__":
    app()