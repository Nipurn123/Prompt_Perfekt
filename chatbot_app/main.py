import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
import time

class Bot:
    def __init__(self):
        self.llm = None
        self.model_name, self.api_key = self.get_model_name_and_api_key()

        if self.model_name == "Gemini":
            self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.api_key, convert_system_message_to_human=True)
        elif self.model_name == "GPT3.5-Turbo":
            if self.api_key is not None:
                self.llm = ChatOpenAI(openai_api_key=self.api_key)

    def get_model_name_and_api_key(self):
        model_name = st.sidebar.selectbox("Choose Generative AI Model", ["Gemini", "GPT3.5-Turbo"])
        api_key = None
        if model_name == "GPT3.5-Turbo":
            api_key = st.sidebar.text_input("Enter your OpenAI API Key:")
        elif model_name == "Gemini":
            api_key = "AIzaSyADEdfxRrcyqB-Kp-5u5CYjDrKNnxokWXQ"  # Replace with your actual API key
        return model_name, api_key

    def display_message(self, message):
        st.markdown(message)

    def run(self):
        st.title("Bot")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "max_messages" not in st.session_state:
            # Counting both user and assistant messages, so 10 rounds of conversation
            st.session_state.max_messages = 20

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message['content'])

        if prompt := st.chat_input("Message PromptPerfekt.."):
            # Display user message in chat message container
            st.chat_message("user").write(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            # Generate prompt including chat history
            prompt_with_history = prompt + "If you dont get any other data other than user input simply answer the  user input and if you get some data aprt from user input then give the answer  by taking refrence of that data and if no refrence you got still answer the question  "
            for message in st.session_state.messages:
                if message["role"] == "user":
                    prompt_with_history += f'User: {message["content"]}\n'
                elif message["role"] == "assistant":
                    prompt_with_history += f'Assistant: {message["content"]}\n'

            # Invoke language model with prompt including history
            response = self.llm.invoke(prompt_with_history)

            def stream_data():
                for word in response.content.split(" "):
                    yield word + " "
                    time.sleep(0.02)

            with st.chat_message("assistant"):
                st.write_stream(stream_data)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.content})

if __name__ == "__main__":
    bot = Bot()
    bot.run()
