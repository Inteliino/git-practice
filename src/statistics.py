
import sqlite3
from contextlib import closing

from database import DB_PATH


def get_task_statistics():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        total = conn.execute(
            "SELECT COUNT(*) FROM tasks"
        ).fetchone()[0]

        completed = conn.execute(
            "SELECT COUNT(*) FROM tasks WHERE completed = 1"
        ).fetchone()[0]

        pending = conn.execute(
            "SELECT COUNT(*) FROM tasks WHERE completed = 0"
        ).fetchone()[0]

    completion_rate = (
        round(completed / total * 100, 2)
        if total > 0 else 0.0
    )

    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": completion_rate,
    }


def show_statistics():
    stats = get_task_statistics()

    print("\n===== TASK STATISTICS =====")
    print(f"Total tasks: {stats['total']}")
    print(f"Completed tasks: {stats['completed']}")
    print(f"Pending tasks: {stats['pending']}")
    print(f"Completion rate: {stats['completion_rate']}%")


if __name__ == "__main__":
    show_statistics()
