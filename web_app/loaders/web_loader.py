from langchain_community.document_loaders import WebBaseLoader

class DocumentLoader:
    def __init__(self):
        pass

    def load_document(self,url):
        return WebBaseLoader(url).load()
