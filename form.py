import streamlit as st
import mysql.connector

# MySQL configurations
db_config = {
    'user': 'root',
    'password': '',  # Default XAMPP MySQL password is empty
    'host': 'localhost',
    'database': 'resume_db'
}

# Streamlit UI for resume submission form
st.title("Resume Submission Form")
st.subheader("Fill Form and Get Chance To Work With ProCoderJii 🤗")

name = st.text_input("Name")
email = st.text_input("Email")
location = st.text_input("Location")
college_name = st.text_input("College Name")  # Added college name input
study_year = st.number_input("Study Year", min_value=1, max_value=5, step=1)
branch = st.text_input("Branch")
age = st.number_input("Age", min_value=16, max_value=100, step=1)
resume = st.file_uploader("Upload your resume", type=["pdf", "docx", "doc"])

if st.button("Submit"):
    if name and email and location and college_name and branch and age and resume:  # Check for college name
        try:
            # Convert the uploaded file to binary (BLOB)
            resume_data = resume.read()

            # Establish a database connection
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert the data into the database
            cursor.execute(
                'INSERT INTO resumes (name, email, location, college_name, study_year, branch, age, resume) '
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (name, email, location, college_name, study_year, branch, age, resume_data)
            )
            connection.commit()

            # Close the connection
            cursor.close()
            connection.close()

            st.success("Resume submitted successfully!")

        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
    else:
        st.error("Please fill in all fields and upload a resume.")
