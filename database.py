import sqlite3

connection=sqlite3.connect(
    "tasks.db",
    check_same_thread=False
)

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL
)
""")

connection.commit()

cursor.execute("SELECT COUNT(*) FROM tasks")

count=cursor.fetchone()[0]

if count==0:
    cursor.executemany(
        """
        INSERT INTO tasks(title, done)
        VALUES (?, ?)
        """,
        [
            ("Complete assignment", 0),
            ("Go to gym", 1),
            ("Practice DSA", 0)
        ]
    )
    connection.commit()

    print("Inserted sample tasks.")

print("Database initialized successfully!")
