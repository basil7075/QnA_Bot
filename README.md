# Q&A Bot

A simple AI-powered PDF Question & Answer application built with Python, LlamaIndex, Groq, and Gradio. Upload a PDF and ask questions about its contents in natural language.

## Features

- Upload PDF documents
- Ask questions about the uploaded PDF
- Uses LlamaIndex for document indexing and retrieval
- Uses Groq LLM for generating answers
- Simple Gradio web interface

## Tech Stack

- Python
- Gradio
- LlamaIndex
- Groq API
- HuggingFace Embeddings
- python-dotenv

## Installation

1. Clone the repository.

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project directory.

```env
GROQ_API_KEY=your_api_key_here
```

4. Run the application.

```bash
python main.py
```

## Usage

1. Open the Gradio interface in your browser.
2. Upload a PDF.
3. Wait until the status shows **PDF Loaded**.
4. Enter a question about the document.
5. Click **Ask** to receive an answer.

## Project Structure

```
.
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Requirements

- Python 3.10+
- Groq API Key
## License

This project is for educational purposes.
