from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitter:
    def __init__(self):
        pass

    @staticmethod
    def split_documents(docs):
        return RecursiveCharacterTextSplitter().split_documents(docs)
