import streamlit as st

class ChatInterface:
    @staticmethod
    def display_chat_message(role, content):
        with st.chat_message(role):
            st.markdown(content)

    @staticmethod
    def get_user_input():
        prompt=st.chat_input("You:")
        return prompt 
