import sqlite3

DATABASE_NAME = "library.db"


def connect_db():
    """
    Create and return a database connection and cursor.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    return conn, cursor


def create_tables():
    """
    Create all required tables if they do not already exist.
    """

    conn, cursor = connect_db()

    try:

        # -----------------------------
        # Students Table
        # -----------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            department TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """)

        # -----------------------------
        # Books Table
        # -----------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """)

        # -----------------------------
        # Issued Books Table
        # -----------------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS issued_books(
            issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            book_id TEXT NOT NULL,
            issue_date DATE NOT NULL,
            due_date DATE NOT NULL,
            return_date DATE,
            fine INTEGER DEFAULT 0,

            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
        )
        """)

        conn.commit()

        print("Database and tables created successfully.")

    except sqlite3.Error as e:

        print("Database Error:", e)

    finally:

        conn.close()


if __name__ == "__main__":
    create_tables()