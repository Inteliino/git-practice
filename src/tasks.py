
import sqlite3

from database import DB_PATH, run_migrations


def add_task(title):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, 0)",
            (title,)
        )
        task_id = cursor.lastrowid

    print(f"Task added: {title} (ID: {task_id})")
    return task_id


def list_tasks():
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, title, completed FROM tasks ORDER BY id"
        ).fetchall()

    print("\nTask list:")
    for task_id, title, completed in rows:
        status = "Completed" if completed else "Pending"
        print(f"{task_id}. {title} [{status}]")

    return rows


def delete_task(task_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

    if cursor.rowcount:
        print("Task deleted")
    else:
        print("Invalid task ID")


def edit_task(task_id, new_title):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "UPDATE tasks SET title = ? WHERE id = ?",
            (new_title, task_id)
        )

    if cursor.rowcount:
        print("Task updated")
    else:
        print("Invalid task ID")


def complete_task(task_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )

    if cursor.rowcount:
        print("Task completed")
    else:
        print("Invalid task ID")


if __name__ == "__main__":
    run_migrations()
    list_tasks()
