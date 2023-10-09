import streamlit as st
import send_email
import re

st.header("Contact Us")

with st.form(key="Email_form"):
    options = ["Freelance", "Teach", "Report an issue", "Other"]
    user_option = st.selectbox("What topic do you want to discuss?", options)

    user_email = st.text_input("Enter your email")
    user_message = st.text_area("Enter your message")


    message = f"""\
Subject: New email from {user_email}

From: {user_email} 
Topic: {user_option}

Message:

{user_message} 
"""
# the break line on 13 is important to show the email address in the message.

    button = st.form_submit_button("Submit")

    if button and not re.match(r"[^@]+@[^@]+\.[^@]+",
                               user_email):
        st.warning("Please enter a valid email address")

    elif button and re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
        send_email.send_email_wow(message)
        st.success("Email sent successfully")
