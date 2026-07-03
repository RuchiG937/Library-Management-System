from database import create_tables
from student import Student
from book import Book
from Library_manager import LibraryManager


student = Student()
book = Book()
library = LibraryManager()


# ---------------------------------
# Display Result
# ---------------------------------
def display_result(result):

    print("\n" + "=" * 50)

    print(result["message"])

    if result["success"] and result["data"]:

        data = result["data"]

        if isinstance(data, list):

            for item in data:

                print("-" * 50)

                for key, value in item.items():

                    print(f"{key.capitalize():12}: {value}")

        elif isinstance(data, dict):

            print("-" * 50)

            for key, value in data.items():

                print(f"{key.capitalize():12}: {value}")

    print("=" * 50)


# ---------------------------------
# Main Menu
# ---------------------------------
def main():

    create_tables()

    while True:

        print("""
========== Library Management System ==========

1. Import Students
2. View Students
3. Search Student

4. Import Books
5. Add New Book
6. Increase Book Quantity
7. View Books
8. Search Book

9. Issue Book
10. Return Book

0. Exit

===============================================
""")

        choice = input("Enter your choice: ")

        # -----------------------------
        # Students
        # -----------------------------
        if choice == "1":

            result = student.import_students()
            display_result(result)

        elif choice == "2":

            result = student.view_students()
            display_result(result)

        elif choice == "3":

            student_id = input("Enter Student ID: ")

            result = student.search_student(student_id)
            display_result(result)

        # -----------------------------
        # Books
        # -----------------------------
        elif choice == "4":

            result = book.import_books()
            display_result(result)

        elif choice == "5":

            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))

            result = book.add_new_book(
                book_id,
                title,
                author,
                quantity
            )

            display_result(result)

        elif choice == "6":

            book_id = input("Enter Book ID: ")
            copies = int(input("Enter Copies: "))

            result = book.increase_book_quantity(
                book_id,
                copies
            )

            display_result(result)

        elif choice == "7":

            result = book.view_books()
            display_result(result)

        elif choice == "8":

            book_id = input("Enter Book ID: ")

            result = book.search_book(book_id)
            display_result(result)

        # -----------------------------
        # Library
        # -----------------------------
        elif choice == "9":

            student_id = input("Enter Student ID: ")
            book_id = input("Enter Book ID: ")

            result = library.issue_book(
                student_id,
                book_id
            )

            display_result(result)

        elif choice == "10":

            student_id = input("Enter Student ID: ")
            book_id = input("Enter Book ID: ")

            result = library.return_book(
                student_id,
                book_id
            )

            display_result(result)

        # -----------------------------
        # Exit
        # -----------------------------
        elif choice == "0":

            print("\nThank you for using Library Management System.")
            break

        else:

            print("\nInvalid Choice!")


if __name__ == "__main__":

    main()