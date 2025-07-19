import streamlit as st
import sys
import os
# Add the parent directory to the system path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.wikipedia_scraper import get_wikipedia_content


from utils.vector_utils import build_vector_store
from utils.qa_chain import build_qa_chain
from utils.wikipedia_scraper import split_text

def search_page():
    st.header("🔍 Recherche Wikipédia augmentée (RAG)")

    topic = st.text_input("Entrez un sujet culinaire africain :", "Cuisine ivoirienne")

    if st.button("Charger les données"):
        with st.spinner("Chargement de Wikipédia..."):
            content = get_wikipedia_content(topic)
            chunks = split_text(content)
            vectordb = build_vector_store(chunks)
            st.session_state.vectordb = vectordb
        st.success("Index vectoriel prêt ✅")

    if "vectordb" in st.session_state:
        question = st.text_input("Posez votre question :")
        if question:
            chain = build_qa_chain(st.session_state.vectordb)
            with st.spinner("Recherche de la réponse..."):
                answer = chain.run(question)
            st.markdown("### ✨ Réponse :")
            st.write(answer)
