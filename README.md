# NER-Tool: AI-Powered Named Entity Recognition

A powerful and user-friendly Named Entity Recognition (NER) tool that leverages the DeepSeek-R1 AI model through Ollama to extract named entities from text. This project provides both a modern web interface using Gradio and a FastAPI backend for seamless integration into other applications.

## 🌟 Features

- **Intelligent Entity Extraction**: Automatically identifies and extracts:
  - 👤 **People** - Names of individuals
  - 🏢 **Organizations** - Companies, institutions, and groups
  - 📍 **Locations** - Cities, countries, and places
  - 📅 **Dates** - Temporal references and time expressions

- **Dual Interface Options**:
  - **Interactive Web UI**: Beautiful Gradio interface for direct user interaction
  - **REST API**: FastAPI backend for programmatic access and integration

- **Local AI Processing**: Uses Ollama with DeepSeek-R1 model for privacy-focused, offline processing
- **Real-time Results**: Fast entity extraction with no streaming delays
- **Simple & Lightweight**: Minimal dependencies, easy to set up and use

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+** - Programming language
- **Ollama** - For running the DeepSeek-R1 model locally
- **DeepSeek-R1 Model** - AI model for entity recognition

### Installing Ollama and DeepSeek-R1

1. **Install Ollama**:
   - Visit [Ollama's website](https://ollama.ai/) and download the installer for your OS
   - Follow the installation instructions

2. **Pull DeepSeek-R1 Model**:
   ```bash
   ollama pull deepseek-r1
   ```

3. **Start Ollama Server**:
   ```bash
   ollama serve
   ```
   - The server will run on `http://localhost:11434`

## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ankushkhakale/NER-Tool.git
   cd NER-Tool
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install fastapi uvicorn gradio requests
   ```

## 💻 Usage

### Option 1: Gradio Web Interface (Recommended for Interactive Use)

The Gradio interface provides an intuitive web UI for extracting named entities:

```bash
python "ner extractor.py"
```

- The interface will open automatically in your default browser
- Or navigate to the provided local URL (typically `http://127.0.0.1:7860`)
- Enter your text in the input box
- Click "Submit" to extract entities
- View the extracted entities in the output section

### Option 2: FastAPI Backend (For API Integration)

The FastAPI backend is perfect for integrating NER capabilities into other applications:

1. **Start the FastAPI Server**:
   ```bash
   uvicorn app:app --reload
   ```

2. **Access the API**:
   - API runs on: `http://localhost:8000`
   - Interactive API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

3. **Make API Requests**:
   ```bash
   curl -X POST "http://localhost:8000/extract_entities/" \
        -H "Content-Type: application/json" \
        -d '{"text": "Elon Musk founded SpaceX in California in 2002."}'
   ```

   Or using Python:
   ```python
   import requests

   response = requests.post(
       "http://localhost:8000/extract_entities/",
       params={"text": "Elon Musk founded SpaceX in California in 2002."}
   )
   print(response.json())
   ```

## 📁 Project Structure

```
NER-Tool/
│
├── app.py                  # FastAPI backend server
├── ner extractor.py        # Gradio web interface
├── README.md               # Project documentation
├── LICENSE                 # License information
└── __pycache__/           # Python cache files
```

## 📝 Example Use Cases

- **Content Analysis**: Analyze articles, documents, and reports
- **Research**: Extract entities from research papers and studies
- **Data Mining**: Process large text datasets for entity information
- **Customer Feedback**: Identify mentioned people, places, and organizations in reviews
- **Legal Documents**: Extract key entities from contracts and legal texts
- **News Monitoring**: Track mentions of specific entities in news articles

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Gradio](https://gradio.app/)** - Easy-to-use UI library for machine learning demos
- **[Ollama](https://ollama.ai/)** - Run large language models locally
- **[DeepSeek-R1](https://ollama.ai/library/deepseek-r1)** - Advanced AI model for text understanding
- **[Python Requests](https://requests.readthedocs.io/)** - HTTP library for API calls


## 🙏 Acknowledgments

- Built with DeepSeek AI for enhanced NER capabilities
- Powered by Ollama for local AI model deployment
- UI created with Gradio for seamless user experience
- API built with FastAPI for robust backend services

**Note**: This project requires Ollama to be running locally. Make sure to start the Ollama server before running either the Gradio interface or the FastAPI backend.
