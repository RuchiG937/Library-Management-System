import streamlit as st


def show():

    # ---------------------------------
    # Header
    # ---------------------------------

    st.title("📚 Library Management System")

    

    st.divider()

    # ---------------------------------
    # Features
    # ---------------------------------

    st.header("✨ Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("👨‍🎓 Student Management")

        st.write("""
- Import Students
- View Students
- Search Students
""")

        st.success("📚 Book Management")

        st.write("""
- Import Books
- Add New Books
- Increase Book Quantity
- Search Books
""")

    with col2:

        st.success("📖 Library Operations")

        st.write("""
- Issue Books
- Return Books
- Automatic Fine Calculation
""")

        st.success("🛡 Business Rules")

        st.write("""
- Prevent duplicate book issue
- Prevent issuing when books are overdue
- Quantity management
""")

    st.divider()

    # ---------------------------------
    # Technologies
    # ---------------------------------

    st.header("🛠 Technologies Used")

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.info("🐍 Python")

    with tech2:
        st.info("🗄 SQLite")

    with tech3:
        st.info("🏗 OOP")

    with tech4:
        st.info("🌐 Streamlit")

    st.divider()

    # ---------------------------------
    # Quick Guide
    # ---------------------------------

    st.header("🚀 Quick Navigation")

    st.write("""
1. Import Students from CSV

2. Import Books from CSV

3. Issue Books

4. Return Books

5. Monitor Library Statistics from the Dashboard
""")

    st.divider()

    st.success("✅ Library Management System is Ready to Use!")

    st.caption(
        "Developed by Ruchi  | Python • SQLite • Streamlit"
    )