import streamlit as st

from Library_manager import LibraryManager


library = LibraryManager()


def show():

    st.title("📖 Issue Book")

    student_id = st.text_input(
        "Student ID",
        key="issue_student"
    )

    book_id = st.text_input(
        "Book ID",
        key="issue_book"
    )

    if st.button("Issue Book"):

        result = library.issue_book(
            student_id,
            book_id
        )

        if result["success"]:

            st.success(result["message"])

            data = result["data"]

            st.subheader("📘 Issue Details")

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Book ID :** {data['book_id']}")
                st.write(f"**Title :** {data['title']}")
                st.write(f"**Author :** {data['author']}")

            with col2:

                st.write(f"**Issue Date :** {data['issue_date']}")
                st.write(f"**Due Date :** {data['due_date']}")

        else:

            st.error(result["message"])