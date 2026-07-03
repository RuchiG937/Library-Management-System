import csv
import sqlite3

from database import connect_db


class Book:

    CSV_FILE = "books.csv"

    # ---------------------------------
    # Import Books
    # ---------------------------------
    def import_books(self):

        conn, cursor = connect_db()

        try:

            with open(self.CSV_FILE, "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                imported = 0
                skipped = 0

                for row in reader:

                    try:

                        cursor.execute("""
                        INSERT INTO books(
                            book_id,
                            title,
                            author,
                            quantity
                        )
                        VALUES (?, ?, ?, ?)
                        """, (
                            row["book_id"],
                            row["title"],
                            row["author"],
                            row["quantity"]
                        ))

                        imported += 1

                    except sqlite3.IntegrityError:

                        skipped += 1

                conn.commit()

                return {

                    "success": True,
                    "message": "Books imported successfully.",
                    "data": {

                        "imported": imported,
                        "skipped": skipped

                    }

                }

        except FileNotFoundError:

            return {

                "success": False,
                "message": "books.csv file not found.",
                "data": None

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
    # Add New Book
    # ---------------------------------
    def add_new_book(self, book_id, title, author, quantity):

        conn, cursor = connect_db()

        try:

            cursor.execute("""
            INSERT INTO books(
                book_id,
                title,
                author,
                quantity
            )
            VALUES (?, ?, ?, ?)
            """, (
                book_id,
                title,
                author,
                quantity
            ))

            conn.commit()

            return {

                "success": True,
                "message": "Book added successfully.",
                "data": None

            }

        except sqlite3.IntegrityError:

            return {

                "success": False,
                "message": "Book ID already exists.",
                "data": None

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
    # Increase Book Quantity
    # ---------------------------------
    def increase_book_quantity(self, book_id, copies):

        if copies <= 0:

            return {

                "success": False,
                "message": "Copies must be greater than zero.",
                "data": None

            }

        conn, cursor = connect_db()

        try:

            cursor.execute("""
            UPDATE books
            SET quantity = quantity + ?
            WHERE book_id = ?
            """, (
                copies,
                book_id
            ))

            if cursor.rowcount == 0:

                return {

                    "success": False,
                    "message": "Book not found.",
                    "data": None

                }

            conn.commit()

            return {

                "success": True,
                "message": f"{copies} copies added successfully.",
                "data": None

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
    # View Books
    # ---------------------------------
    def view_books(self):

        conn, cursor = connect_db()

        try:

            cursor.execute("""
            SELECT *
            FROM books
            ORDER BY book_id
            """)

            books = cursor.fetchall()

            if not books:

                return {

                    "success": False,
                    "message": "No books available.",
                    "data": []

                }

            books_data = []

            for book in books:

                books_data.append({

                    "book_id": book[0],
                    "title": book[1],
                    "author": book[2],
                    "quantity": book[3]

                })

            return {

                "success": True,
                "message": "Books retrieved successfully.",
                "data": books_data

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
    # Search Book
    # ---------------------------------
    def search_book(self, book_id):

        conn, cursor = connect_db()

        try:

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

            book_data = {

                "book_id": book[0],
                "title": book[1],
                "author": book[2],
                "quantity": book[3]

            }

            return {

                "success": True,
                "message": "Book found.",
                "data": book_data

            }

        except sqlite3.Error as e:

            return {

                "success": False,
                "message": f"Database Error: {e}",
                "data": None

            }

        finally:

            conn.close()