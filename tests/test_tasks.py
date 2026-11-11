
import sys
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import closing

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import tasks


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

    def tearDown(self):
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


if __name__ == "__main__":
    unittest.main()
