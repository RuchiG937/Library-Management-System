import csv
import sqlite3

from database import connect_db


class Student:

    CSV_FILE = "students.csv"

    # ---------------------------------
    # Import Students
    # ---------------------------------
    def import_students(self):

        conn, cursor = connect_db()

        try:

            with open(self.CSV_FILE, "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                imported = 0
                skipped = 0

                for row in reader:

                    try:

                        cursor.execute("""
                        INSERT INTO students(
                            student_id,
                            name,
                            email,
                            mobile,
                            department,
                            year
                        )
                        VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            row["student_id"],
                            row["name"],
                            row["email"],
                            row["mobile"],
                            row["department"],
                            row["year"]
                        ))

                        imported += 1

                    except sqlite3.IntegrityError:
                        skipped += 1

                conn.commit()

                return {
                    "success": True,
                    "message": "Students imported successfully.",
                    "data": {
                        "imported": imported,
                        "skipped": skipped
                    }
                }

        except FileNotFoundError:

            return {
                "success": False,
                "message": "students.csv file not found.",
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
    # View All Students
    # ---------------------------------
    def view_students(self):

        conn, cursor = connect_db()

        try:

            cursor.execute("""
            SELECT *
            FROM students
            ORDER BY student_id
            """)

            students = cursor.fetchall()

            if not students:

                return {
                    "success": False,
                    "message": "No students found.",
                    "data": []
                }

            students_data = []

            for student in students:

                students_data.append({

                    "student_id": student[0],
                    "name": student[1],
                    "email": student[2],
                    "mobile": student[3],
                    "department": student[4],
                    "year": student[5]

                })

            return {

                "success": True,
                "message": "Students retrieved successfully.",
                "data": students_data

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
    # Search Student
    # ---------------------------------
    def search_student(self, student_id):

        conn, cursor = connect_db()

        try:

            cursor.execute("""
            SELECT *
            FROM students
            WHERE student_id = ?
            """, (student_id,))

            student = cursor.fetchone()

            if student is None:

                return {

                    "success": False,
                    "message": "Student not found.",
                    "data": None

                }

            student_data = {

                "student_id": student[0],
                "name": student[1],
                "email": student[2],
                "mobile": student[3],
                "department": student[4],
                "year": student[5]

            }

            return {

                "success": True,
                "message": "Student found.",
                "data": student_data

            }

        except sqlite3.Error as e:

            return {

                "success": False,
                "message": f"Database Error: {e}",
                "data": None

            }

        finally:

            conn.close()