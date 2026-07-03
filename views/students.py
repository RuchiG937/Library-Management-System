import pandas as pd
import streamlit as st

from student import Student


student = Student()


def show():

    st.title("👨‍🎓 Student Management")

    # ---------------------------------
    # Import Students
    # ---------------------------------
    with st.expander("📥 Import Students"):

        if st.button("Import Students from CSV"):

            with st.spinner("Importing students..."):

                result = student.import_students()

            if result["success"]:

                st.success(result["message"])

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        label="✅ Imported",
                        value=result["data"]["imported"]
                    )

                with col2:

                    st.metric(
                        label="⏭️ Skipped",
                        value=result["data"]["skipped"]
                    )

            else:

                st.error(result["message"])

    # ---------------------------------
    # Search Student
    # ---------------------------------
    with st.expander("🔍 Search Student"):

        student_id = st.text_input(
            "Enter Student ID",
            key="search_student"
        )

        if st.button("Search Student"):

            result = student.search_student(student_id)

            if result["success"]:

                st.success(result["message"])

                student_data = result["data"]

                st.subheader("👤 Student Details")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(f"**Student ID :** {student_data['student_id']}")
                    st.write(f"**Name :** {student_data['name']}")
                    st.write(f"**Email :** {student_data['email']}")

                with col2:

                    st.write(f"**Mobile :** {student_data['mobile']}")
                    st.write(f"**Department :** {student_data['department']}")
                    st.write(f"**Year :** {student_data['year']}")

            else:

                st.error(result["message"])

    # ---------------------------------
    # View All Students
    # ---------------------------------
    with st.expander("📋 View All Students"):

        if st.button(
            "Show All Students",
            key="show_students"
        ):

            result = student.view_students()

            if result["success"]:

                df = pd.DataFrame(result["data"])

                st.success(
                    f"Total Students : {len(df)}"
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No students found.")