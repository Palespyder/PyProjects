import sqlite3
import typer
from datetime import datetime

# Initialize Typer CLI app
app = typer.Typer()

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create the todo_items table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS todo_items (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date_added TEXT,
                 task TEXT,
                 status TEXT
             )''')
conn.commit()

@app.command()
def add(task: str):
    """
    Add a new task to the todo list.

    Parameters:
    - task (str): The description of the task to add.
    """
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO todo_items (date_added, task, status) VALUES (?, ?, ?)", (date_added, task, 'open'))
    conn.commit()
    typer.echo(f"Task '{task}' added!")

@app.command()
def list():
    """
    List all tasks from the todo list.
    """
    c.execute("SELECT id, task, status FROM todo_items")
    tasks = c.fetchall()
    
    if tasks:
        for task in tasks:
            typer.echo(f"{task[0]}. {task[1]} [{task[2]}]")
    else:
        typer.echo("No tasks found.")

@app.command()
def complete(task_id: int):
    """
    Mark a task as complete.

    Parameters:
    - task_id (int): The ID of the task to mark as complete.
    """
    c.execute("UPDATE todo_items SET status = 'complete' WHERE id = ?", (task_id,))
    conn.commit()
    typer.echo(f"Task {task_id} marked as complete!")

@app.command()
def delete(task_id: int):
    """
    Delete a task from the todo list.

    Parameters:
    - task_id (int): The ID of the task to delete.
    """
    c.execute("DELETE FROM todo_items WHERE id = ?", (task_id,))
    conn.commit()
    typer.echo(f"Task {task_id} deleted!")

if __name__ == "__main__":
    app()
