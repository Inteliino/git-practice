
import sys
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import closing

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import tasks
import statistics


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_tasks.db"

        with closing(sqlite3.connect(self.db_path)) as conn:
            conn.execute("""
                CREATE TABLE tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    completed INTEGER NOT NULL DEFAULT 0,
                    priority TEXT NOT NULL DEFAULT 'Medium'
                )
            """)
            conn.commit()

        self.db_patch = patch.object(tasks, "DB_PATH", self.db_path)
        self.db_patch.start()

        self.stats_patch = patch.object(statistics, "DB_PATH", self.db_path)
        self.stats_patch.start()

    def tearDown(self):
        self.stats_patch.stop()
        self.db_patch.stop()
        self.temp_dir.cleanup()

    def test_add_task(self):
        task_id = tasks.add_task("Learn Python", "High")

        with closing(sqlite3.connect(self.db_path)) as conn:
            result = conn.execute(
                "SELECT title, completed, priority FROM tasks WHERE id = ?",
                (task_id,)
            ).fetchone()

        self.assertEqual(result, ("Learn Python", 0, "High"))

    def test_edit_task(self):
        task_id = tasks.add_task("Original task", "Medium")

        tasks.edit_task(task_id, "Updated task")

        with closing(sqlite3.connect(self.db_path)) as conn:
            result = conn.execute(
                "SELECT title FROM tasks WHERE id = ?",
                (task_id,)
            ).fetchone()

        self.assertEqual(result[0], "Updated task")

    def test_delete_task(self):
        task_id = tasks.add_task("Task to delete", "Low")

        tasks.delete_task(task_id)

        with closing(sqlite3.connect(self.db_path)) as conn:
            result = conn.execute(
                "SELECT id FROM tasks WHERE id = ?",
                (task_id,)
            ).fetchone()

        self.assertIsNone(result)

    def test_task_statistics(self):
        first_id = tasks.add_task("First task", "High")
        tasks.add_task("Second task", "Low")

        tasks.complete_task(first_id)

        result = statistics.get_task_statistics()

        self.assertEqual(result["total"], 2)
        self.assertEqual(result["completed"], 1)
        self.assertEqual(result["pending"], 1)
        self.assertEqual(result["completion_rate"], 50.0)

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            tasks.add_task("Invalid task", "Unknown")

        with closing(sqlite3.connect(self.db_path)) as conn:
            total = conn.execute(
                "SELECT COUNT(*) FROM tasks"
            ).fetchone()[0]

        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
