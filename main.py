import os
from dotenv import load_dotenv
import gradio as gr
from llama_index.core import VectorStoreIndex, Settings
from llama_index.readers.file import PDFReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()

Settings.llm = Groq(
    model = "llama-3.1-8b-instant",
    api_key = os.getenv("GROQ_API_KEY")
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name = "BAAI/bge-small-en-v1.5"
)

query_engine = None

def load_pdf(file):
    
    global query_engine
    reader = PDFReader()
    document = reader.load_data(file = file.name)
    index = VectorStoreIndex.from_documents(document)
    query_engine = index.as_query_engine()

    return "PDF Loaded"

def ask_question(question):

    if not query_engine:
        return "Upload PDF"
    
    response = query_engine.query(question)

    return str(response)

with gr.Blocks() as app:

    gr.Markdown("PDF Q&A")

    with gr.Row():

        file_input = gr.File(
            label = "Upload PDF",
            file_types = [".pdf"]
        )

        load_status = gr.Textbox(
            label = "Status",
            interactive = False
        )

    file_input.change(
        fn = load_pdf,
        inputs = file_input,
        outputs = load_status
    )

    question_input = gr.Textbox(
        label = "Ask a Question"
    )

    answer_output = gr.Textbox(
        label = "Answer",
        interactive = False
    )

    ask_btn = gr.Button("Ask")

    ask_btn.click(
        fn = ask_question,
        inputs = question_input,
        outputs = answer_output
    )

app.launch()