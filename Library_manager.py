import sqlite3
from datetime import date, datetime, timedelta

from database import connect_db


class LibraryManager:

    # ---------------------------------
    # Calculate Fine
    # ---------------------------------
    def calculate_fine(self, due_date, return_date):

        if isinstance(due_date, str):

            due_date = datetime.strptime(
                due_date,
                "%Y-%m-%d"
            ).date()

        if return_date <= due_date:
            return 0

        late_days = (return_date - due_date).days

        return late_days * 10

    # ---------------------------------
    # Issue Book
    # ---------------------------------
    def issue_book(self, student_id, book_id):

        conn, cursor = connect_db()

        try:

            # -----------------------------
            # Check Student Exists
            # -----------------------------
            cursor.execute("""
            SELECT 1
            FROM students
            WHERE student_id = ?
            """, (student_id,))

            if cursor.fetchone() is None:

                return {

                    "success": False,
                    "message": "Student not found.",
                    "data": None

                }

            # -----------------------------
            # Check Overdue Books
            # -----------------------------
            current_date = date.today()

            cursor.execute("""
            SELECT 1
            FROM issued_books
            WHERE student_id = ?
            AND due_date < ?
            AND return_date IS NULL
            """, (
                student_id,
                current_date
            ))

            if cursor.fetchone() is not None:

                return {

                    "success": False,
                    "message": "You have an overdue book. Please return it first.",
                    "data": None

                }

            # -----------------------------
            # Check Book Exists
            # -----------------------------
            cursor.execute("""
            SELECT *
            FROM books
            WHERE book_id = ?
            """, (book_id,))

            book = cursor.fetchone()

            if book is None:

                return {

                    "success": False,
                    "message": "Book not found.",
                    "data": None

                }
            book_id, title, author, quantity = book

            # -----------------------------
            # Check Quantity
            # -----------------------------
            if quantity <= 0:

                return {

                    "success": False,
                    "message": "Book is currently unavailable.",
                    "data": None

                }

            # -----------------------------
            # Check Duplicate Issue
            # -----------------------------
            cursor.execute("""
            SELECT 1
            FROM issued_books
            WHERE student_id = ?
            AND book_id = ?
            AND return_date IS NULL
            """, (
                student_id,
                book_id
            ))

            if cursor.fetchone() is not None:

                return {

                    "success": False,
                    "message": "You have already issued this book.",
                    "data": None

                }

            # -----------------------------
            # Issue Book
            # -----------------------------
            issue_date = current_date
            due_date = issue_date + timedelta(days=15)

            cursor.execute("""
            INSERT INTO issued_books(
                student_id,
                book_id,
                issue_date,
                due_date
            )
            VALUES (?, ?, ?, ?)
            """, (
                student_id,
                book_id,
                issue_date,
                due_date
            ))

            # -----------------------------
            # Reduce Quantity
            # -----------------------------
            cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = ?
            """, (book_id,))

            conn.commit()

            return {

                "success": True,
                "message": "Book issued successfully.",

                "data": {

                    "book_id": book_id,
                    "title": title,
                    "author": author,
                    "issue_date": str(issue_date),
                    "due_date": str(due_date)

                }

            }

        except sqlite3.Error as e:

            return {

                "success": False,
                "message": f"Database Error: {e}",
                "data": None

            }

        finally:

            conn.close()


    # ---------------------------------
    # Return Book
    # ---------------------------------
    def return_book(self, student_id, book_id):

        conn, cursor = connect_db()

        try:

            # -----------------------------
            # Check Student Exists
            # -----------------------------
            cursor.execute("""
            SELECT 1
            FROM students
            WHERE student_id = ?
            """, (student_id,))

            if cursor.fetchone() is None:

                return {

                    "success": False,
                    "message": "Student not found.",
                    "data": None

                }

            # -----------------------------
            # Check Book Exists
            # -----------------------------
            cursor.execute("""
            SELECT 1
            FROM books
            WHERE book_id = ?
            """, (book_id,))

            if cursor.fetchone() is None:

                return {

                    "success": False,
                    "message": "Book not found.",
                    "data": None

                }

            # -----------------------------
            # Find Active Issue Record
            # -----------------------------
            cursor.execute("""
            SELECT issue_id, due_date
            FROM issued_books
            WHERE student_id = ?
            AND book_id = ?
            AND return_date IS NULL
            """, (
                student_id,
                book_id
            ))

            issue_record = cursor.fetchone()

            if issue_record is None:

                return {

                    "success": False,
                    "message": "No active issue record found.",
                    "data": None

                }
            issue_id, due_date = issue_record
            # -----------------------------
            # Return Date
            # -----------------------------
            return_date = date.today()

            # -----------------------------
            # Calculate Fine
            # -----------------------------
            fine = self.calculate_fine(
                due_date,
                return_date
            )

            # -----------------------------
            # Update Issue Record
            # -----------------------------
            cursor.execute("""
            UPDATE issued_books
            SET
                return_date = ?,
                fine = ?
            WHERE issue_id = ?
            """, (
                return_date,
                fine,
                issue_id
            ))

            # -----------------------------
            # Increase Book Quantity
            # -----------------------------
            cursor.execute("""
            UPDATE books
            SET quantity = quantity + 1
            WHERE book_id = ?
            """, (book_id,))

            conn.commit()

            return {

                "success": True,

                "message": "Book returned successfully.",

                "data": {

                    "student_id": student_id,
                    "book_id": book_id,
                    "return_date": str(return_date),
                    "fine": fine

                }

            }

        except sqlite3.Error as e:

            return {

                "success": False,

                "message": f"Database Error: {e}",

                "data": None

            }

        finally:

            conn.close()
    
    # ---------------------------------
    # Dashboard Statistics
    # ---------------------------------
    def get_dashboard_statistics(self):

        conn, cursor = connect_db()

        try:

            # Total Students
            cursor.execute("""
            SELECT COUNT(*)
            FROM students
            """)
            total_students = cursor.fetchone()[0]

            # Number of Book Titles
            cursor.execute("""
            SELECT COUNT(*)
            FROM books
            """)
            total_titles = cursor.fetchone()[0]

            # Available Books
            cursor.execute("""
            SELECT SUM(quantity)
            FROM books
            """)
            available_books = cursor.fetchone()[0] or 0

            # Currently Issued Books
            cursor.execute("""
            SELECT COUNT(*)
            FROM issued_books
            WHERE return_date IS NULL
            """)
            issued_books = cursor.fetchone()[0]

            return {

                "success": True,

                "message": "Dashboard statistics retrieved successfully.",

                "data": {

                    "total_students": total_students,
                    "total_titles": total_titles,
                    "available_books": available_books,
                    "issued_books": issued_books

                }

            }

        except sqlite3.Error as e:

            return {

                "success": False,
                "message": f"Database Error: {e}",
                "data": None

            }

        finally:

            conn.close()        