
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "tasks.db"
MIGRATIONS_DIR = BASE_DIR / "migrations"

def run_migrations():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                filename TEXT PRIMARY KEY
            )
        """)

        for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
            applied = conn.execute(
                "SELECT 1 FROM schema_migrations WHERE filename = ?",
                (migration.name,)
            ).fetchone()

            if applied:
                continue

            sql = migration.read_text(encoding="utf-8")
            conn.executescript(sql)

            conn.execute(
                "INSERT INTO schema_migrations (filename) VALUES (?)",
                (migration.name,)
            )

            print(f"Applied migration: {migration.name}")

if __name__ == "__main__":
    run_migrations()
    print("Database is ready!")
