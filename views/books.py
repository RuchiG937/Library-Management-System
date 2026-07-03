import pandas as pd
import streamlit as st

from book import Book


book = Book()


def show():

    st.title("📚 Book Management")

    # ---------------------------------
    # Import Books
    # ---------------------------------
    with st.expander("📥 Import Books"):

        if st.button("Import Books from CSV"):

            with st.spinner("Importing books..."):

                result = book.import_books()

            if result["success"]:

                st.success(result["message"])

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "✅ Imported",
                        result["data"]["imported"]
                    )

                with col2:

                    st.metric(
                        "⏭️ Skipped",
                        result["data"]["skipped"]
                    )

            else:

                st.error(result["message"])

    # ---------------------------------
    # Add New Book
    # ---------------------------------
    with st.expander("➕ Add New Book"):

        book_id = st.text_input(
            "Book ID",
            key="add_book_id"
        )

        title = st.text_input(
            "Title",
            key="add_title"
        )

        author = st.text_input(
            "Author",
            key="add_author"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1,
            key="add_quantity"
        )

        if st.button("Add Book"):

            result = book.add_new_book(
                book_id,
                title,
                author,
                quantity
            )

            if result["success"]:

                st.success(result["message"])

            else:

                st.error(result["message"])

    # ---------------------------------
    # Increase Quantity
    # ---------------------------------
    with st.expander("📈 Increase Book Quantity"):

        book_id = st.text_input(
            "Book ID",
            key="increase_book_id"
        )

        copies = st.number_input(
            "Copies",
            min_value=1,
            step=1,
            key="increase_copies"
        )

        if st.button("Increase Quantity"):

            result = book.increase_book_quantity(
                book_id,
                copies
            )

            if result["success"]:

                st.success(result["message"])

            else:

                st.error(result["message"])

    # ---------------------------------
    # Search Book
    # ---------------------------------
    with st.expander("🔍 Search Book"):

        book_id = st.text_input(
            "Enter Book ID",
            key="search_book"
        )

        if st.button("Search Book"):

            result = book.search_book(book_id)

            if result["success"]:

                st.success(result["message"])

                book_data = result["data"]

                st.subheader("📖 Book Details")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(f"**Book ID :** {book_data['book_id']}")
                    st.write(f"**Title :** {book_data['title']}")

                with col2:

                    st.write(f"**Author :** {book_data['author']}")
                    st.write(f"**Quantity :** {book_data['quantity']}")

            else:

                st.error(result["message"])

    # ---------------------------------
    # View All Books
    # ---------------------------------
    with st.expander("📋 View All Books"):

        if st.button(
            "Show All Books",
            key="show_books"
        ):

            result = book.view_books()

            if result["success"]:

                df = pd.DataFrame(result["data"])

                st.success(
                    f"Total Books : {len(df)}"
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No books available.")