# 🍛 Nnakouri - African Culinary Intelligence Assistant

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Nnakouri is an intelligent assistant designed to celebrate and showcase the rich culinary heritage of the African continent. Using a RAG (Retrieval-Augmented Generation) system, it leverages Wikipedia knowledge to suggest traditional recipes, compose balanced menus, and provide interactive cooking guidance.

## 🌟 Features

- **🔍 RAG-Powered Search**: Enhanced Wikipedia search for African culinary topics
- **🍽️ Recipe Discovery**: Find traditional African recipes and cooking techniques
- **🌍 Country-Based Exploration**: Discover cuisine by African countries
- **🗺️ Restaurant Mapping**: Interactive map to locate African restaurants
- **📚 Knowledge Base**: Comprehensive information about African food culture
- **🤖 Interactive Assistant**: AI-powered cooking guidance and menu suggestions

## 🏗️ Architecture

The application is built using:
- **Frontend**: Streamlit for the web interface
- **Backend**: Python with LangChain for RAG implementation
- **Vector Database**: FAISS for similarity search
- **Knowledge Source**: Wikipedia scraping for African cuisine content
- **Embeddings**: HuggingFace all-MiniLM-L6-v2 model
- **LLM**: OpenAI GPT-3.5-turbo for question answering

## 📁 Project Structure

```
Nnakouri/
├── app/
│   ├── app.py              # Main Streamlit application
│   ├── home.py             # Home page component
│   ├── search_plat.py      # RAG-powered search functionality
│   ├── restaurant.py       # Interactive restaurant map
│   ├── country.py          # Country-based cuisine exploration
│   └── recipes.py          # Recipe management (coming soon)
├── utils/
│   ├── qa_chain.py         # Question-answering chain setup
│   ├── vector_utils.py     # Vector store utilities
│   └── wikipedia_scraper.py # Wikipedia content extraction
├── databases/
│   ├── database.py         # Database setup and management
│   └── african_countries.db # SQLite database for African countries
├── assets/
│   └── nnakouri.png        # Application logo
└── requirements.txt        # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for GPT-3.5-turbo)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Nnakouri.git
   cd Nnakouri
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Initialize the database:**
   ```bash
   python databases/database.py
   ```

5. **Run the application:**
   ```bash
   streamlit run app/app.py
   ```

The application will open in your browser at `http://localhost:8501`.

## 🎯 Usage

### Home Page
Welcome interface introducing Nnakouri and its features for African cuisine discovery.

### Search Functionality
1. Enter an African culinary topic (e.g., "Ivorian cuisine", "Jollof rice")
2. Click "Load Data" to fetch and process Wikipedia content
3. Ask questions about the loaded content
4. Get AI-powered answers based on the retrieved information

### Restaurant Mapping
Interactive map showing African restaurants with location details and cuisine types.

### Country Exploration
Browse African cuisines organized by country with filtering capabilities.

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[LangChain](https://langchain.com/)** - LLM application framework
- **[FAISS](https://faiss.ai/)** - Vector similarity search
- **[HuggingFace Transformers](https://huggingface.co/transformers/)** - Text embeddings
- **[OpenAI GPT-3.5](https://openai.com/)** - Language model for Q&A
- **[Wikipedia API](https://wikipedia-api.readthedocs.io/)** - Content extraction
- **[Folium](https://folium.readthedocs.io/)** - Interactive maps
- **[SQLite](https://sqlite.org/)** - Local database

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key for GPT-3.5-turbo access

### Customization
- Modify `utils/vector_utils.py` to change embedding models
- Update `utils/qa_chain.py` to use different LLM models
- Adjust chunk size and overlap in `utils/wikipedia_scraper.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Wikipedia for providing extensive knowledge about African cuisine
- The African culinary community for inspiring this project
- OpenAI and HuggingFace for providing powerful AI models
- The open-source community for the amazing tools and libraries

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please feel free to reach out.

---

**Nnakouri** - Celebrating the rich diversity of African cuisine through technology 🌍✨
