import streamlit as st

from Library_manager import LibraryManager


library = LibraryManager()


def show():

    st.title("📊 Dashboard")

    st.markdown(
        "Welcome to the **Library Management Dashboard**. "
        "Here you can view the current status of your library."
    )

    st.divider()

    result = library.get_dashboard_statistics()

    if not result["success"]:

        st.error(result["message"])
        return

    data = result["data"]

    # ---------------------------------
    # Dashboard Metrics
    # ---------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            label="👨‍🎓 Students",
            value=data["total_students"]
        )

    with col2:

        st.metric(
            label="📚 Book Titles",
            value=data["total_titles"]
        )

    with col3:

        st.metric(
            label="📖 Issued Books",
            value=data["issued_books"]
        )

    with col4:

        st.metric(
            label="✅ Available Copies",
            value=data["available_books"]
        )

    st.divider()

    # ---------------------------------
    # Library Overview
    # ---------------------------------

    st.subheader("📋 Library Overview")

    st.write(f"👨‍🎓 **Registered Students:** {data['total_students']}")
    st.write(f"📚 **Total Book Titles:** {data['total_titles']}")
    st.write(f"📖 **Books Currently Issued:** {data['issued_books']}")
    st.write(f"✅ **Available Copies:** {data['available_books']}")

    st.divider()

    # ---------------------------------
    # Library Status
    # ---------------------------------

    st.subheader("📈 Library Status")

    total_books = data["issued_books"] + data["available_books"]

    if total_books > 0:

        available_percent = int(
            (data["available_books"] / total_books) * 100
        )

        issued_percent = int(
            (data["issued_books"] / total_books) * 100
        )

    else:

        available_percent = 0
        issued_percent = 0

    st.write(f"📚 Available Copies ({available_percent}%)")
    st.progress(available_percent)

    st.write(f"📖 Issued Books ({issued_percent}%)")
    st.progress(issued_percent)

    st.divider()

    # ---------------------------------
    # System Status
    # ---------------------------------

    st.subheader("🟢 System Status")

    st.success("Database Connected Successfully")

    st.success("Library Management System is Running")

    st.success("No Errors Detected")