
import sqlite3

from database import DB_PATH, run_migrations

VALID_PRIORITIES = ("Low", "Medium", "High")


def add_task(title, priority="Medium"):
    if priority not in VALID_PRIORITIES:
        raise ValueError("Invalid priority")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed, priority) VALUES (?, 0, ?)",
            (title, priority)
        )
        task_id = cursor.lastrowid

    print(f"Task added: {title} [{priority}]")
    return task_id


def list_tasks():
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, title, completed, priority FROM tasks ORDER BY id"
        ).fetchall()

    print("\nTask list:")
    for task_id, title, completed, priority in rows:
        status = "Completed" if completed else "Pending"
        print(f"{task_id}. {title} [{status}] [{priority}]")

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
