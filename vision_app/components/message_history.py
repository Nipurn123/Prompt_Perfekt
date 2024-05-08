import streamlit as st 
class MessageHistory:
    @staticmethod
    def get_chat_history(messages, max_messages):
        return "\n".join(f'{m["role"].capitalize()}: {m["content"]}' for m in messages[-max_messages:])