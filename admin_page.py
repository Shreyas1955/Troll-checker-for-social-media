import streamlit as st
import mysql.connector

#Function to connect to existing MySQL database
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  #Replace with your MySQL username
        password="",  #Replace with your MySQL password
        database="social_media_platform"
    )
    return conn

#Function to retrieve logs from the database
def get_logs():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    conn.close()
    return logs

#Streamlit UI for Admin Page
def admin_page():
    st.title("Admin Page - View Comment Logs")

    #Display logs in a table
    logs = get_logs()
    if logs:
        st.write("### Comment Logs")
        for log in logs:
            st.write(f"**Username:** {log['username']}")
            st.write(f"**Comment:** {log['comment']}")
            st.write(f"**Classification:** {log['classification']}")
            if log.get('rephrased_comment'):
                st.write(f"**Rephrased Comment:** {log['rephrased_comment']}")
            st.write(f"**Timestamp:** {log['timestamp']}")
            st.write("---")
    else:
        st.write("No logs found.")

    #Filter logs (by date, username, classification)
    st.write("### Filter Logs")
    filter_username = st.text_input("Filter by Username")
    filter_classification = st.selectbox("Filter by Classification", ["All", "Hate Speech", "Offensive Language", "Neither"])

    #Apply filters (if any)
    filtered_logs = logs
    if filter_username:
        filtered_logs = [log for log in logs if filter_username.lower() in log['username'].lower()]
    if filter_classification != "All":
        filtered_logs = [log for log in filtered_logs if log['classification'] == filter_classification]

    #Display filtered logs
    if filtered_logs:
        st.write("### Filtered Logs")
        for log in filtered_logs:
            st.write(f"**Username:** {log['username']}")
            st.write(f"**Comment:** {log['comment']}")
            st.write(f"**Classification:** {log['classification']}")
            if log.get('rephrased_comment'):
                st.write(f"**Rephrased Comment:** {log['rephrased_comment']}")
            st.write(f"**Timestamp:** {log['timestamp']}")
            st.write("---")
    else:
        st.write("No logs match the filter criteria.")
