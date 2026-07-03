import streamlit as st
from streamlit_option_menu import option_menu

from views import (
    home,
    dashboard,
    students,
    books,
    issue_book,
    return_book
)

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:

    st.title("📚 Library Management")

    st.markdown("---")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Dashboard",
            "Students",
            "Books",
            "Issue Book",
            "Return Book"
        ],
        icons=[
            "house-fill",
            "speedometer2",
            "people-fill",
            "book-fill",
            "journal-plus",
            "arrow-return-left"
        ],
        menu_icon="book-half",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#262730"
            },
            "icon": {
                "color": "#00C853",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "--hover-color": "#404040",
                "border-radius": "8px"
            },
            "nav-link-selected": {
                "background-color": "#00C853",
                "color": "white",
                "border-radius": "8px"
            },
        }
    )

    st.markdown("---")

    st.info(
        """
### 📖 Library Management System

Manage students, books, issue books and return books through a simple and interactive interface.
"""
    )

    st.markdown("---")

    st.caption(
        """
**Developed by Ruchi**

Python • SQLite • Streamlit
"""
    )

# ---------------------------------
# Page Routing
# ---------------------------------

if selected == "Home":
    home.show()

elif selected == "Dashboard":
    dashboard.show()

elif selected == "Students":
    students.show()

elif selected == "Books":
    books.show()

elif selected == "Issue Book":
    issue_book.show()

elif selected == "Return Book":
    return_book.show()