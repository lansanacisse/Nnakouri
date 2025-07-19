import wikipedia
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_wikipedia_content(query: str) -> str:
    wikipedia.set_lang("fr")
    try:
        page = wikipedia.page(query)
        return page.content
    except Exception as e:
        return f"Erreur : {e}"

def split_text(text: str, chunk_size=500, overlap=50) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)
