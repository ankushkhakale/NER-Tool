import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_named_entities(text):
    """
    Uses deepseek AI to identify named entities (people, organizations, locations, dates).
    I'm building this project to enhance my applications in AI Text processing and NLP.
    """
    prompt = f"Extract named entities (people, organizations, locations, dates) from the following text:\n\n{text}\n\nNamed Entities:"
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json().get("response", "No entities found.")
    else:
        return f"Error: {response.text}"
    
#Gradio Interface
interface = gr.Interface(
    fn=extract_named_entities,
    inputs=gr.Textbox(lines=10, placeholder="Enter text here..."),
    outputs=gr.Textbox(label="Extracted Entities"),
    title="AI-Powered Named Entity Recognition Extractor",
)

interface.launch()