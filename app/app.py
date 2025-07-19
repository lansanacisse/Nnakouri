import streamlit as st
import sys
import os
# Add the parent directory to the system path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.wikipedia_scraper import get_wikipedia_content
from streamlit_option_menu import option_menu

# pages
from search_plat import search_page
from home import home_page
from restaurant import restaurant
import glob

st.set_page_config(page_title="Nnakouri", layout="centered")

# Navigation using streamlit_option_menu
selected = option_menu(
    menu_title=None,
    options=["Home", "Search", "Country", "Recipes", "Africain"],
    icons=["house", "search", "globe", "book", "shop"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    home_page()
elif selected == "Search":
    search_page()
elif selected == "Country":
    st.write("See soon!")
elif selected == "Recipes":
    st.write("See soon!")
elif selected == "Africain":
    restaurant()

