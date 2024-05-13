import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

class ChatApp:
    def __init__(self):
        self.model_name = ""
        self.api_key = None

    def select_model(self):
        st.sidebar.title("Welcome to the Prompt Perfekt App! Let's optimize your input prompt!!")
       
        self.model_name = st.sidebar.selectbox("Choose Generative AI Model", ["Nipurn's LLM", "Gemini","Ollama"])
        if self.model_name == "Nipurn's LLM":
            self.api_key = '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'
        elif self.model_name == "Gemini":
            self.api_key = st.sidebar.text_input("Enter your Google API Key:") # Sample API Key

    def display_messages(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def user_input(self):
        
        if prompt := st.chat_input("Message PromptPerfekt.."):
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
            return prompt

    def prepare_prompt(self, prompt_with_history):
        for message in st.session_state.messages:
            role = message["role"]
            content = message["content"]
            prompt_with_history += f'{role.capitalize()}: {content}\n'
        return prompt_with_history

    def select_ai_model(self):
        if self.model_name == "Nipurn's LLM":
            return ChatOpenAI(openai_api_key=self.api_key)

        elif self.model_name == "Gemini":
            return ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.api_key, convert_system_message_to_human=True)
        
    def run(self):
        st.title("Prompt Perfekt")
        st.write("Let's optmize your input prompt for best possible output quality")
                
        self.select_model()
        self.display_messages()
        user_prompt = self.user_input()
        if user_prompt:
            prompt_with_history = self.prepare_prompt(user_prompt)

            ai_model = self.select_ai_model()

            prompt = ChatPromptTemplate.from_messages([
                ("system", "Your task is to optimize the input prompt given by the user and that to using all kind of advanced prompt engeneeering techniques so to say and dont answer the user prompt just optimize that  "),
                ("user", prompt_with_history)
            ])

            chain = prompt | ai_model
            response = chain.invoke({"input": prompt_with_history})

            with st.chat_message("assistant"):
                st.markdown(f"Answer: {response.content}")

            st.session_state.messages.append({"role": "assistant", "content": response.content})

def prompt_main():
    app = ChatApp()
    app.run()

if __name__ == "__main__":
    prompt_main()

