import streamlit as st
from send_email import send_email

with st.form(key='email_forms'):
    user_email = st.text_input("Your email address")
    select_box = st.selectbox("What topic do you want to discuss?", ('Job inquiries', 'Project proposal', 'Others'))
    text = st.text_area("Text")

    raw_message = st.text_area("Your message ")
    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully")
