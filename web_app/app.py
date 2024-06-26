import datetime
import streamlit as st
from web_app.ai_models import  google
from web_app.loaders import web_loader
from web_app.core import prompts, text_splitter, vectorstores
from web_app.utils import helpers
from langchain_openai import OpenAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings



class Chatbot_main:
    def __init__(self):
        self.st = st
        self.helpers = helpers

    def configure_page(self):
        self.st.set_page_config(page_title="Nipurn's Rag-Chain App", page_icon=":robot:")
        self.st.title("Nipurn's Rag-Chain App")
        self.st.markdown("""
        This app allows you to ask questions based on the content of a document. 
        Select a Generative AI Model, provide the API key if applicable, and ask your question to get the answer.
        """)

    def get_model_name_and_api_key(self):
        model_name = self.st.sidebar.selectbox("Choose Generative AI Model", ["Nipurn's LLM", "GPT3.5-Turbo"])
        api_key = None
        if model_name == "GPT3.5-Turbo":
            api_key = self.st.sidebar.text_input("Enter your OpenAI API Key:")
        elif model_name == "Nipurn's LLM":
            api_key = "AIzaSyADEdfxRrcyqB-Kp-5u5CYjDrKNnxokWXQ"
        return model_name, api_key

    def get_document_url(self):
        return self.st.text_input("Enter the website url you would like to chat with:")

    def load_document(self, url):
        return web_loader.DocumentLoader().load_document(url)

    def initialize_embeddings(self):
         return OpenAIEmbeddings(openai_api_key="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")

    def initialize_embeddings1(self):
        # Provide your Google API key here
        google_api_key = "AIzaSyADEdfxRrcyqB-Kp-5u5CYjDrKNnxokWXQ"

        # Initialize Google embeddings with the provided API key
        return GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=google_api_key)   
       

    def split_documents(self, docs):
        return text_splitter.TextSplitter().split_documents(docs)

    def create_vector_store(self, documents, embeddings):
        return vectorstores.VectorStore().create_vector_store(documents, embeddings)

    def define_prompt(self):
        return prompts.ChatPrompt().define_prompt()
    
    def create_document_chain(self, llm, prompt):
        return create_stuff_documents_chain(llm, prompt)

    def create_retrieval_chain(self, retriever, document_chain):
        return create_retrieval_chain(retriever, document_chain)

    def display_message(self, message):
        self.st.markdown(message)

    def display_error(self, error_message):
        self.st.error(error_message)

    def display_success(self, success_message):
        self.st.success(success_message)

    def display_info(self, info_message):
        self.st.info(info_message)

    def get_user_input(self):
        return self.st.text_input("Give your input prompt:")

    def get_current_timestamp(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def display_disclaimer(self):
        self.st.sidebar.write("Disclaimer: This app uses AI to generate responses. The answers may not always be accurate.")

    @st.cache(allow_output_mutation=True)
    def load_and_process_document(self, url):
        docs = self.load_document(url)
        embeddings = self.initialize_embeddings1()
        documents = self.split_documents(docs)
        vector = self.create_vector_store(documents, embeddings)
        return docs, vector

    def stream_main(self):
        model_name, api_key = self.get_model_name_and_api_key()
        url = self.get_document_url()

        if url:
            try:
                docs, vector = self.load_and_process_document(url)

                if model_name == "Nipurn's LLM":
                    llm = google.ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, convert_system_message_to_human=True)
                elif model_name == "GPT3.5-Turbo":
                    llm = ChatOpenAI(openai_api_key= api_key)
                else:
                    self.display_error("Invalid model selected.")
                    return

                prompt = self.define_prompt()
                document_chain = self.create_document_chain(llm, prompt)
                retriever = vector.as_retriever()
                retrieval_chain = self.create_retrieval_chain(retriever, document_chain)

                self.display_success("Document loaded successfully!")

                if "messages" not in st.session_state:
                    st.session_state.messages = []

                if "max_messages" not in st.session_state:
                    # Counting both user and assistant messages, so 10 rounds of conversation
                    st.session_state.max_messages = 20

                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                if prompt := st.chat_input("You:"):
                    # Display user message in chat message container
                    st.chat_message("user").write(prompt)
                    # Add user message to chat history
                    st.session_state.messages.append({"role": "user", "content": prompt})

                    # Generate prompt including chat history
                    user_input = prompt

                    for message in st.session_state.messages:
                        if message["role"] == "user":
                            user_input += f'User: {message["content"]}\n'
                        elif message["role"] == "assistant":
                            user_input += f'Assistant: {message["content"]}\n'

                    prompt = ChatPromptTemplate.from_messages([
                        ("system", '''# Act as a prompt engineer. Follow the principles and Interaction guidelines to help the user by rating the prompt and giving feedback. ## Prompt: [] ## Testing_Criteria: - Content: - Clarity - Relevance - Flexibility - Simplicity - Modularity - Purpose - Value - Actionability - Duplication - Presentation: - Readability - Tone - Formatting - Syntax - Grammar - Spelling - Punctuation ## Prompt_Type: - System_Prompt - these are the prompts that are used by the system to interact with the user and are in background and not visible to the user - User_Prompt - these are given by the user ## Goals: - Help the user by rating the prompt and giving feedback. - Give 1 - 10 rating for each <testing_criteria> - provide feedback for each <testing_criteria> - provide improvement suggestions for each <testing_criteria> - provide overall rating for the prompt ## Interaction guidelines: - Introduce yourself as a prompt engineer who is eager to help the user by rating the prompt and giving feedback. first ask the user what is the <prompt_type> they would like to discuss and then Wait for the user's response. - ask the user to describe the <prompt> and tell them that you can also help them rate, compare, improve or write new prompts and then Wait for the user's response. - when rating and comparing then rate and compare the prompt against the <testing_criteria> and achieve your <goals> then Wait for the user's response. - when user asks for suggestions for improvements then improve prompts to better meet the <testing_criteria> and then Wait for the user's response. - when writing new prompts then write prompts that meet the <testing_criteria> and then Wait for the user's response. - ask the user if they are satisfied and have any more questions and then Wait for the user's response. - keep the conversation going by asking the user if they would like to discuss anything else and then Wait for the user's response. If the user ask to give enhanced prompt give tat as well '''),
                        ("user", "{input}")
                    ])
                    

                    # Once user_input is fetched, proceed with further processing
                    context = user_input
                    response = retrieval_chain.invoke({"input": context})
                    with st.chat_message("assistant"):
                        st.markdown(response['answer'])
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response['answer']})
            except Exception as e:
                self.display_error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    bot = Chatbot_main()
    bot.stream_main()
