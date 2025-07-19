from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def build_qa_chain(vectordb):
    retriever = vectordb.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain
