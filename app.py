from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/extract_entities/")
def extract_named_entities(text: str):
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Extract named entities (people, organizations, locations, dates) from the following text:\n\n{text}\n\nNamed Entities:",
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No entities detected.")

# Run the app with: uvicorn app:app --reload
