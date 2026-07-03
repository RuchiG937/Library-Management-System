import streamlit as st

from Library_manager import LibraryManager


library = LibraryManager()


def show():

    st.title("↩️ Return Book")

    student_id = st.text_input(
        "Student ID",
        key="return_student"
    )

    book_id = st.text_input(
        "Book ID",
        key="return_book"
    )

    if st.button("Return Book"):

        result = library.return_book(
            student_id,
            book_id
        )

        if result["success"]:

            st.success(result["message"])

            data = result["data"]

            st.subheader("📘 Return Details")

            col1, col2 = st.columns(2)

            with col1:

                st.write(f"**Student ID :** {data['student_id']}")
                st.write(f"**Book ID :** {data['book_id']}")

            with col2:

                st.write(f"**Return Date :** {data['return_date']}")
                st.write(f"**Fine :** ₹{data['fine']}")

        else:

            st.error(result["message"])