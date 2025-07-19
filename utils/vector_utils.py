from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def build_vector_store(chunks: list):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = FAISS.from_texts(chunks, embedding=embeddings)
    return vectordb
