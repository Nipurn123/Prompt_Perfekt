from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self):
        pass

    @staticmethod
    def create_vector_store(documents, embeddings):
        return FAISS.from_documents(documents, embeddings)
