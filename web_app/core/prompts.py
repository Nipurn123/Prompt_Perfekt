from langchain_core.prompts import ChatPromptTemplate

class ChatPrompt:
    def __init__(self):
        pass

    @staticmethod
    def define_prompt():
        return ChatPromptTemplate.from_template("""
            Answer the following question based only on the provided context:

            <context>
            {context}
            </context>

            Question: {input}
            """)
